import datetime as dt
import pandas as pd
import mysql.connector
stockdata = input('\n\t\t\t\t****Select any Company Name****\n')
ts1 = str(int(dt.datetime(2023,2,1).timestamp()))
ts2 = str(int(dt.datetime(2023,2,8).timestamp()))
interval = input('Enter the interval from 1d to 1mo :\n\t daywise = 1d\n\t weekwise = 1wk\n\t monthwise = 1mo\n')

#interval = '1d' , '1wk' ,'1mo'
events = input('Want to Print a Historical data or Dividened ? \n')

#events = 'history','split'
Stockurl = 'https://finance.yahoo.com/quote/'+stockdata+'/history?p='+stockdata+''

print('\n\nTo view it Click here :')
print(Stockurl)

Stock_downurl = 'https://query1.finance.yahoo.com/v7/finance/download/' + stockdata + '?period1='+ ts1 + '&period2=' + ts2 + '&interval=' + interval + '&events'+ events
company_data = pd.read_csv(Stock_downurl)
print(company_data)

print('\n\nThe Download link is here :')
print(Stock_downurl)

print('\n/////Hence you Can change the "date interval" at line no.4 and 5 in code and try/////\n')


# Connect to the database
cnx = mysql.connector.connect(
  name ="Company_name",
  open ="open Price",
  close ="closed price",
  database="database_name"
)

# Create the table (if it doesn't already exist)
cursor = cnx.cursor()
table_create_query = """
CREATE TABLE IF NOT EXISTS online_data (
  id INT AUTO_INCREMENT PRIMARY KEY,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  data VARCHAR(255)
);
"""
cursor.execute(table_create_query)
cnx.commit()

# Insert new data into the table
insert_query = """
INSERT INTO online_data (data)
VALUES (%s)
"""
data = "new data"
cursor.execute(insert_query, (data,))
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()
