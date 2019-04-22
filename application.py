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
     
    # import os
    # connectionstring=os.getenv("SQLAZURECONNSTR_assetdbconn")
     # mssql+pymssql://dbadmin@nedomkulltest:password@nedomkulltest.database.windows.net:1433/exampledb
    # connString=os.environ['SQLAZURECONNSTR_assetdbconn']
    # connectionstring=os.environ['SQLAZURECONNSTR_assetdbconn']

    #connectionstring='mssql+pymssql://mdpadmin:Robo#2010@mdpsqldbserverdev.database.windows.net:1433/mdpappdb'
    
    
    # connectionstring=os.getenv('SQLAZURECONNSTR_mdppip freappdb')
    #print('connectionstring')
    #print(os.getenv('SQLAZURECONNSTR_sqldbcon'))
    
    pyodbc.connect('Data Source=tcp:mdpsqldbserverdev.database.windows.net,1433;Initial Catalog=mdpappdb;User ID=mdpadmin;Password=Robo#2010')
        
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