#!/usr/bin/env python3
# 
# PAPI Sample Snippet - Upload property json rule tree
# - This snippet uploads a json rule tree to the latest property version
# - The snippet assumes that the latest property version is not active on staging or production
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
edgerc = EdgeRc('.edgerc')
# Edgegrid credentials section
section = 'default'
# Property id to be updated. Obtain the property id from by downloading property rule tree. See step3_papisample_listpropertydetails.py
property_id = "prp_477692"
# json rule tree file.  Obtain a starting point by first downloading a property rule tree. See step3_papisample_listpropertydetails.py
ruletree_file = "rules.json"
#
# --- REPLACE END ---

# STEP 1
# Open session
baseurl = 'https://%s' % edgerc.get(section, 'host')
s = requests.Session()
s.auth = EdgeGridAuth.from_edgerc(edgerc, section)

# STEP 2
# Get property versions using:
#     GET /papi/v1/properties/1234/versions
# Sample output:
# {
#    "accountId": "act_B-3-1A3M5A3",
#    "assetId": "aid_10582968",
#    "contractId": "ctr_3-1A42HS1",
#    "groupId": "grp_113897",
#    "propertyId": "prp_477692",
#    "propertyName": "papitest.akamlab.com",
#    "versions": {
#        "items": [
#            {
#                "etag": "6173c37819ae344ad2fb293b39cd5d3f4f09ee6f",
#                "note": "made some changes",
#                "productId": "prd_SPM",
#                "productionStatus": "INACTIVE",
#                "propertyVersion": 2,
#                "ruleFormat": "latest",
#                "stagingStatus": "INACTIVE",
#                "updatedByUser": "wp248@akamaiuniversity.com",
#                "updatedDate": "2018-08-07T01:51:37Z"
#            },

papiurl_getpropertyversions = '/papi/v1/properties/'+property_id+'/versions'
result = s.get(urljoin(baseurl, papiurl_getpropertyversions))
parsed = json.loads(result.text)
print ("PAPI Status: " + str(result.status_code))
print ("--- Print property versions for "+property_id+" ---")
print (json.dumps(parsed, indent=4, sort_keys=True))
print ()

# Latest version is first in the list (there are other ways to get the latest/staging/produtction versions)
latestVersion = parsed['versions']['items'][0]['propertyVersion']

# Upload (PUT) contents of ruletree_file using:
#     PUT /papi/v1/properties/1234/versions/4/rules
print ("--- Uploading property json for "+property_id+" (V"+str(latestVersion)+") ---")
papiurl_putversion = '/papi/v1/properties/'+property_id+'/versions/'+str(latestVersion)+'/rules'
# Set json Content-type
headers = {'Content-type': 'application/json'}
put_body=open(ruletree_file, 'rb')
result = s.put(urljoin(baseurl, papiurl_putversion), headers=headers, data=put_body)
parsed = json.loads(result.text)
print ("PAPI Status: " + str(result.status_code))
print (json.dumps(parsed, indent=4, sort_keys=True))
