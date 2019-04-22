import os
import pyodbc
from flask import Flask, request,  jsonify
from flask_restful import Api, marshal
from flask_cors import CORS
app = Flask(__name__)


@app.route('/assets')
def getwelcomeMsg():
    return 'Asset API'



@app.route('/asset01')
def getAssetByID():
    mssql_host = 'mdpsqldbserverdev.database.windows.net'
    mssql_db = 'mdpappdb'
    mssql_user = 'mdpadmin'
    mssql_pwd = 'Robo#2010'
    mssql_port = 1433 
    mssql_driver = 'ODBC Driver 17 for SQL Server'
    database_server_name = 'mdpsqldbserverdev'
    dns = 'testodbc'
     #/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.2.so.0.1
    # connectionstring = 'DRIVER={mssql_driver};SERVER={mssql_host};PORT={mssql_port};DATABASE={mssql_db};UID={mssql_user};PWD={mssql_pwd}'
    # connectionstring = f'DRIVER={driver};SERVER={server};PORT={port};DATABASE={database};UID={username};PWD={password}'
     #connectionstring=os.environ['SQLAZURECONNSTR_mdpappdb'] #os.getenv('mdpappdb')
     # mssql+pymssql://dbadmin@nedomkulltest:password@nedomkulltest.database.windows.net:1433/exampledb
    # connectionstring=os.environ['SQLAZURECONNSTR_mdpappdb']
    #connectionstring='mssql+pymssql://mdpadmin:Robo#2010@mdpsqldbserverdev.database.windows.net:1433/mdpappdb'
    
    connection_string = 'DNS+=+{0}+;+UID+={1}+;PWD+={2}+DATABASE+={3}+;'.format(
        dns,  mssql_user, mssql_pwd, mssql_db)
    # connectionstring=os.getenv('SQLAZURECONNSTR_mdppip freappdb')
    #print('connectionstring')
    #print(os.getenv('SQLAZURECONNSTR_sqldbcon'))
    
    pyodbc.connect(connection_string)
    #pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=mdpsqldbserverdev.database.windows.net;DATABASE=mdpappdb;UID=mdpadmin;PWD=Robo#2010')
    from sqlalchemy import create_engine
    engine = create_engine(connection_string) 

    
    #conn = pymssql.connect(
    #server="mdpsqldbserverdev.database.windows.net",
    #port=1433,
    #user= "mdpadmin",
    #password="Robo#2010",
    #database="mdpappdb")
    #cursor = conn.cursor()
    #cursor.execute(sql_query)
    #sql_query ='SELECT * FROM Asset'
    # results = engine.execute(sql_query)
    #for r in results:
    # print(r)
   # print('connection') 
   # print(connection) 
    #cursor=connection.cursor()
    #print ('cursor')
   # print (cursor)
    

    # print(f'Value: {user_id}')
    # print(request.args.get('username'))
    return "results"