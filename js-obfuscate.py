from requests import post
from urllib.parse import urlencode as ncode
from headerz import headerz as hdd
import re,html,sys


def header():
	raw ="""
POST /javascript-obfuscator.php HTTP/1.1
Host: beautifytools.com
User-Agent: Mozilla/5.0 (Android 9; Mobile; rv:68.0) Gecko/68.0 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: id-ID,id;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 66
Connection: keep-alive
Referer: http://beautifytools.com/javascript-obfuscator.php
Cookie:
Upgrade-Insecure-Requests: 1"""
	hd = hdd()
	head = hd.parser(raw)
	header = head["headers"]
	header.update(head["ua"])
	return header
def gas(command):
	if command:
		if command == "-i":
			print("input js code, input '!done' if you're done")
			x =""
			while True:
				js_code = input()
				if js_code != "!done":
					x += js_code
				else:
					break
			js_code = x
		elif command == "-f":
			js_code = open(input("file path: "),"r").read()
		else:
			print("command:\n* -i : input\n* -f file")
			exit()
		data = ncode({"src":js_code,"ascii_encoding":62,"fast_decode":"fast-decode"})
		u = "http://beautifytools.com/javascript-obfuscator.php"
		hdr = header()
		r = post(u,headers=hdr,data=data)
		js_encoded = re.search(r"\>(.*?)\n<\/textarea>",r.text).group(1)
		o = html.unescape(js_encoded).strip()
		#p = open("js.html","r").read().replace("%%jscode%%",o)
		x = open(input("nama: ")+".js","w")
		x.write(o)
		x.close()
	else:
		print("command:\n* -i : input\n* -f file")
if len(sys.argv) < 3:
	print("command:\n* -i : input\n* -f : file")
else:
	gas(sys.argv[2])
