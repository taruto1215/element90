
import os
import sys

try:
    arg1 = sys.argv[1]
except:
    arg1 = 'default'

os.system('git add .')
os.system('git commit -m {0}'.format(arg1))
os.system('git push -f heroku master')
