def store_provisioned_resources(col):
    cursor = col.find({})
    for document in cursor:
        from authentication_access_token import gettoken
        access_token = gettoken(document['credentials']['tenant_id'],document['credentials']['client_id'],document['credentials']['client_secret'])
        from fetch_resources import fetch_rg_details
        all_resource_groups = fetch_rg_details(access_token)
        res_doc = {"Resource Groups":all_resource_groups}
        
        filter_criteria = {"_id": document["_id"]}
        update_operation = {
        "$set": {
            "Provisioned Resources": res_doc, 
        }
    }
        
        print("\n")
        result = col.update_one(filter_criteria, update_operation)