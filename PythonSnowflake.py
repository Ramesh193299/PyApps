#This is first Python Prgram 
#This is first Python Prgram 
#This is first Python Prgram 
import snowflake.connector
import pandas as pd
conn = snowflake.connector.connect(user='ramesh1980', password='Prannu@2009', account='swb55287.us-east-1')
cs = conn.cursor()
try:
   cs.execute("Use Role ACCOUNTADMIN")
   cs.execute("Use Warehouse COMPUTE_WH")
   cs.execute("Use SNOWFLAKE_SAMPLE_DATA")
   cs.execute("Use Schema TPCDS_SF100TCL")
   data = cs.execute("select * from CALL_CENTER")
   dfCallCenter = pd.DataFrame.from_records(iter(data), columns=[x[0] for x in data.description])
   print(dfCallCenter.tail(1))
finally:
   cs.close()
   conn.close()