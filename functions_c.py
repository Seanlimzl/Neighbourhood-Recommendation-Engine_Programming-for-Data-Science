###################################################
##      YSC2244 Programming for Data Science     ##
##                    #######                    ##
## Singapore Neighbourhood Recommendation System ##
##               Callable Functions              ##
###################################################

# Authors: Elizabeth STEPTON, Sean LIM, Joshua VARGAS, NING Xinran

### Import necessary packages ###

import pandas as pd
import geopandas as gpd

### Recommendation Algorithm ###

# Import data
subdistrict_database = gpd.read_file('Generated Files/subzones_featurecount.shp')
x = pd.read_csv('Generated Files/algorithm_x.csv')

# Travel Time
travel_time = gpd.read_file('Generated Files/subzones_all_stats_with_travel.shp')
travel_order = travel_time[['SUBZONE_N','travel__cn']]
resale_and_travel = x.merge(travel_order, how= 'left', on= 'SUBZONE_N')
resale_and_travel['travel__cn'] = resale_and_travel['travel__cn']/60
resale_and_travel.head()

# Input processing
def get_tuples(sliders_dict):
    amenities = ['busstop_no','hawkercent','malls_no','mrtsg_no','schools_no', 'supermarke']
    result = []
    for i in range(6):
        result.append((amenities[i], sliders_dict[i]))
    return result

# Algorithm
def our_algorithm(resale_range, list_of_tuples_from_website, max_travel_time):
    
    #filter out based on resale range
    filtered_resale = resale_and_travel[(resale_range[0] <= resale_and_travel['real_price']) & (resale_and_travel['real_price'] <= resale_range[1])]
    #filter out long travel times
    filtered_travel_time = filtered_resale[filtered_resale['travel__cn']<= max_travel_time]
    #get names of the filtered subdistricts
    filtered_subdistrict_names = filtered_travel_time['SUBZONE_N']

    #initialise result_list
    result_list = []
    
    # using names
    subdistrict_database_prices = subdistrict_database[subdistrict_database['SUBZONE_N'].isin(filtered_subdistrict_names)]
    #reset index
    subdistrict_database_prices = subdistrict_database_prices.reset_index()

    #calculate score for each subdistrict row
    for index, row in subdistrict_database_prices.iterrows():
        #initialise score for row
        result = 0
        #compute based on inputs
        for amenity, score in list_of_tuples_from_website:
            result += list(subdistrict_database_prices.iterrows())[index][1][amenity] * score
        result_list.append((index, result))
    
    #sort the list
    result_list.sort(key = lambda result: result[1], reverse = True)

    #keep the top 10 results
    result_list = result_list[:10]

    #return the database with those results by taking the indices in result_list
    result_database = pd.DataFrame(subdistrict_database_prices.iloc[list(map(lambda result: result[0], result_list))])

    #append their score to the database
    scores_list = []
    for index, score in result_list:
        scores_list.append(score)
    result_database['SCORE'] = scores_list

    #return database
    return result_database

def clean_algorithm_results(result_database):
    # Given the database of our top 10 results,
    # return the desired outputs in a dataframe
    result_clean = pd.DataFrame(result_database.iloc[:,[3,6,8,16,17,18,19,20,21,23]])
    result_clean.columns = ['Subzone', 'Planning Area', 'Region', '# Bus Stops', '# MRT', '# Schools', '# Malls', '# Supermarkets', '# Hawker Centres', 'Score']
    return result_clean

