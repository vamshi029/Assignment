import pysftp
import os
import sqlite3
import pandas as pd

myHostname = "your_server_ip_address.com"
myUsername = "username"
myPassword = "password"

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
    print "Connection succesfully stablished"
    
    # Switch to a remote directory where csv files are present
    sftp.cd('/folder_on_remote_server')

    # Obtain structure of the remote directory '/folder_on_remote_server'
    directory_structure = sftp.listdir_attr()

    localFilePath = './my_directory'
    remoteFilePath = '/folder_on_remote_server'
    for attr in directory_structure:
        if attr.filename[:5] == 'Pref-' and attr.filename[-4:] =='.csv:
            print attr.filename
            sftp.get(remoteFilePath/attr.filename, localFilePath)
            sftp.remove(remoteFilePath/attr.filename)


#listing items in my current directory - 'my_directory' and pushing it to a dataframe df
items=os.listdir('my_directory/')
for item in items:
    
    # picking the files which have Pref prefix and .csv extension
    if item.name[:5] == 'Pref-' and item.name[-4: ] =='.csv':
        
        #reading the csv file into a dataframe df
        df = pd.read_csv(item)


#establishing connection object 
conn = sqlite3.connect('SOLUTION.db')
c = conn.cursor()

#creating a Table with name DB_TABLE with the mentioned columns
c.execute('CREATE TABLE DB_TABLE (Result Time,Granularity Period,Object Name,Cell ID,CallAttemps)')  



#pushing the dataframe - df to table DB_TABLE
df.to_sql('DB_TABLE', conn, if_exists='replace', index = False)

#closing sql connection
conn.commit()
