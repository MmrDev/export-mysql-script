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

 
import os
import time
from datetime import date


class File:
	def __init__(self, address):
		self.address = address

	def listFiles(self):
		return os.listdir(self.address)

	def removeWeeclyBackups(self, files, today):
		today = int(today)
		for key in files:
			item = key[-6:]
			backUp_day = int(item[:2]) + 8
			if today == backUp_day and key[-3:] == 'sql':
				os.remove('/opt/dbBackUp/' + key)
				print(key + 'removed')
		


def main():
	address = '/opt/dbBackUp'
	today = format(date.today())[-2:]
	file = File(address)

	files = file.listFiles()
	print('list of backUps : ')
	print(files)
	print('_______________\n')
	file.removeWeeclyBackups(files, today)
    

if __name__ == '__main__':
    main()

