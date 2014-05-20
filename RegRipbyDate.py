'''

Created on May 19, 2014

@author: CaptainCrabnasty
----------------------------------------------------------------------------------
Copyright 2014

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
----------------------------------------------------------------------------------

A script very similar to William Ballenthin's print all sample script @ 
https://github.com/williballenthin/python-registry/blob/master/samples/printall.py, 
but this allows for a more elegant way to do a refined search of the registry to happen 
based upon the modified date.

'''

from Registry import Registry
from datetime import datetime
import argparse
import os
import csv

mydic = {}

def createdate(datestr):
	try:
		return datetime.strptime(datestr, "%Y-%m-%d %H:%M:%S")
	except Exception, e:
		print e
				  
def fileexists(filepath):
	try:
		if os.path.isfile(filepath):
			return filepath
		else:
			print "There is no hive at:" + filepath
	except Exception, e:
			print e
						
def rip():
	parser = argparse.ArgumentParser(description="Parse the Windows registry hive for date related artifacts.")
	parser.add_argument("-e", "--earliest", type=createdate, required=True, metavar="2014-01-26 00:00:00", help="Earliest Date. Format: 2014-01-26 00:00:00")
	parser.add_argument("-l", "--latest", type=createdate, required=True, metavar="2014-01-27 00:00:00", help="Latest Date Format: 2014-01-27 00:00:00")
	parser.add_argument('-i', '--hive', type=fileexists, required=True, metavar="'/Desktop/Somewhere/HiveName'", help='Location of the Windows registry hive file Date')
	parser.add_argument('-c', '--csv', help='Optional Parameter == output of csv.', action='store_true', default=False)
	args = parser.parse_args()

	if args.earliest and args.latest and args.hive:
		f = open(args.hive, "rb")
		r = Registry.Registry(f)
		MIN_DATE =  datetime.strptime(str(args.earliest), "%Y-%m-%d %H:%M:%S")
		MAX_DATE = datetime.strptime(str(args.latest), "%Y-%m-%d %H:%M:%S")
		#createdate(str(args.earliest))
		rec(r.root(),MIN_DATE,MAX_DATE)
		if args.csv:
			#User wants csv output.
			x=csv.writer(open(getDir(args.hive),'wb'), delimiter=',', dialect='excel-tab', quoting=csv.QUOTE_ALL)
			x.writerow(['Timestamp','Key Path'])
			for key, value in mydic.iteritems():
				x.writerow([str(key), str(value)])
		else:
			#User wants no output.
			for key, value in mydic.iteritems():
				print "%s, %s" % (key, value)
	else:
		print parser.usage
		exit(0)

def rec(key,MIN_DATE,MAX_DATE):
    if MIN_DATE < key.timestamp() < MAX_DATE:
        #print "%s    %s" % (key.timestamp(), key.path())
		mydic.update({key.timestamp(): key.path()}) 
    for subkey in key.subkeys():
        rec(subkey,MIN_DATE,MAX_DATE)

def getDir(x):
	return x.rsplit('/', 1)[0] + '/' + 'RegRipbyDate.txt'

if __name__ == "__main__":
    rip()
