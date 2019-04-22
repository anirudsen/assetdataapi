import os
from flask import Flask, request,  jsonify
from flask_restful import Api, marshal
from flask_cors import CORS
app = Flask(__name__)


@app.route('/assets')
def getwelcomeMsg():
    return 'Asset API'



@app.route('/asset')
def getAssetByID():
    server = 'mdpsqldbserverdev.database.windows.net'
    database = 'mdpappdb'
    username = 'mdpadmin'
    password = 'Robo#2010'
    port = 1433 
    driver = '{ODBC Driver 17 for SQL Server}'
    # connectionstring = f'DRIVER={driver};SERVER={server};PORT={port};DATABASE={database};UID={username};PWD={password}'
    # connectionstring = f'DRIVER={driver};SERVER={server};PORT={port};DATABASE={database};UID={username};PWD={password}'
     #connectionstring=os.environ['SQLAZURECONNSTR_mdpappdb'] #os.getenv('mdpappdb')
     # mssql+pymssql://dbadmin@nedomkulltest:password@nedomkulltest.database.windows.net:1433/exampledb
    # connectionstring=os.environ['SQLAZURECONNSTR_mdpappdb']
    connectionstring='mssql+pymssql://mdpadmin:Robo#2010@mdpsqldbserverdev.database.windows.net:1433/mdpappdb'
    # connectionstring=os.getenv('SQLAZURECONNSTR_mdppip freappdb')
    #print('connectionstring')
    #print(os.getenv('SQLAZURECONNSTR_sqldbcon'))
    from sqlalchemy import create_engine
    engine = create_engine(connectionstring) 
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
    return 'hello'