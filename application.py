import pyodbc 
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
    connectionstring=os.environ['mdpappdb']
    # connectionstring=os.getenv('SQLAZURECONNSTR_mdpappdb')
    print('connectionstring')
    #print(os.getenv('SQLAZURECONNSTR_sqldbcon'))
    connection = pyodbc.connect(connectionstring)  
    print('connection') 
    print(connection) 
    cursor=connection.cursor()
    print ('cursor')
    print (cursor)
    

    # print(f'Value: {user_id}')
    # print(request.args.get('username'))
    return 'good db connected'