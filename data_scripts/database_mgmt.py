# This file is for storing the scraped DF into a PostgreSQL db. For sharing purposes the db tech used is sqlite3

import sys
#DataBase tools
import psycopg2
import psycopg2.extras as extras
import sqlite3
import pandas as pd

param_dic = {
    "host"      : "127.0.0.1",
    "database"  : "taxis",
    "user"      : "snowman",
    "password"  : "snowball"
}


def create_data_base():

    #establishing the connection
    conn = psycopg2.connect(
    database="postgres", user='snowman', password='snowball', host='127.0.0.1', port= '5432'
    )

    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Preparing query to create a database
    sql = '''CREATE database taxis''';

    #Creating a database
    cursor.execute(sql)
    print("Database created successfully !")

    #Closing the connection
    conn.close()



def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print('Connection succesful')
    
    return conn


def creating_table(table_name: str):
    
    conn = connect(param_dic)
    cursor = conn.cursor()
    
    sql =f'''CREATE TABLE {table_name}(
       VendorID float,
       month int,
       tpep_pickup_datetime timestamp,
       tpep_dropoff_datetime timestamp,
       trip_duration_seconds int,
       trip_duration varchar,
       passenger_count float,
       trip_distance float,
       RatecodeID float,
       store_and_fwd_flag varchar,
       PULocationID float,
       DOLocationID float,
       payment_type float,
       fare_amount float,
       extra float,
       mta_tax float,
       tip_amount float,
       tolls_amount float,
       improvement_surcharge float,
       total_amount float,
       congestion_surcharge float
    );'''
    
    print(f"Creating table {table_name}")
    cursor.execute(sql)
    print("Table created")
    conn.commit()
    #cursor.close()
    #print("Cursor object closed")
    conn.rollback()
    #print(f"Closing {conn.info.dbname} database conection")
    #conn.close()
    #print("Conection closed.")


# SQLITE3
def sqlite_insert_df(db_name: str, table_name: str, df: pd.DataFrame):

    print(f"Creating Sqlite3 DB '{db_name}'...")
    conn = sqlite3.connect(f"./database/{db_name}.db")
    print("DB created successfully!")

    print(f"Inserting DF of size {df.size} into DB '{db_name}' and table '{table_name}'.This operation can take a few minutes...")
    df.to_sql(f'{table_name}', conn, if_exists='replace', index=False)
    print("DataBase insertion finished successfully!")

