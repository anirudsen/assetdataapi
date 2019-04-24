import pyodbc
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
    cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = dbo.Device_Data ORDER BY ORDINAL_POSITION;") 
    row = cursor.fetchall()
    return row


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
    row = cursor.fetchall()
    #while 
    return row[0]