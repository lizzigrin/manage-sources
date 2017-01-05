#!/usr/bin/python

import sys
import csv
#import psycopg2

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
   db_dict = {}   

   with open(filename,'rb') as csvFile:
      csvReader = csv.reader(csvFile)
      for row in csvReader:
         f_name, f_value = row
         db_dict[f_name] = f_value
   
   # Call PostGreSQL with db parameters and create db
   print "dbname is ",db_dict['dbname'], " user is ", db_dict['user']
   print " host is ", db_dict['host'], " password is ", db_dict['password'] 
   #con = connect(dbname = 'postgres', user = db_dict['user'], host = db_dict['host'], password = db_dict['password'])
   #cur = con.cursor()
   #cur.execute('CREATE DATABASE ' + db_dict['dbname']
   #cur.close()
   #con.close()
   
   # Test db exists and return schema and table list
      
   # Run test to add data 
   
   # Prompt to ask if db should be removed - comment this step out initially
   
   sys.exit()
   
if __name__ == "__main__":
   main()
