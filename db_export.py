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
    def __init__(self, db_user, db_pass,
                 db_host='localhost',
                 db_port='3306'):
        self.db_url = db_host
        self.db_port = db_port
        self.db_user = db_user
        self.db_pass = db_pass

    def dbConnection(self):
        db_conn = pymysql.connect(host=self.db_url,
                                  port=self.db_port,
                                  user=self.db_user,
                                  password=self.db_pass)
        return db_conn

    def dbNames(self):
        defaultDb = ['information_schema', 'mysql', 'performance_schema', 'phpmyadmin', 'sys']

        conn = self.dbConnection()
        cursor = conn.cursor()
        cursor.execute("SHOW DATABASES")
        dataBases = cursor.fetchall()
        dataBases = [i[0] for i in dataBases]
        for key in defaultDb:
            if key in dataBases:
                dataBases.remove(key)
        return dataBases


    def dbExport(self, dbName, file_name):
        dumpcmd = "mysqldump " + " -h " + self.db_url + " -P " + self.db_port + " -u " + self.db_user + " -p" + self.db_pass + " " + dbName + " > " + pipes.quote(
            file_name)
        os.system(dumpcmd)
        return dumpcmd

    def dbImport(self):
        dumpcmd = "mysqldump " + " -u " + self.db_user + " -p" + self.db_pass + " " + self.db_name + " < " + pipes.quote(
            self.file_name)
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
    db = Db(db_user, db_pass, db_url)
    databases = db.dbNames()
    for item in databases:
        file_name = address + item + '_' + format(date.today()) + '.sql'
        db.dbExport(item, file_name)


if __name__ == '__main__':
    db_url = 'localhost'
    db_port = '3306'
    db_user = 'root'
    db_pass = your_password
    address = "/opt/dbBackUp/"

    main()
