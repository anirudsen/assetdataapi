import pyodbc
import collections
import json
import datetime
import time
import calendar
from flask import Flask, request,  jsonify


app = Flask(__name__)

@app.route('/')
def getwelcomeMsg():
    return 'Asset API with /'



@app.route('/v1/iSolveCommandAsset',methods=['POST'])
def getData():

    '''
    mssql_host = 'tcp:mdpsqldbserverdev.database.windows.net'
    mssql_db = 'mdpappdb'
    mssql_user = 'mdpadmin'
    mssql_pwd = 'Robo#2010'
    mssql_port = 1433 
    mssql_driver = 'ODBC Driver 17 for SQL Server'
    database_server_name = "mdpsqldbserverdev"
    dns = 'testodbc'
    '''
    mssql_host = 'tcp:mdpsqldbserverqc.database.windows.net'
    mssql_db = 'mdp'
    mssql_user = 'appadmin'
    mssql_pwd = 'Robo#2010'
    mssql_port = 1433 
    mssql_driver = 'ODBC Driver 17 for SQL Server'
    database_server_name = "mdpsqldbserverdev"
    dns = 'testodbc'
    #-----------------------------------------------------
    content=request.get_json()
    tablename=content['tableName']
    columnname=content['columnName']
    filtercondition=content['Full']
    incrementaldate=content['incrementalDate']
    offset=content['offSet']
    limit=content['Limit']
    #------------------------------------------------------------------------- Date
    
    if incrementaldate !=' ':
        data_pre = incrementaldate.strip().split(',')
        stDate = data_pre[0].replace("\"", "")
        try:
            dat_time = datetime.datetime.strptime(stDate,'%Y-%m-%d %H:%M:%S.%f')
        except:
            stDate = stDate + ".4"
        dat_time = datetime.datetime.strptime(stDate,'%Y-%m-%d %H:%M:%S.%f')

    mic_sec = dat_time.microsecond
    timcon = calendar.timegm(dat_time.timetuple())*1000000 + mic_sec
    strDate = "\"" + stDate + "\""
    
    #-------------------------------------------------------------------------- Date end
    #-----------------------------------------------------
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+mssql_host+';DATABASE='+mssql_db+';UID='+mssql_user+';PWD='+ mssql_pwd+';Trusted_connection=no')
    cursor = cnxn.cursor()
    sql_query = " "
    if filtercondition == '*'  and incrementaldate != ' ' :
        sql_query = "SELECT * FROM (SELECT *, Row_number() OVER (ORDER BY Asset_Identifier DESC) AS rownum FROM [dbo].iSolve_Asset_Stg)tb1 WHERE rownum between " + offset + "AND " + limit + " AND Last_Update_Date >='"+strDate+"';"
        print(sql_query)
        #sql_query = "SELECT * FROM "+ "dbo.iSolve_Asset_Stg" +" WHERE Last_Update_Date >='" + strDate + "';"
    if filtercondition == '*'  and incrementaldate == ' ' :
        sql_query = "SELECT * FROM (SELECT * , Row_number() OVER (ORDER BY Asset_Identifier DESC) AS rownum FROM [dbo].iSolve_Asset_Stg)tbl WHERE rownum between " + offset + "AND " + limit +";"
        #sql_query = "SELECT * from "+"dbo.iSolve_Asset_Stg ORDER BY ASSET_Identifier" +"OFFSET "+ offset + "FETCH NEXT "+limit+" ROWS ONLY"+";"

    '''
    if filtercondition == '*' and columnname == ' ' and incrementaldate == ' ' :
    		sql_query = "SELECT * from "+tablename +";"

    if filtercondition == ' ' and columnname != ' ' and incrementaldate == ' ':
	    sql_query = "SELECT "+ columnname + " "+"FROM "+tablename +";"
		
    if filtercondition == '*' and columnname == ' ' and incrementaldate !=' ' :
		#"SELECT * FROM dbo.Device_Data WHERE Last_Update_Date ='" + dateval + "';"
	    sql_query = "SELECT * FROM "+ tablename +" WHERE Last_Update_Date >='" + incrementaldate + "';"
		
    if filtercondition == ' ' and columnname != ' ' and incrementaldate !=' ':
	    sql_query = "SELECT "+ columnname + "FROM "+ tablename +" WHERE Last_Update_Date >='" + incrementaldate + "';"

    '''
    cursor.execute(sql_query) 
    #rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    #rec = [ dict(rec) for rec in rows ]

#j = json.dumps(objects_list,myconverter)
    return jsonify(results)


@app.route('/incremental')
def getAssetByAssets():
    mssql_host = 'tcp:mdpsqldbserverdev.database.windows.net'
    mssql_db = 'mdpappdb'
    mssql_user = 'mdpadmin'
    mssql_pwd = 'Robo#2010'
    mssql_port = 1433 
    mssql_driver = 'ODBC Driver 17 for SQL Server'
    database_server_name = "mdpsqldbserverdev"
    dns = 'testodbc'
    dateval = request.get_.args.get('date', '')
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+mssql_host+';DATABASE='+mssql_db+';UID='+mssql_user+';PWD='+ mssql_pwd)
    cursor = cnxn.cursor()
    date_time_obj = datetime.datetime.strptime(dateval, '%Y-%m-%d')
    sql_query =  "SELECT * FROM dbo.Device_Data WHERE Last_Update_Date ='" + dateval + "';"
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d['DerviceDataUI'] = row.Device_Data_Feed_Unique_Identifier
        d['AssetID'] = row.Asset_Identifier
        d['PublishID'] = row.Publisher_Identifier
        d['LastUpdatedDate'] = row.Last_Update_Date
        objects_list.append(d)
     #query = "SELECT personal || ' ' || family FROM Person WHERE id='" + person_id + "';"

    return jsonify(objects_list)
    