import pyodbc
import collections
import json
import datetime
from flask import Flask, request,  jsonify


app = Flask(__name__)

@app.route('/')
def getwelcomeMsg():
    return 'Asset API with /'



@app.route('/assets')
def getAssetByID():
    mssql_host = 'tcp:mdpsqldbserverdev.database.windows.net'
    mssql_db = 'mdpappdb'
    mssql_user = 'mdpadmin'
    mssql_pwd = 'Robo#2010'
    mssql_port = 1433 
    mssql_driver = 'ODBC Driver 17 for SQL Server'
    database_server_name = "mdpsqldbserverdev"
    dns = 'testodbc'

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+mssql_host+';DATABASE='+mssql_db+';UID='+mssql_user+';PWD='+ mssql_pwd)
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM dbo.Device_Data;") 
    rows = cursor.fetchall()
    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d['DerviceDataUI'] = row.Device_Data_Feed_Unique_Identifier
        d['AssetID'] = row.Asset_Identifier
        d['PublishID'] = row.Publisher_Identifier
        d['LastUpdatedDate'] = myconverter(row.Last_Update_Date)
        objects_list.append(d)

    j = json.dumps(objects_list)
    return j

def myconverter(o):
        if isinstance(o, datetime.datetime):
            return o.__str__()

@app.route('/asset01')
def getAssetByAssets():
    mssql_host = 'tcp:mdpsqldbserverdev.database.windows.net'
    mssql_db = 'mdpappdb'
    mssql_user = 'mdpadmin'
    mssql_pwd = 'Robo#2010'
    mssql_port = 1433 
    mssql_driver = 'ODBC Driver 17 for SQL Server'
    database_server_name = "mdpsqldbserverdev"
    dns = 'testodbc'

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+mssql_host+';DATABASE='+mssql_db+';UID='+mssql_user+';PWD='+ mssql_pwd)
    cursor = cnxn.cursor()
    cursor.execute("SELECT @@version;") 
    row = cursor.fetchone()
    #while 
    return row[0]