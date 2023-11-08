import json
import pprint

import urllib3

# Make the HTTP request.
response = urllib3.request("GET",
                           'https://opendata.nhsbsa.net/api/3/action/package_list')
assert response.status == 200

# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.data)

# Check the contents of the response.
assert response_dict['success'] is True
result = response_dict['result']
pprint.pprint(result)
