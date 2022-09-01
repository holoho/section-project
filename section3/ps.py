import psycopg2
from psycopg2 import Error
import pandas as pd
import psycopg2 as ps
from sqlalchemy import create_engine as ce


# pgconn = ps.connect(host = 'localhost',
#port = '5432', database = 'pp',
#user = 'postgres', password = '1234')

# driver://username:password@server/database
tt = pd.read_csv("section3/tt.csv")
tt.columns = ['Country','year','Population','CO2mt','CO2gask','CO2liquidk','CO2solidk','Methane','NO','HRC','PFC','SF6','Total','GlobTemp','Wheat','Corn','Soybean']
pg_engine = ce("postgresql://postgres:1234@localhost:5432/postgres")

tt.to_sql('tt', con=pg_engine, if_exists='replace', index=False)

#try:
#    
#    connection = psycopg2.connect(user="postgres",
#                                  password="1234",
#                                  host="localhost",
#                                  port="5432",
#                                  database="postgres")
#
    
#    cursor = connection.cursor()
#    
#    create_table_query =  """ CREATE TABLE CO2 ( 
#                      Country  VARCHAR NULL,
#                      year INTEGER NULL,
#                      Population FLOAT NULL,	
#                      CO2mt	FLOAT NULL,
#                      CO2gask	FLOAT NULL,
#                      CO2liquidk	FLOAT NULL,
#                      CO2solidk	FLOAT NULL,
#                      Methane	FLOAT NULL,
#                      NO FLOAT NULL,	
#                      HFC	FLOAT NULL,
#                      PFC	FLOAT NULL,
#                      SF6	FLOAT NULL,
#                      Total	FLOAT NULL,
#                      GlobTemp FLOAT NULL,	
#                      Wheat FLOAT NULL,	
#                      Corn FLOAT NULL,
#                      Soybean FLOAT NULL)"""
#  
    
#    cursor.execute(create_table_query)
#    connection.commit()
#    print("Table created successfully in PostgreSQL ")

#except (Exception, Error) as error:
#    print("Error while connecting to PostgreSQL", error)
#finally:
#    if connection:
#        cursor.close()
#        connection.close()
#        print("PostgreSQL connection is closed")
        
        
        
