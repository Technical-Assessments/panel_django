import sys
sys.path.append('../FROGTEK_TECHNICAL_ASSESSMENT')
import pandas as pd
from .data_extraction import soup, all_months_links_df


def time_lapse(seconds):
    seconds_in_day = 60 * 60 * 24
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60
    
    days = seconds // seconds_in_day
    hours = (seconds - (days * seconds_in_day)) // seconds_in_hour
    minutes = (seconds - (days * seconds_in_day) - (hours * seconds_in_hour)) // seconds_in_minute
    
    return f"{days} days, {hours} hours, {minutes} minutes"


def csv_to_df(year, taxi_color ,*month):
    
    soup(year) ###
    
    print(f"list of months requested: {month}")
    links_table = all_months_links_df(year, *month)
    links_table = links_table[links_table['description'].str.contains(taxi_color)][['month','links']]
    print(links_table['links'])
    
    final_df = pd.DataFrame()
    
    print("Starting parsing process:")
    for index, elem in enumerate(links_table['links']):
        print(f"Parsing csv {elem}")
        #m =  month[index]
        df = pd.read_csv(elem)
        df.insert(1, 'month', month[index])
        #df['month'] = m
        final_df = final_df.append(df, ignore_index=True)
        print("Parsing completed")
    
    type_object = final_df.select_dtypes(include='object').columns.to_list()
    type_object.remove('store_and_fwd_flag')
    type_object.remove('month')
    
    for elem in type_object:
        final_df[f"{elem}"] = pd.to_datetime(final_df[f"{elem}"], yearfirst=True, format="%Y/%m/%d %H:%M:%S")
    
    final_df['month'] = pd.to_datetime(final_df['month'], format="%B").dt.month  
    
    trip_duration_seconds = (final_df['tpep_dropoff_datetime'] - final_df['tpep_pickup_datetime']).astype('timedelta64[s]').astype('int')
    trip_duration = trip_duration_seconds.apply(time_lapse)
    
    final_df.insert(4, 'trip_duration_seconds', trip_duration_seconds)
    final_df.insert(5, 'trip_duration', trip_duration)
    
    return final_df