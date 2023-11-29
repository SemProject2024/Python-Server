def main(): 
    import pymongo
    import Encrypt_varibles
    mongodb_uri = "mongodb+srv://Semproject2024:Semproject2024@test-db.dm1ghqi.mongodb.net/"
    client = pymongo.MongoClient(mongodb_uri)
    db = client.get_database('User')
    collection = db.get_collection("Details")
    import encryption


    subscription_id = encryption.encrypt(Encrypt_varibles.subscription_id,"72a851c4-6ce9-4328-902a-1b4f3e431554")
    tenant_id = encryption.encrypt(Encrypt_varibles.tenant_id,"f2a009da-b491-4dbb-94e8-5809162549cd")
    client_id = encryption.encrypt(Encrypt_varibles.client_id,"9e46e6ee-df6f-438d-bf40-6dbfa737777c")
    client_secret = encryption.encrypt(Encrypt_varibles.client_secret,"szF8Q~xjzDW2_IFD0yyaOZE_SjkvX8TysLW86c8T")

    document = {
        "credentials":{
        "subscription_id": subscription_id,
        "tenant_id":tenant_id,
        "client_id":client_id,
        "client_secret":client_secret,
        
    },
        "Provisioned Resources" : {},
        
    }
    #result = collection.insert_one(document)
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
    return res


def registerUser(col,data_dic):
    from random import randint
    from encryption import encrypt,decrypt
    import Encrypt_varibles
    encrypted_password = encrypt(Encrypt_varibles.password,data_dic['password'])
    data_dic['password'] = encrypted_password
    data_dic['userID'] = randint(100,10000)
    col.insert_one(data_dic)
    
def verifyUser(collection,data_dic):
    from encryption import decrypt
    import Encrypt_varibles
    cursor = collection.find({})
    
    for document in cursor:
        if 'emailAddress' in document.keys():
            if document['emailAddress'] == data_dic['emailAddress']:
                print(document['emailAddress'])
                if(data_dic['password'] == decrypt(Encrypt_varibles.password,document['password'])):
                    return document['userID']
    
    return None


def addCredentials(collection,data_dic):
    from encryption import encrypt
    import Encrypt_varibles
    update_doc = {"subscriptionID":encrypt(Encrypt_varibles.subscription_id,data_dic['subscriptionId']),
                  "tenantID":encrypt(Encrypt_varibles.tenant_id,data_dic['tenantId']),
                  "clientID":encrypt(Encrypt_varibles.client_id,data_dic['clientId']),
                  "clientSecret":encrypt(Encrypt_varibles.client_secret,data_dic['clientSecret'])}
    filter_criteria = {'userID':int(data_dic['userId'])}
    update_operation = {
        "$set": {
            "credentials": update_doc, 
        }
    }
        
    result = collection.update_one(filter_criteria, update_operation)
    return True

def fetchCredentials(collection,data_dic):
    from encryption import decrypt
    import Encrypt_varibles
    query = {'userID':int(data_dic['userId'])}
    mydoc =collection.find(query)
    document = mydoc[0]
    creds = document['credentials']
    subscriptionId = decrypt(Encrypt_varibles.subscription_id,creds['subscriptionID'])
    tenantId = decrypt(Encrypt_varibles.tenant_id,creds['tenantID'])
    clientId = decrypt(Encrypt_varibles.client_id,creds['clientID'])
    clientSecret = decrypt(Encrypt_varibles.client_secret,creds['clientSecret'])
    return subscriptionId,tenantId,clientId,clientSecret
    
    
def fetchEncryptedCredentials(collection,data_dic):
    from encryption import decrypt
    import Encrypt_varibles
    query = {'userID':int(data_dic['userId'])}
    mydoc =collection.find(query)
    document = mydoc[0]
    creds = document['credentials']
    subscriptionId = decrypt(Encrypt_varibles.subscription_id,creds['subscriptionID'])
    tenantId = decrypt(Encrypt_varibles.tenant_id,creds['tenantID'])
    clientId = decrypt(Encrypt_varibles.client_id,creds['clientID'])
    clientSecret = decrypt(Encrypt_varibles.client_secret,creds['clientSecret'])
    return str(creds['subscriptionID']),str(creds['tenantID']),str(creds['clientID']),str(creds['clientSecret'])
