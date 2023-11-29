import requests,json
import encryption
import Encrypt_varibles

def gettoken(tenant_id,client_id,client_secret):
    tenant_id = encryption.decrypt(Encrypt_varibles.tenant_id,tenant_id)
    client_id= encryption.decrypt(Encrypt_varibles.client_id,client_id)
    client_secret = encryption.decrypt(Encrypt_varibles.client_secret,client_secret)
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




# def fetch_all_subscriptions():
#     from fetch_resources import fetch_all_subscriptions_details
#     print("Fetching All Subscriptions")
#     fetch_all_subscriptions_details(token=token)
#     print("\n\n\n ")

# def fetch_all_resources():
#     from fetch_resources import fetch_all_resources_details
#     print("Fetching All Resources")
#     fetch_all_resources_details(token)
#     print("\n\n\n ")

# def fetch_vm_resources():
#     from fetch_resources import fetch_vm_details
#     print("Fetching VM Resources")
#     fetch_vm_details(token)
#     print("\n\n\n ")
    
# def fetch_rg_resources():
#     from fetch_resources import fetch_rg_details
#     print("Fetching Resource Group Resources")
#     fetch_rg_details(token=token)
#     print("\n\n\n ")
    
# tenant_id = ''
# client_id = ''
# client_secret = ''
# resource_url = 'https://management.azure.com'
# token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/token'

# token_data = {
#     'grant_type': 'client_credentials',
#     'client_id': client_id,
#     'client_secret': client_secret,
#     'resource': resource_url
# }
# token_response = requests.post(token_url, data=token_data)
# token = token_response.json().get('access_token')
# if not token:
#     print('Failed to get token')


# fetch_all_subscriptions()
# fetch_vm_resources()
# fetch_all_resources()
# fetch_rg_resources()
# print(gettoken("f2a009da-b491-4dbb-94e8-5809162549cd","9e46e6ee-df6f-438d-bf40-6dbfa737777c","szF8Q~xjzDW2_IFD0yyaOZE_SjkvX8TysLW86c8T"))




# auth = 'Bearer '+token
# url_for_all_resources = 'https://management.azure.com/subscriptions/72a851c4-6ce9-4328-902a-1b4f3e431554/resources?api-version=2021-04-01'
# url_for_vm = 'https://management.azure.com/subscriptions/72a851c4-6ce9-4328-902a-1b4f3e431554/resourceGroups/test-rg-1//providers/Microsoft.Compute/virtualMachines/test-vm?api-version=2021-04-01'
# headers = {
#     'Authorization':auth
# }

# response = requests.get(url_for_vm,headers=headers )

# if response.status_code == 200:
#     print(response.text)
# else:
#     print(f"Request failed with status code {response.status_code}")
    
# data_dict = json.loads(response.text)


# if int(input()):
#     # Extract name, type, and location for each item in the "value" list
#     for item in data_dict["value"]:
#         name = item.get("name")
#         item_type = item.get("type")
#         location = item.get("location")

#         print(f"Name: {name}, Type: {item_type}, Location: {location}")
# else:
#     for key, value in data_dict.items():
#         if key == "properties":
#             # Special handling for the "properties" dictionary
#             print("Properties:")
#             for sub_key, sub_value in value.items():
#                 print(f"  {sub_key}: {sub_value}")
#         else:
#             print(f"{key}: {value}")