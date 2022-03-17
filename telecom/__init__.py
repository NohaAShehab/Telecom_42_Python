# ## here you can either define some functions that can be
# accessed using the package name

def telecompkg():
    print("I am the function inside the init module")


# ## indexing for the functions inside modules related the package
from telecom.dbfunctions import connectToDB
