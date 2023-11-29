from flask import Flask , request,jsonify
import json
from flask_cors import CORS
from bson import json_util
app = Flask(__name__) 
CORS(app)
import pymongo
import Encrypt_varibles
mongodb_uri = "mongodb+srv://Semproject2024:Semproject2024@test-db.dm1ghqi.mongodb.net/"
client = pymongo.MongoClient(mongodb_uri)
db = client.get_database('User')
collection = db.get_collection("Details")

import encryption
@app.route("/",methods=["GET","POST"]) 
def hello(): 
    cursor = collection.find({})
    res = {"Result":{}}
    for document in cursor:
        for key,value in document['credentials'].items():
            print(key,encryption.decrypt(key,value))
        print("\n")
        
    from db_operations import store_provisioned_resources
    store_provisioned_resources(collection)
    
    cursor = collection.find({})
    k = 0
    for document in cursor:
        res["Result"][k] = (document["Provisioned Resources"])
        k+=1
    print(res)
    #res = {"message":"hi"}
    print(json.dumps(res))
    return res


@app.route("/signIn",methods=["POST"]) 
def process(): 
    data = request.get_json()
    from mongodb import verifyUser
    userId = verifyUser(collection=collection,data_dic=data)
    if userId is not None:
        return {"userId":userId}
    else:
        return {"userId":"None"}


@app.route('/registerUser',methods=['POST']) 
def registerUser(): 
    data = request.get_json() # retrieve the data sent from JavaScript
    from mongodb import registerUser
    registerUser(collection,data_dic=data)
    return {"userID":data["userID"]}

@app.route('/addCredentials',methods=['POST']) 
def addCredentials(): 
    data = request.get_json() # retrieve the data sent from JavaScript
    from mongodb import addCredentials
    addCredentials(collection,data_dic=data)
    return {"Saved":"Success"}

@app.route('/fetchCredentials',methods=['POST']) 
def fetchCredentials(): 
    data = request.get_json() # retrieve the data sent from JavaScript
    from mongodb import fetchCredentials
    subscriptionId,tenantId,clientId,clientSecret = fetchCredentials(collection,data_dic=data)
    return {"subscriptionId":subscriptionId,
            "tenantId":tenantId,
            "clientId":clientId,
            "clientSecret":clientSecret}

@app.route('/fetchEncryptedCredentials',methods=['POST']) 
def fetchEncryptedCredentials(): 
    data = request.get_json() # retrieve the data sent from JavaScript
    from mongodb import fetchEncryptedCredentials
    subscriptionId,tenantId,clientId,clientSecret = fetchEncryptedCredentials(collection,data_dic=data)
    return {"subscriptionId":subscriptionId,
            "tenantId":tenantId,
            "clientId":clientId,
            "clientSecret":clientSecret}
    
    
@app.route('/fetchDecryptedCredentials',methods=['POST']) 
def fetchDecryptedCredentials(): 
    data = request.get_json() # retrieve the data sent from JavaScript
    from mongodb import fetchCredentials
    subscriptionId,tenantId,clientId,clientSecret = fetchCredentials(collection,data_dic=data)
    return {"subscriptionId":subscriptionId,
            "tenantId":tenantId,
            "clientId":clientId,
            "clientSecret":clientSecret}


@app.route('/fetchSubscriptionDetails',methods=['POST']) 
def fetchSubscriptionDetails(): 
    data = request.get_json() # retrieve the data sent from JavaScript
    from mongodb import fetchCredentials
    subscriptionId,tenantId,clientId,clientSecret = fetchCredentials(collection,data_dic=data)
    from fetch_resources import gettoken
    token = gettoken(tenant_id=tenantId,client_id=clientId,client_secret=clientSecret)
    from fetch_resources import fetch_all_subscriptions_details
    subscriptions = fetch_all_subscriptions_details(token=token)
    return {"Subscriptions":subscriptions}

@app.route('/fetchResourceGroupDetails',methods=['POST']) 
def fetchResourceGroupDetails(): 
    data = request.get_json() # retrieve the data sent from JavaScript
    print(data)
    from mongodb import fetchCredentials
    subscriptionId,tenantId,clientId,clientSecret = fetchCredentials(collection,data_dic=data)
    from fetch_resources import gettoken
    token = gettoken(tenant_id=tenantId,client_id=clientId,client_secret=clientSecret)
    from fetch_resources import fetch_rg_details
    resourceGroups = fetch_rg_details(token=token,subId=subscriptionId)
    return {"ResourceGroups":resourceGroups}

@app.route('/fetchAllVmDetails',methods=['POST']) 
def fetchAllVmDetails(): 
    data = request.get_json() # retrieve the data sent from JavaScript
    print(data)
    from mongodb import fetchCredentials
    subscriptionId,tenantId,clientId,clientSecret = fetchCredentials(collection,data_dic=data)
    from fetch_resources import gettoken
    token = gettoken(tenant_id=tenantId,client_id=clientId,client_secret=clientSecret)
    from fetch_resources import fetch_all_vm_details
    VirtualMachines = fetch_all_vm_details(token=token,subId=subscriptionId)
    return {"Virtual Machines":VirtualMachines}
@app.route('/fetchVmDetails',methods=['POST']) 
def fetchVmDetails(): 
    data = request.get_json() # retrieve the data sent from JavaScript
    print(data)
    from mongodb import fetchCredentials
    subscriptionId,tenantId,clientId,clientSecret = fetchCredentials(collection,data_dic=data)
    from fetch_resources import gettoken
    token = gettoken(tenant_id=tenantId,client_id=clientId,client_secret=clientSecret)
    from fetch_resources import fetch_vm_details
    VirtualMachineDetails = fetch_vm_details(token=token,subId=subscriptionId,vmName=data['vmName'],rg=data['rg'])
    print(data)
    return {"Virtual Machines":VirtualMachineDetails}
@app.route('/fetchIpAddress',methods=['POST']) 
def fetchIpAddress(): 
    data = request.get_json() # retrieve the data sent from JavaScript
    print(data)
    from mongodb import fetchCredentials
    subscriptionId,tenantId,clientId,clientSecret = fetchCredentials(collection,data_dic=data)
    from fetch_resources import gettoken
    token = gettoken(tenant_id=tenantId,client_id=clientId,client_secret=clientSecret)
    from fetch_resources import fetch_ip_address_details
    IpAddress = fetch_ip_address_details(token=token,subId=subscriptionId,rg=data['rg'],ipName=data['ipName'])
    print(data)
    return {"IP address":IpAddress}





	# process the data using Python code
# @app.route('/process', methods=['POST']) 
# def process(): 
#     data = request.get_json() # retrieve the data sent from JavaScript
#     print(data)
# 	# process the data using Python code 
#     result = int(data['value']) * 2
#     return jsonify(result=result,message=result*2) # return the result to JavaScript 

if __name__ == '__main__': 
	app.run(debug=True) 