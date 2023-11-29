import csv
import random
code = """
resource "azurerm_resource_group" "example" {
    name=""
    location = "EastUS"
}

"""

# Sample text data
text_data = [["prompt","code"]
]

for i in range(1000):
    nn = chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))

    prompt = "Deploy a resource group with name "+nn
    
    code = """
resource "azurerm_resource_group" "example" {
    name=\""""+nn+"""\"
    location = "EastUS"
}
"""
    arr = [prompt,code]
    text_data.append(arr)



csv_file_path = "resource_group.csv"

# Open the CSV file in write mode and specify newline='' to ensure consistent line endings
with open(csv_file_path, mode='w', newline='') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)
    
    # Write the text data to the CSV file
    csv_writer.writerows(text_data)

print(f"Data has been saved to {csv_file_path}")
