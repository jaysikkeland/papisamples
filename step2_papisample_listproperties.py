#!/usr/bin/env python3
# 
# PAPI Sample Snippet - List Property Manager Configs
# - This snippet lists all properties (aka property manager configs) in a group (you will need a group_id).
# - Finally it parses the properties json and prints the details for a specific property by property_name
#
# Instructions:
# - Python 2 or 3
# - Install required modules:  
#      pip install requests
#      pip install edgegrid-python
# - Edit the values in the REPLACE BEGIN/END section based on your environment
#

# required  modules 
import requests, json
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin
# akamai open authentication edgegrid module
from akamai.edgegrid import EdgeGridAuth, EdgeRc

# --- REPLACE BEGIN ---
#
# Edgegrid credentials file and section
edgerc = EdgeRc('/Users/jsikkela/.edgerc')
# Edgegrid credentials section
section = 'default'
#
# Group and contract for the properties you want to print
# You can find the group from the gid query parameter when viewing a property manager version in the portal
# You can find the contract from the property version information section when viewing a property manager version
# You can also retrieve these values from the GET /papi/v1/groups json output
group_id = '113897'
# You can find the contract from the property version information section when viewing a property manager version
contract_id = '3-1A42HS1'
# Property name you want to print
property_name = 'papitest.akamlab.com'
#
# --- REPLACE END ---

# Open session
baseurl = 'https://%s' % edgerc.get(section, 'host')
s = requests.Session()
s.auth = EdgeGridAuth.from_edgerc(edgerc, section)

# Get a list of properties in a group using GET /papi/v1/properties?groupId=123&contractId=456
papiurl_getproperties = '/papi/v1/properties?groupId='+group_id+'&contractId='+contract_id
result = s.get(urljoin(baseurl, papiurl_getproperties))
parsed = json.loads(result.text)
print ("PAPI Status: " + str(result.status_code))
print ("--- Print all properties in "+contract_id+"/"+group_id+" ---")
print (json.dumps(parsed, indent=4, sort_keys=True))
print ()

# Print specific property by parsing the previous json response and find propertyName=property_name
# json format:
# {
#    "properties": {
#        "items": [
#            {
#                "accountId": "act_123",
#                "assetId": "aid_234",
#                "contractId": "ctr_345",
#                "groupId": "grp_456",
#                "latestVersion": 1,
#                "productionVersion": null,
#                "propertyId": "prp_567",
#                "propertyName": "test.myproperty.com",
#                "stagingVersion": null
#            },
find_property = [x for x in parsed['properties']['items'] if x['propertyName'] == property_name]
print ("--- Print property: " + property_name + " ---")
print (json.dumps(find_property, indent=4, sort_keys=True))
print ()

# Get the list of versions for the specific property (the first item in the find_property list)
# Using GET /papi/v1/properties/123/versions
property_id = find_property[0]['propertyId']
papiurl_getpropertyversions = '/papi/v1/properties/'+property_id+'/versions'
result = s.get(urljoin(baseurl, papiurl_getpropertyversions))
parsed = json.loads(result.text)
print ("PAPI Status: " + str(result.status_code))
print ("--- Print all versions of "+property_id+" ("+property_name+")")
print (json.dumps(parsed, indent=4, sort_keys=True))
