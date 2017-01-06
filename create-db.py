#!/usr/bin/python

import sys
import csv
import psycopg2 as pg
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

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
   try:
      con = pg.connect(dbname = 'postgres', user = db_dict['user'], host = db_dict['host'], password = db_dict['password'])
   except OperationalError as err:
      print("Error class is: ", type(err))
      print("Error message is: ", err)

   cur = con.cursor()
   
   con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

   # Form SQL for database creation from parameter dbname supplied from db property file
   SQL = "CREATE DATABASE " + db_dict['dbname'] + ";"
   cur.execute(SQL)

   # close connection to database
   cur.close()
   con.close()
      
   sys.exit()
   
if __name__ == "__main__":
   main()
