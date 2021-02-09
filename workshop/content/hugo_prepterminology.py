#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import json 
import boto3

client = boto3.client('translate')
# Read the terminology from a local file
with open('terminology.csv', 'rb') as f:
    data = f.read()
file_data = bytearray(data)


response = client.import_terminology(
    Name='hugo_ct',
    MergeStrategy='OVERWRITE',
    Description='string',
    TerminologyData={
        'File': file_data,
        'Format': 'CSV'
    }
)
print (response)