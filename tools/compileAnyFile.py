# !/usr/bin/python3
import os, sys

# listing directories
os.chdir("../../Parts")
directories = os.listdir(os.getcwd())

for d in directories:

    if(d[0] != "."):
        os.rename(d, "."+d)

print (">>> Any directory will be compiled")
