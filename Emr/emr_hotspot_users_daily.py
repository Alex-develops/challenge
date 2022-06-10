#! /usr/bin/python

import MySQLdb as mdb
import gc
import time

gc.collect()

print ("EMR HOTSPOT USERS DAILY EXPORT")

today = time.strftime("%Y_%m_%d")
# filenameprefix = "emr_daily_hotspot_users"
filenameprefix = "icomera_emr_daily_hotspot_users"
fullfilename = filenameprefix + "_" + today + ".csv"
fullpath = "/home/alex_develops/redeye/Emr/"

# open the file and write the csv header
f = open(fullpath+fullfilename,'w')
print ("Opened output file")

f.write('email,terms,emailpermit,ico_active,ico_system_id,ico_created_at,ico_updated_at\n')
print ("Output file header")

conn = mdb.connect('hotspot.db.icomera.com','observer','mtotfls+127','hotspot',charset='utf8')
print ("Connected to DB")

sql = """SELECT `hotspot_users`.`email` AS `email`, 
`hotspot_users`.`address1` AS `terms`, 
`hotspot_users`.`offers_email` AS `emailpermit`, 
`hotspot_users`.`active` AS `ico_active`,`hotspot_users`.`system_id` AS `ico_system_id`,
 DATE_FORMAT(`hotspot_users`.`created_at`,'%m/%d/%Y %H:%i:%s') AS `ico_created_at`, DATE_FORMAT(`hotspot_users`.`updated_at`,'%m/%d/%Y %H:%i:%s') as `ico_updated_at` FROM `hotspot_users` WHERE created_at >= DATE(NOW()) - INTERVAL 1 DAY AND customer_id="225" """


cursor = conn.cursor(mdb.cursors.DictCursor)

cursor.execute(sql)
cursor.fetchone()
rows = cursor.fetchall()

for row in rows:

    outputstring = ""
    outputstring = outputstring + str(row['email']) + ","
    outputstring = outputstring + str(row['terms']) + ","
    outputstring = outputstring + str(row['emailpermit']) + ","
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

