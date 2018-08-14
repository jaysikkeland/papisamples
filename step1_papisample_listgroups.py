#!/usr/bin/env python3
#
# PAPI Sample Snippet - List Groups
# - This snippet first prints all groups ("directories") under your account
# - Finally it parses the groups json and prints a specific group by group_name
#
# Instructions:
# - Python 2 or 3
# - Install required modules:  
#      pip install requests
#      pip install edgegrid-python
# - Edit the values in the REPLACE BEGIN/END section based on your environment
#

# more specific about creating credentials and edgerc
# full edgerc example with sections and size

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
# Group you want to print separately
group_name = 'PAPI Lab'
#
# --- REPLACE END ---

# Open session
baseurl = 'https://%s' % edgerc.get(section, 'host')
s = requests.Session()
s.auth = EdgeGridAuth.from_edgerc(edgerc, section)

# Get all groups using GET /papi/v1/groups
papiurl_getgroups = '/papi/v1/groups'
result = s.get(urljoin(baseurl, papiurl_getgroups))
parsed = json.loads(result.text)
print ("PAPI Status: " + str(result.status_code))
print ("--- Print all groups ---")
print (json.dumps(parsed['groups']['items'], indent=4, sort_keys=True))
print ()

# Print a specific group by parsing the previous json response and find groupName=group_name
# json format:
#[
#    {
#        "contractIds": [
#            "ctr_123"
#        ],
#        "groupId": "grp_567",
#        "groupName": "PAPI Lab",
#        "parentGroupId": "grp_890"
#    }
#]
find_group = [x for x in parsed['groups']['items'] if x['groupName'] == group_name]
print ("--- Find group: " + group_name + " ---")
print (json.dumps(find_group, indent=4, sort_keys=True))
