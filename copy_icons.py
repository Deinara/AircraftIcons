import os
import shutil
import fnmatch
import json

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def load():
    with open(duplicatefile, 'r') as JSON:
        copy_dict = json.load(JSON)
    with open(placeholderfile, 'r') as JSON:
        copy_dict_add = json.load(JSON)
    copy_dict.update(copy_dict_add)
    return copy_dict
    
def copy():
    duplicates = load()
    for key, value in duplicates.items():
        print("Searching for icon '" + value + "'")
        filename = value + ".*"
        searchresult = find(filename, './')
        if(len(searchresult)<1):
            print("No icon found")
        else:
            filepath = searchresult[0]
            dirpath = os.path.dirname(filepath)
            destpath = dirpath + "/" + key + ".svg"
            copied = shutil.copy(filepath, destpath) # target filename is /dst/dir/file.ext
            print("Copied to: " + copied)
        print("")


duplicatefile = './duplicates.json'
placeholderfile = './placeholders.json'

copy()
