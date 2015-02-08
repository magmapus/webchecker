import time
import os
import sys
import requests
import hashlib
import subprocess
import pickle
f=open("websites.conf","r")
lines=f.readlines()
f.close()
websites=[]

def sendpush(sitename):
	subprocess.call(["pushbullet-bash/pushbullet", "push", "all", "note", "Website Changed", sitename])

for site in lines:
	sitedef={}
	sit=site.split("\t")
	sitedef["url"]=sit[0]
	if sitedef["url"][0]=="#":
		continue
	sitedef["name"]=sit[1].rstrip()
	sitedef["hash"]=""
	sitedef["nexthash"]="no"
	websites.append(sitedef)
while 1:
	if True:
		for site in websites:
			sitetext=requests.get(site["url"]).text
			hash=hashlib.sha1(sitetext.encode("utf-8")).hexdigest()
			print hash
			if hash != site["hash"]:
				if site["nexthash"]==hash: # Some sites send very slightly modified versions every once in a while. This second check checks for a different hash two times in a row.
					site["hash"]=hash
					sendpush(site["name"])
				site["nexthash"]=hash
		time.sleep(60) # Don't run all the time
#	except:
#		print "badrun"
