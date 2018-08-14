#!/usr/bin/env python3
# 
# PAPI Sample Snippet - List Property Details
# - This snippet finds a property by hostname and prints the hostnames/edgehostnames and the json rule tree of the last version.
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
# Hostname of the property you want to search for
host_name = 'papitest.akamlab.com'
#
# --- REPLACE END ---

# STEP 1
# Open session
baseurl = 'https://%s' % edgerc.get(section, 'host')
s = requests.Session()
s.auth = EdgeGridAuth.from_edgerc(edgerc, section)

# STEP 2
# Search for properties matching host_name using:
#    POST /papi/v1/search/find-by-value
# Sample response:
# {
#    "versions": {
#        "items": [
#            {
#                "accountId": "act_B-3-1A3M5A3",
#                "assetId": "aid_10582968",
#                "contractId": "ctr_3-1A42HS1",
#                "edgeHostname": "papitest.akamlab.com.edgesuite.net",
#                "groupId": "grp_113897",
#                "hostname": "papitest.akamlab.com",
#                "note": "made some changes",
#                "productionStatus": "INACTIVE",
#                "propertyId": "prp_477692",
#                "propertyName": "papitest.akamlab.com",
#                "propertyVersion": 2,
#                "stagingStatus": "INACTIVE",
#                "updatedByUser": "wp248@akamaiuniversity.com",
#                "updatedDate": "2018-08-07T01:51:37Z"
#            }
#        ]
#    }
# }
papiurl_searchproperties = '/papi/v1/search/find-by-value'
result = s.post(urljoin(baseurl, papiurl_searchproperties),json={"hostname": host_name})
parsed = json.loads(result.text)
print ("PAPI Status: " + str(result.status_code))
print ("--- Print search result for hostname="+host_name+" ---")
print (json.dumps(parsed, indent=4, sort_keys=True))

# STEP 3
# Find the latest version (search endpoint returns up to 3 versions - staging/production/latest)
# Note:  Here you would also often look for the version currently active on staging or production
propertyId = parsed['versions']['items'][0]['propertyId']
latestVersion = parsed['versions']['items'][0]['propertyVersion']
print ("--- Latest version for " + propertyId + " = Version " + str(latestVersion) + "---")
print ()

# STEP 4
# Print list of hostnames+edgehostnames for the latest property version using
#    GET /papi/v1/properties/123/versions/4/hostnames?validateHostnames=true
# Sample response:
# [
#    {
#        "cnameFrom": "papitest.akamlab.com",
#        "cnameTo": "papitest.akamlab.com.edgesuite.net",
#        "cnameType": "EDGE_HOSTNAME"
#    }
# ]
papiurl_gethostnames = '/papi/v1/properties/'+propertyId+'/versions/'+str(latestVersion)+'/hostnames?validateHostnames=true'
result = s.get(urljoin(baseurl, papiurl_gethostnames))
print ("PAPI Status: " + str(result.status_code))
parsed = json.loads(result.text)
print ("--- Property hostnames for " + propertyId + " (V" + str(latestVersion) + ") ---")
print (json.dumps(parsed['hostnames']['items'], indent=4, sort_keys=True))
print ()

# STEP 5
# Print latest version rule tree, skipping validation, using:
#    GET /papi/v1/properties/1234/versions/4/rules?validateRules=false
# Sample response:
# {
#    "accountId": "act_B-3-1A3M5A3",
#    "comments": "made some changes",
#    "contractId": "ctr_3-1A42HS1",
#    "etag": "6173c37819ae344ad2fb293b39cd5d3f4f09ee6f",
#    "groupId": "grp_113897",
#    "propertyId": "prp_477692",
#    "propertyName": "papitest.akamlab.com",
#    "propertyVersion": 2,
#    "ruleFormat": "latest",
#    "rules": {
#        "behaviors": [
#            {
#                "name": "origin",
#                "options": {
#                    "cacheKeyHostname": "ORIGIN_HOSTNAME",
#                    "compress": true,
#                    "enableTrueClientIp": true,
#                    "forwardHostHeader": "REQUEST_HOST_HEADER",
#                    "hostname": "origin-papitest.akamlab.com",
#                    "httpPort": 80,
#                    "originType": "CUSTOMER",
#                    "trueClientIpClientSetting": false,
#                    "trueClientIpHeader": "True-Client-IP"
#                }
#            },
#         etc...
papiurl_getruletree = '/papi/v1/properties/'+propertyId+'/versions/'+str(latestVersion)+'/rules?validateRules=false'
result = s.get(urljoin(baseurl, papiurl_getruletree))
parsed = json.loads(result.text)
print ("PAPI Status: " + str(result.status_code))
print ("--- Property json ruletree for " + propertyId + " (V" + str(latestVersion) + ") ---")
print (json.dumps(parsed, indent=4, sort_keys=True))
