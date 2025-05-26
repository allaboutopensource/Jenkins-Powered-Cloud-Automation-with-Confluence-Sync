#!/usr/bin/python3
import openstack.cloud
import argparse
import re
import os
import csv
import sys

# Initialize and turn on debug logging
openstack.enable_logging(debug=False)

# Create a connection to the OpenStack cloud
user = os.getenv('OS_USERNAME')
pwd = os.getenv('OS_PASSWORD')
conn = openstack.connect(cloud='openstack')
conn2 = conn.connect_as(username=user, password=pwd)
cloud2 = conn2.connect_as_project('7b9b3c86a8ab4a6e9a1cdc8bb07ae190')

# Get all projects
projects = cloud2.identity.projects()
sorted_projects = sorted(projects, key=lambda p: p.name)
# Print the project names
project_list = []
# Print the project names
for p in sorted_projects:
     project_list.append(p.name)
# Print the project list
print(project_list)

