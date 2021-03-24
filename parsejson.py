import json
import datetime

myf = open('firstout.json',)
mydata=json.load(myf)

for datum in mydata:
  print(datum['system_id'])
  for kv in datum['kv']:
    mykey=kv['key']
    for value in kv['Value']:
      myval=kv['Value'][value]
    if mykey == "__prefix__":
      prefix=myval
    if "timestamp" in mykey:
      myval=datetime.datetime.fromtimestamp(myval/1000)
    if mykey[0] != '/' and mykey[0] != '_':
      print(f"{prefix}{mykey} -> {myval}")
    else:
      print(f"{mykey} -> {myval}")
