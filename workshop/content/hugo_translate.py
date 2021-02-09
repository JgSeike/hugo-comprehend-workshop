#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json 
import boto3
import re

regex = r"\[[0-9]\. (.*?)\]\((.*?)\)"

trans = boto3.client('translate')

# Language Codes https://docs.aws.amazon.com/translate/latest/dg/what-is.html#what-is-languages
src_language = 'ko'
dst_language = 'pt'

markdown_tokens = [ '# ', '## ', '### ', '**', '*', '- ']

 
def translate(text):
    response = trans.translate_text(
            Text=text,
            TerminologyNames=[
                'hugo_ct'
            ],
            SourceLanguageCode=src_language,
            TargetLanguageCode=dst_language
        )
    return response['TranslatedText'].lstrip().rstrip()


def process_tokens(resp,text):
    if '### ' in text:
        resp.append(text.split('### ',1)[0])
        resp.append('# ')
        text = text.split('### ',1)[1]
        resp, text = process_tokens(resp,text) 
    elif '## ' in text:
        resp.append(text.split('## ',1)[0])
        resp.append('## ')
        text = text.split('## ',1)[1]
        resp, text = process_tokens(resp,text) 
    elif '# ' in text:
        resp.append(text.split('# ',1)[0])
        resp.append('# ')
        text = text.split('# ',1)[1]
        resp, text = process_tokens(resp,text)   
    elif '***' in text:
        resp.append(text.split('***',1)[0])
        resp.append('***')
        text = text.split('***',1)[1]
        resp, text = process_tokens(resp,text) 
    elif '**' in text:
        resp.append(text.split('**',1)[0])
        resp.append('**')
        text = text.split('**',1)[1]
        resp, text = process_tokens(resp,text)   
    elif '*' in text:
        resp.append(text.split('*',1)[0])
        resp.append('*')
        text = text.split('*',1)[1]
        resp, text = process_tokens(resp,text) 
    else: 
        resp.append(text)


    return resp, text

          


# Count the arguments
arguments = len(sys.argv) - 1
if arguments < 1:
    print ("Error, expected arguments 2, found "+ str(arguments))
    print ("Usage:   hugo_translate.py source_file.md destination_language_code [optional, default pt]")
    print ("Example: hugo_translate.py _index.ko.md en")
    exit()
else:
    source_file = sys.argv[1]
    if arguments == 2:
        dst_language = sys.argv[2]
    dest_file = source_file.replace(src_language,dst_language)







source = open(source_file, 'r') 
Lines = source.readlines() 
destination = open(dest_file,"w")  
print ("Writing: "+dest_file)
inHeader = False
inCode = False
inQuote = False
for line in Lines: 

    ##Don't translate hugo header
    if line.startswith('---'):
        if inHeader : 
            inHeader = False
            output =  line
        else:
            if ('----' not in line): 
                inHeader = True
                output =  line
            else: 
                output = line
    elif line.startswith('{{'):
        output =  line
    elif line.startswith('```'):
        inCode = not inCode
        output = line
    else:
        if (inHeader):
            if "title:" in line:
                title = line
                title = title.split('"')[1]

                output = 'title: "' + translate(title)+ '"  \n'
            else:    
                output = line
        elif inCode:
            output = line
        else:
            if ('](' in line) :
                if  ('![' in line) :
                    output = line
                else:
                    matches = re.finditer(regex, line, re.MULTILINE)
                    for matchNum, match in enumerate(matches, start=1):
                        itemtxt = match.groups()[0]
                        itemtxt2 = translate(itemtxt)
                        output = line.split(itemtxt)[0]+itemtxt2 +line.split(itemtxt)[1] 
            else: 
                items = []
                items, output = process_tokens(items,line)
                if items != []:
                    output = ""
                    for x in items:
                            if (x in markdown_tokens) or (x == ''):
                                output = output + x
                            else: 
                                output = output + translate(x) 
                output = output +'  \n'


    
    destination.write(output)
print ("done")