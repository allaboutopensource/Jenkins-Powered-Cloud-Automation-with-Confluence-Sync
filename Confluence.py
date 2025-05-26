#!/usr/bin/python3

import requests
import json
import base64
import html 
import re
import os
import sys
import time
import openstack_project_list
# Set your Confluence credentials
username = os.getenv('email')
api_token = os.getenv('API_KEY')
# Set the title and content of the page to create
PAGE_ID = "700122109"
page_title = 'OpenStack project space'
space_key = "PENG"
# Confluence API URL for creating a new page
#url = f"https://ellucian-sandbox-102.atlassian.net/wiki/rest/api/content/{PAGE_ID}"

url = f"https://ellucian.atlassian.net/wiki/rest/api/content/{PAGE_ID}"

auth = base64.b64encode(f'{username}:{api_token}'.encode()).decode()
# Request headers
headers = {
    'Authorization': f'Basic {auth}',
    'Content-Type': 'application/json',
}

# Get the current page version
response = requests.get(url, headers=headers)
current_version = response.json()['version']['number']

#print(openstack_project_list.project_list[5])
# Add the project list to the HTML content
project_list = openstack_project_list.project_list
project_list_html = '<ul>'
for project in project_list:
    project_list_html += f'<li>{html.escape(project)}</li>'
project_list_html += '</ul>'

# Create the basic auth for use in the authentication header

# Request body data
data = {
    'id': PAGE_ID,
    'type': 'page',
    'title': page_title,
    'space': {'key': space_key},
    'body': {
        'storage': {
            'value': project_list_html,
            'representation': 'storage',
        }
    },
    "version": {
        "number": current_version + 1,
        "message": "Updated from OpenStack Cloud"
    }
}

# Make the API request to update the page
try:
    response = requests.put(url, data=json.dumps(data), headers=headers)
    response.raise_for_status()  # Raise an error for bad status codes
    print('Page Updated Successfully!')
except requests.exceptions.RequestException as e:
    print(f'Error: {e}')

