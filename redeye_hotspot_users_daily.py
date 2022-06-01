#!/usr/bin/python

import MySQLdb as mdb
import gc
import time

gc.collect()

print ("EMR HOTSPOT USERS DAILY EXPORT")

today = time.strftime("%Y_%m_%d")
filenameprefix = "emr_daily_hotspot_users"
fullfilename = filenameprefix + "_" + today + ".csv"
fullpath = "/home/uks/report_files/emr/"

# open the file and write the csv header
f = open(fullpath+fullfilename,'w')
print ("Opened output file")

f.write('email,forename,surname,postcode,offers_email,ico_active,ico_system_id,ico_created_at,ico_updated_at\n')
print ("Output file header")

conn = mdb.connect('hotspot.db.icomera.com','observer','mtotfls+127','hotspot',charset='utf8')
print ("Connected to DB")

sql = """SELECT `hotspot_users`.`email` AS `email`, `hotspot_users`.`forename` AS `forename`, `hotspot_users`.`surname` AS `surname`, 
`hotspot_users`.`postcode AS `postocode`, `hotspot_users`.`offers_email` AS `offers_email`, 
`hotspot_users`.`active` AS `ico_active`, `hotspot_users`.`system_id` AS `ico_system_id`, 
`hotspot_users`.`created_at` AS `ico_created_at`,
 `hotspot_users`.`updated_at` AS `ico_updated_at` FROM `hotspot_users` WHERE (date(`hotspot_users`.`updated_at`) = 
date(date_add(now(), INTERVAL -1 day))
   AND (`hotspot_users`.`customer_id` = 225)) """

cursor = conn.cursor(mdb.cursors.DictCursor)

cursor.execute(sql)
cursor.fetchone()
rows = cursor.fetchall()

for row in rows:

    outputstring = ""
    outputstring = outputstring + str(row['email']) + ","
    outputstring = outputstring + str(row['forename']) + ","
    outputstring = outputstring + str(row['surname']) + ","
    outputstring = outputstring + str(row['postcode']) + ","
    outputstring = outputstring + str(row['offers_email']) + ","
    outputstring = outputstring + str(row['ico_active']) + ","
    outputstring = outputstring + str(row['ico_system_id']) + ","
    outputstring = outputstring + str(row['ico_created_at']) + ","
    outputstring = outputstring + str(row['ico_updated_at']) 
    

    #print (outputstring)
    f.write (outputstring+"\n")

count = cursor.rowcount
conn.close()
f.close()


#Count lines in the file
row_count = sum(1 for line in open(fullpath+fullfilename))

print ("Emr hotspot daily report Completed")
