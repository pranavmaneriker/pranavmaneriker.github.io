import urllib2, urllib
url = "http://patft.uspto.gov/netahtml/PTO/search-bool.html"
values = {"Sect1": "PT02", 
		  "Sect2": "HITOFF",
		  "p": 1,
		  "u": "/netahtml/PTO/search-bool.html",
		  "r": 0,
		  "f": "S",
		  "l": 500,
		  "TERM1": "Intuitive+Surgical",
		  "FIELD1": "ASNM",
		  "cc1": "AND",
		  "TERM2": "",
		  "FIELD2": "",
		  "d": "PTXT"}
query = urllib.urlencode(values)
print query