import os
import re
import zipfile
from collections import namedtuple
from shutil import copy, copyfile

import requests as req

import settings

# Check settings
# is_on_path = os.getenv('LOCAL_PROGRAM')
# if not is_on_path:
#     os.environ['LOCAL_PROGRAM'] = settings.BASE_DIR

# print(os.environ)

generators = []
for constructed_dir in settings.CONSTRUCTED_DIRS:
    for key in constructed_dir:
        # Get key
        files = os.walk(constructed_dir[key])
        if files:
            # Append the generator
            generators.append(files)

# Do something with the
# generator
query_for_files = []
for generator in generators:
    # Get list of items
    items = list(generator)[0]
    # Get path in order to construct
    # file + path e.g. c:\...\file.*
    path = items[0]
    for item in items:
        if isinstance(item, list) and len(item) > 1:
            for user_file in item:
                extension = re.search(r'\.(xlsx|zip|docx|pdf|csv|pptx)', str(user_file))
                if extension:
                    # Construct full path and append
                    query_for_files.append(os.path.join(path, user_file))

# Now copy each file
# in the local base directory
if not os.path.exists(settings.LOCAL_FILE_DIR):
    os.mkdir(settings.LOCAL_FILE_DIR)

# Copy files to local directory
for queried_file in query_for_files:
    # Create a zip file in temp
    # zipfile.ZipFile.write(queried_file)
    # Copy files in temp
    copy(queried_file, settings.LOCAL_FILE_DIR)

# Post on the internet
# payload = dict(key1='value1', key2='value2')  
# response = req.post('http://httpbin.org/post', data=payload)
# if response.status_code == 200:
#     print('Updloded zip on %s' % settings.CLOUD_DIRECTORY)
