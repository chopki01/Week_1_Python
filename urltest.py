import urllib2
import re

def search(curUrl,curDep,allUsedUrls):
	global searchString
	global maxDepth
	
	try:
		webPage = urllib2.urlopen(curUrl, timeout=5)
		lines = [line for line in webPage]
		if len([x for line in lines for x in re.findall(searchString,line)  ]) != 0: #if page contains python add to list #python string
			print curUrl
			
		if curDep == maxDepth:
			return
			
		nexDep = curDep+1
		newUrls = set([x for line in lines for x in re.findall(r'http://[a-zA-z0-9\:\\\/\.\(\)\-\?]+',line)  ]) #find all lines with a url in it and grab the urls
		
		newUrls = newUrls - allUsedUrls 		#only test new links
		allUsedUrls = newUrls | allUsedUrls 	#update all used urls
		
		return [search(x, nexDep,allUsedUrls) for x in newUrls]	
	except urllib2.URLError:
		pass
	

	
	
seed = str(raw_input("Input Seed for Search\n")) #"http://docs.python.org"
maxDepth = int(raw_input("Input depth\n"))
searchString = raw_input("Input search string\n")


urls = [x for line in urllib2.urlopen(seed) for x in re.findall(r'http://[a-zA-z0-9\:\\\/\.\-\?]+',line)  ] #find all lines with a url in it and grab the url
allUsedUrls = set(urls)

[search(x, 0, allUsedUrls) for x in allUsedUrls]
