import pyodbc as db
from flask import Flask, request,  jsonify
from flask_restful import Api, marshal
from flask_cors import CORS
app = Flask(__name__)


@app.route('/assets')
def getwelcomeMsg():
    return 'Asset API'



@app.route('/asset/<asset_id>')
def getAssetByID(asset_id=None):
    server = 'mdpsqldbserverdev.database.windows.net'
    database = 'mdpappdb'
    username = 'mdpadmin'
    password = 'Robo#2010'
    port = 1433
    driver = '{ODBC Driver 13 for SQL Server}'
    connectionstring = f'DRIVER={driver};SERVER={server};PORT={port};DATABASE={database};UID={username};PWD={password}'
    print(connectionstring)
    connection = db.connect(connectionstring)  
    print(connection) 
    cursor=connection.cursor()
    print (cursor)
    cursor.execute(
        'SELECT Id,FullName, UserName, Email, Password, Avatar FROM [TechnologyApp].[Users]')
    row = cursor.fetchone()

    assets = []

    while row:
        asset = {
            'Id': row[0],
            'FullName': row[1],
            'UserName': row[2],
            'Email': row[3],
            'Password': row[4],
            'Avatar': row[5]
        }
        assets.append(asset)
        row = cursor.fetchone()

    # print(f'Value: {user_id}')
    # print(request.args.get('username'))
    return jsonify(assets)