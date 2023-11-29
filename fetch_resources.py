import requests,json,encryption,Encrypt_varibles



def fetch_all_subscriptions_details(token):
    auth = 'Bearer '+token
    url_for_all_resources = 'https://management.azure.com/subscriptions?api-version=2021-04-01'
    headers = {
    'Authorization':auth
    }
    response = requests.get(url_for_all_resources,headers=headers )
    if response.status_code == 200:
        print(response.text)
        print("\n")
    else:
        print(f"Request failed with status code {response.status_code}")
    
    data_dict = json.loads(response.text)
    for item in data_dict["value"]:
        name = item.get("subscriptionId")
        print(f"Subscription ID: {name}")
    return data_dict



def fetch_all_resources_details(token):
    auth = 'Bearer '+token
    url_for_all_resources = 'https://management.azure.com/subscriptions/72a851c4-6ce9-4328-902a-1b4f3e431554/resources?api-version=2021-04-01'
    headers = {
    'Authorization':auth
    }
    response = requests.get(url_for_all_resources,headers=headers )
    if response.status_code == 200:
        print(response.text)
        print("\n")
    else:
        print(f"Request failed with status code {response.status_code}")
    
    data_dict = json.loads(response.text)
    for item in data_dict["value"]:
        name = item.get("name")
        item_type = item.get("type")
        location = item.get("location")
        print(f"Name: {name}, Type: {item_type}, Location: {location}")
    return data_dict



def fetch_rg_details(token,subId):
    auth = 'Bearer '+token
    url_for_all_resources = 'https://management.azure.com/subscriptions/'+subId+'/resourcegroups?api-version=2021-04-01'
    headers = {
    'Authorization':auth
    }
    response = requests.get(url_for_all_resources,headers=headers )
    if response.status_code == 200:
        print(response.text)
        print("\n")
    else:
        print(f"Request failed with status code {response.status_code}")
    data_dict = json.loads(response.text)
    rg_dict = {}
    for item in data_dict["value"]:
        name = item.get("name")
        item_type = item.get("type")
        location = item.get("location")
        prpoerties = item.get("properties")
        provision_state = prpoerties["provisioningState"]
        print(f"Name: {name}, Type: {item_type}, Location: {location}")
        rg_dict[name] = {}
        rg_dict[name]['Type'] = item_type
        rg_dict[name]['Location'] = location
        rg_dict[name]['Provision State'] = provision_state

    return data_dict


def fetch_all_vm_details(token,subId):
    auth = 'Bearer '+token
    url_for_vm = 'https://management.azure.com/subscriptions/'+subId+'/providers/Microsoft.Compute/virtualMachines?api-version=2023-07-01'
    headers = {
    'Authorization':auth
    }
    response = requests.get(url_for_vm,headers=headers )
    if response.status_code == 200:
        print(response.text)
        print("\n")
    else:
        print(f"Request failed with status code {response.status_code}")
    data_dict = json.loads(response.text)
    for key, value in data_dict.items():
        if key == "properties":
            print("Properties:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {sub_value}")
        else:
            print(f"{key}: {value}")
    return data_dict


def fetch_vm_details(token,subId,vmName,rg):
    auth = 'Bearer '+token
    url_for_vm = 'https://management.azure.com/subscriptions/'+subId+'/resourceGroups/'+rg+'/providers/Microsoft.Compute/virtualMachines/'+vmName+'?api-version=2023-07-01'
    headers = {
    'Authorization':auth
    }
    response = requests.get(url_for_vm,headers=headers )
    if response.status_code == 200:
        print(response.text)
        print("\n")
    else:
        print(f"Request failed with status code {response.status_code}")
    data_dict = json.loads(response.text)
    return data_dict

def fetch_ip_address_details(token,subId,rg,ipName):
    auth = 'Bearer '+token
    url_for_vm = 'https://management.azure.com/subscriptions/'+subId+'/resourceGroups/'+rg+'/providers/Microsoft.Network/publicIPAddresses/'+ipName+'?api-version=2023-05-01'
    headers = {
    'Authorization':auth
    }
    response = requests.get(url_for_vm,headers=headers )
    if response.status_code == 200:
        print(response.text)
        print("\n")
    else:
        print(f"Request failed with status code {response.status_code}")
    data_dict = json.loads(response.text)
    return data_dict



def gettoken(tenant_id,client_id,client_secret):
    # tenant_id = encryption.decrypt(Encrypt_varibles.tenant_id,tenant_id)
    # client_id= encryption.decrypt(Encrypt_varibles.client_id,client_id)
    # client_secret = encryption.decrypt(Encrypt_varibles.client_secret,client_secret)
    resource_url = 'https://management.azure.com'
    token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/token'
    
    token_data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'resource': resource_url
    }
    token_response = requests.post(token_url, data=token_data)
    token = token_response.json().get('access_token')
    return token
