# %%
!pip install matplotlib

# %%
""" -*- coding: utf-8 -*-
#%% Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#%% Importing Data
flights_data = pd.read_csv('flights.csv')
flights_data.head(10)
weather_data_pd = pd.read_csv('weather.csv')
weather_data_np = weather_data_pd.to_numpy()
#%% Pandas Data Filtering/Sorting Question Answering
#use flights_data
"""
#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#import teh .csv files given for this assignment
flights_data = pd.read_csv('/Users/a14806/Downloads/data/flights.csv')
flights_data.head(10)



#see chart of data printed out so we know what we are dealing with. Find 17 columns and 336776 rows for flights 
flights_data


# %%
#Question 1 How many flights were there from JFK to SLC? Int
#based on printout of flights_data we can see columns origin and dest denoting origin and destination
# Count flights from JFK to SLC
jfktoslc_count = len(flights_data[(flights_data["origin"] == "JFK") & (flights_data["dest"] == "SLC")])

print("Question 1: Number of flights from JFK to SLC:", jfktoslc_count)


# %%
#Question 2 How many airlines fly to SLC? Should be int
#count flights where dest=SLC

slc_count = len(flights_data[(flights_data["dest"] == "SLC")])
(print("Question 2: Number of flights to SLC:", slc_count))

# %%
#Question 3 What is the average arrival delay for flights to RDU? float
#need to find average of delay ONLY for flights that are going to RDU

delay_rdu= flights_data.loc[flights_data["dest"]=="RDU","arr_delay"].mean()
(print("Question 3: Average delay time of flights to RDU is ", delay_rdu))

# %%
#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA and JFK)? float
#find number of flights that come to seattle
to_sea_count=len(flights_data[(flights_data["dest"] == "SEA")])
print("Number of flights to Seattle:",to_sea_count)
#find number of flights that comt to seattle from NYC (LGA or JFK)
nyc_to_sea_count=len(flights_data[(flights_data["dest"] == "SEA") & (flights_data["origin"].isin (["LGA","JFK"]))])
print("Number of flights to Seattle:",nyc_to_sea_count)
prop_flights_sea=nyc_to_sea_count/to_sea_count
print("Question 4: Proportion of flights to SEA that come from teh two NYC airports: ",prop_flights_sea)

# %%
#Question 5 Which date has the largest average depature delay? Pd slice with date and float
#please make date a column. Preferred format is 2013/1/1 (y/m/d)

# Create a new date column that combines the day, month, and year together into one 
flights_data['date'] = pd.to_datetime(flights_data[['year', 'month', 'day']])

# Calculate average departure delay per date with new variable 'date' and drop null values
avg_delay = flights_data.groupby('date')['dep_delay'].mean().dropna()

# Find the date with the largest average departure delay
max_dep_delay = pd.Series([avg_delay.max()], index=[avg_delay.idxmax()])

print("Question 5: Date with the largest average departure delay =",max_dep_delay)

# %%
#Question 6 Which date has the largest average arrival delay? pd slice with date and float

# Calculate average arrival delay per date
avg_arr_delay = flights_data.groupby('date')['arr_delay'].mean().dropna()

# Find the date with the largest average arrival delay
max_arr_delay = pd.Series([avg_arr_delay.max()], index=[avg_arr_delay.idxmax()])
print("Question 6:Date with largest average arrival delay",max_arr_delay)


# %%
#Question 7 Which flight departing LGA or JFK in 2013 flew the fastest? pd slice with tailnumber and speed
#speed = distance/airtime
#Make a new variable for speed (distance/airtime)
flights_data["speed"]=flights_data["distance"]/flights_data["air_time"]
#find the flights that depart ONLY from LGA or JFK in 2013
filtered_flights = flights_data[(flights_data['origin'].isin(['LGA', 'JFK'])) & (flights_data['year'] == 2013)]
#take filtered (LGA and JFK origin)flights and find the fastest one
fastest_flight = filtered_flights.loc[filtered_flights['speed'].idxmax()]
# Find the tailnumber and speed
tailnumber = fastest_flight['tailnum']
speed = fastest_flight['speed']
# Create a pandas series for the result
result = pd.Series({'tailnumber': tailnumber, 'speed': speed})
print("Question 7:",result)

# %%
#%% Numpy Data Filtering/Sorting Question Answering
#Use weather_data_n

#Import weather_data_np
weather_data_pd = pd.read_csv('/Users/a14806/Downloads/data/weather.csv')
weather_data_np = weather_data_pd.to_numpy()
#See weather info : 15 columns and 8719 rows for weather
weather_data_pd

# %%
#Question 8 Replace all nans in the weather pd dataframe with 0s. Pd with no nans

weather_data_cleaned= weather_data_pd.fillna(0)
#print out df to see if it replace visible NaN values and it did
print ("Question 8: replace nans with 0:",weather_data_cleaned)

# %%
#Question 9 How many observations were made in Feburary? Int
#take month of february and see length of values...here I used the data frame where all null values have been replaced with 0
feb_observ=len(weather_data_cleaned[weather_data_cleaned["month"] == 2.0])
print("Question 9: number of observations in February:",feb_observ)

# %%
#Question 10 What was the mean for humidity in February? Float

#look at constraints of february and humidity and then find mean

mean_hum_feb=weather_data_cleaned.loc[weather_data_cleaned["month"]==2.0,"humid"].mean()
print("Question 10:Mean humidity in February:",mean_hum_feb)

# %%
#Question 11 What was the std for humidity in February? Float
std_hum_feb=weather_data_cleaned.loc[weather_data_cleaned["month"]==2.0,"humid"].std()
print("Question #11: Std for humidity in February:",std_hum_feb)


