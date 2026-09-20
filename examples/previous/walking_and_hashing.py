'''
Assignment 2 Help

'''

import os
import hashlib

DIR = '../../logs'  # Current Directory
# DIR = '../docs/' # Docs Directory

file_hashes = {}

for root, dirs, files in os.walk(DIR):

    # Walk the path from top to bottom.
    # For each file obtain the filename 
    
    for file_name in files:
        path = os.path.join(root, file_name)
        full_path = os.path.abspath(path)
        print("Reading File at: " + full_path)
        with open(full_path, 'rb') as file_obj:
            file_content = file_obj.read()
            # Assuming these are small files .read() is ok, otherwise read in chunks
            # or you'll consume a lot of memory
            sha256_obj = hashlib.sha256()
            sha256_obj.update(file_content)
            hex_digest = sha256_obj.hexdigest()
            print(f"Hex Digest of {file_obj.name}: {hex_digest}")
        
        # At this point you need to hash the
        # the contents of each file
        

        
        
