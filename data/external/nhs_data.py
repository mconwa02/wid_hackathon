import json
import pprint

import urllib2
import urllib3

# Make the HTTP request.
response = urllib3.request(
    "GET", "https://opendata.nhsbsa.net/api/3/action/package_list"
)
assert response.status == 200

# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.data)

# Check the contents of the response.
assert response_dict["success"] is True
result = response_dict["result"]
pprint.pprint(result)

# Put the details of the dataset we're going to create into a dict.
dataset_dict_I = {
    "name": "my_dataset_name",
    "notes": "A long description of my dataset",
    "owner_org": "org_id_or_name",
}

# Put the details of the dataset we're going to create into a dict.
dataset_dict = {
    "name": "hospital-prescribing-dispensed-in-the-community",
    "notes": "A long description of my dataset",
    "owner_org": "org_id_or_name",
}

# Use the json module to dump the dictionary to a string for posting.
data_string = urllib2.quote(json.dumps(dataset_dict))

# We'll use the package_create function to create a new dataset.
request = urllib2.Request(
    "http://www.my_ckan_site.com/api/action/package_create"
)

# Creating a dataset requires an authorization header.
# Replace *** with your API key, from your user account on the CKAN site
# that you're creating the dataset on.
request.add_header("Authorization", "***")

# Make the HTTP request.
response = urllib2.urlopen(request, data_string)
assert response.status == 200

# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.read())
assert response_dict["success"] is True

# package_create returns the created package as its result.
created_package = response_dict["result"]
pprint.pprint(created_package)
