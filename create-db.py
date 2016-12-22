#!/usr/bin/python

import sys
import csv

"""
Tests the process to create a PostGreSQL database based on spec from property file.
"""

# List -> String
# Set the filename return to the name of the database property file with specifications 
# def get_db_prop([' ']): return 'None';
def get_prop_file(arglist):
   if len(arglist) == 1:
      filename = raw_input("Please provide filename that specifies database properties: ")
   elif len(arglist) == 2:
      filename = arglist[1]
   else:
      filename = "Please retry this script and supply the database property filename as the first argument"
   return filename

def main():
   # set database property filename
   filename = get_prop_file(sys.argv)
   print "Your database property filename is: ", filename, "\n"
   
   # Read database properties and return list of parameters that will be used to call db creation function
   
   
   # Call PostGreSQL with db parameters and create db
   
   # Test db exists and return schema and table list
      
   # Run test to add data 
   
   # Prompt to ask if db should be removed - comment this step out initially
   
   sys.exit()
   
if __name__ == "__main__":
   main()
