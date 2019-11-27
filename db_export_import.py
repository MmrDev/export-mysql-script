#!/usr/bin/python

###########################################################
#
# This python script is used for mysql database backup
# using mysqldump and tar utility.
# 
# Written by : MmrDev
# Tested with : Python 2.7.15 & Python 3.5
#
##########################################################

import time
from datetime import date
import os
import pipes
import pymysql


## working with db class (connect & export & import)
## TODO add import method
class Db:
    def __init__(self, file_name, db_user, db_pass ,
                             db_name ,
                             db_host = 'localhost',
                             db_port = '3306'):
        self.file_name = file_name
        self.db_url = db_url
        self.db_port = db_port
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_name = db_name

    def dbConnection(self):
        db_conn = pymysql.connect(host = self.db_url,
                             user = self.db_user,
                             password = self.db_pass,
                             db = self.db_name)
        return db_conn

    def dbExport(self):
        dumpcmd = "mysqldump " + " -u " + self.db_user + " -p" + self.db_pass + " " + self.db_name + " > " + pipes.quote(self.file_name)
        os.system(dumpcmd)
        return dumpcmd


     def dbImport(self):
        dumpcmd = "mysqldump " + " -u " + self.db_user + " -p" + self.db_pass + " " + self.db_name + " < " + pipes.quote(self.file_name)
        # i think its wrong TODO
        os.system(dumpcmd)
        return dumpcmd


## TODO file class for write to file (use for Log) 
class File:
    def __init__(self, name, logString):
        self.filename = name
        self.logString = logString


    def write(self):
        text_file = open(self.filename, "a+")
        text_file.write(self.logString)
        text_file.close()    



def main():

    db = Db(file_name, db_user, db_pass, db_name, db_url)
    db.dbConnection()
    db.dbExport()
    


if __name__ == '__main__':

    db_url = 'localhost'
    db_user = 'root'
    db_pass = '<yourPassword>'
    db_name = '<dbName>'
    address = "<exportPath>"
    file_name = address + db_name + '_' + format(date.today())  + '.sql'

    main()
