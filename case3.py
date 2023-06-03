#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# case3.py
#
# 2022-03-26 converted to Python 3
# removed dependency on deanishe's Alfred Workflow library

# 2014-09-10 by Derick Fay
#
# original inspiration from jdc0589's CaseConversion plug-in for SublimeText:
# https://github.com/jdc0589/CaseConversion/blob/master/case_conversion.py
#
#

import sys
import re
import string
import os
import json 
from titlecase import *

def SendDown(key):
    string = str(key)
    cmd = """osascript -e 'tell application "System Events" to key down (key code """ + string   + ")'"
    os.system(cmd)
    
def copy_selection():
	SendDown(8)

def to_upper(text):
	return text.upper()
	
def to_lower(text):
	return text.lower()

def to_capitalized(text):
	text = string.capwords(text)
	return text
	
def to_sentence_case(text):
	text = text[0].upper() + text[1:].lower()
	return text

# titlecase defined in separate file - from https://muffinresearch.co.uk/titlecasepy-titlecase-in-python/
 
def produceOutput(theString): 
    result = {"items": []}
    # Add items to Alfred feedback with uids so Alfred will track frequency of use
    
    resultString = to_upper(theString)
    result["items"].append({
        "title": resultString,
        'subtitle': "Upper Case",
        'valid': True,
        'uid': 'uppercase',
        "icon": {
            "path": 'icon.png'
        },
        'arg': resultString
            }) 

    resultString = to_lower(theString)
    result["items"].append({
        "title": resultString,
        'subtitle': "Lower Case",
        'valid': True,
        'uid': 'lowercase',
        "icon": {
            "path": 'icon.png'
        },
        'arg': resultString
            }) 
            
    resultString = to_capitalized(theString)
    result["items"].append({
        "title": resultString,
        'subtitle': "Capitalized",
        'valid': True,
        'uid': 'Capitalized',
        "icon": {
            "path": 'icon.png'
        },
        'arg': resultString
            }) 
    
    resultString = to_sentence_case(theString)
    result["items"].append({
        "title": resultString,
        'subtitle': "Sentence Case",
        'valid': True,
        'uid': 'Sentencecase',
        "icon": {
            "path": 'icon.png'
        },
        'arg': resultString
            }) 
    
    resultString = titlecase(theString)
    result["items"].append({
        "title": resultString,
        'subtitle': "Title Case",
        'valid': True,
        'uid': 'titlecase',
        "icon": {
            "path": 'icon.png'
        },
        'arg': resultString
            }) 
    
    
    print (json.dumps(result ))

def main():
    if len(sys.argv) > 2:
        theString = sys.argv[1]
        mySource = sys.argv[2]
        
        myReplacementString = eval(mySource)
        
        myReplacementString = globals()[mySource](theString)
        sys.stdout.write(myReplacementString)
        sys.stdout.flush()
        
    else:
        theString = sys.argv[1] 
        produceOutput (theString)
        
if __name__ == '__main__':
    main()
    
    