#!/usr/bin/python
from urllib2 import urlopen
import json, unicodedata


url='https://wiiu.titlekeys.com/json'
response = urlopen(url)
parsed = json.load(response)
key_file = open("keys.txt",'w') 
key_file.write("""#Common Keys#
D7B00402659BA2ABD2CB0DB27FA2B656 # Wii U Common Key:
805E6285CD487DE0FAFFAA65A6985E17 # Wii U Espresso Ancast Key
B5D8AB06ED7F6CFC529F2CE1B4EA32FD # Wii U Starbuck Ancast Key
############################################################

""")
data=''
for i in xrange(len(parsed)):
    if parsed[i]['titleKey'] == None or parsed[i]['name'] == None:
        pass
    else:
        key = parsed[i]['titleKey']
        name = parsed[i]['name']
        name = name.replace('\n','').replace('\t','')
        name = unicodedata.normalize('NFKD', name).encode('ascii','ignore')
        region = parsed[i]['region']
        line_data = str(key),' # ',name,' (',region,')'
        normalized_data = "".join(line_data)
        key_file.write("%s\n" %normalized_data)
key_file.close()
