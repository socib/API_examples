##AUXILIARY FUNCTIONS
import requests
import json
import shutil
import os
import math

def scbRequestHandler(query,headers):
    buffer, url , i = [], query, 1
    request = requests.get(url, headers=headers)
    response = json.loads(request.text)
    if isinstance(response, dict) == False:
        buffer = response
    elif isinstance(response, dict) and response['next'] == None :
        buffer = response['results']
    else:
        npages = math.ceil(response['count']/len(response['results']))
        while response['next'] is not None:
            i = i + 1
            buffer = buffer + response['results']
            try:
                request = requests.get(url, headers=headers)
                response = json.loads(request.text)
                url = response['next']
            except Exception as e:
                print('--- Error resolving '+url)
                if i<npages:
                    url = response['next'].replace('page='%s,'page='%s)%(str(i),str(i+1))
    return buffer


def scbDownloadHandler(element, target_dir, headers):
    buffer, i, cwd = [], 1, os.getcwd()
    if 'entries' in element.keys():
        buffer = buffer + scbRequestHandler(element['entries'],headers)
    else:
        buffer = [element]
    if len(buffer) == 0:
        print('No associated files could be found for element id'+element.id)
        return
    os.chdir(target_dir)
    filesdir = element['id']
    if not os.path.exists(filesdir):
        os.makedirs(filesdir)
    for ncfile in buffer:
        url = ncfile['services']['http_file']['url']
        local_filename =  os.path.join(filesdir,url.split('/')[-1])
        print('...Donwloading '+url.split('/')[-1])
        with requests.get(url, headers=headers, stream=True) as r:
            with open(local_filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
    os.chdir(cwd)
    print('Ready!')
    return