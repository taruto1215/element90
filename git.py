
import os
import sys

try:
    m = sys.argv[1]
except:
    m = 'pushed by git.py'


os.system('git add .')
os.system('git commit -m ""')
os.system('git push origin master')
