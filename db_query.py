# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 22:50:29 2020

@author: Eric Dudgeon
"""
###import modules####
try:
    import pandas as pd
    import mysql.connector
except:
    print('module not found')

try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Ercddgn21!"
    )
except:
    print('error')
    
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)