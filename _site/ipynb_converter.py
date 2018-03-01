"""
Python script to convert the jupyter notebooks in the posts folder to
markdown format
"""

import os
import re
import fileinput
import sys
from glob import glob
import shutil
import datetime

path = '_posts/'

all_ipynb_files = [os.path.join(root, name) 
    for root, dirs, files in os.walk(path)
        for name in files
            if name.endswith((".ipynb"))]

# ignore checkpoint files
ipynb_files = [ x for x in all_ipynb_files if ".ipynb_checkpoints" not in x ]

curr_date = datetime.date.today().strftime("%Y-%m-%d")

# use nbconvert to convert the files
for file in ipynb_files:
    # Convert into markdown

    file_name = '{}-{}.md'.format(curr_date, file.split('/')[-1][:-6])
    os.system('jupyter nbconvert --to markdown {} --output {}'.format(file, 
        file_name))

# build jekyll
os.system('JEKYLL_ENV=production bundle exec jekyll b')
