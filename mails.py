import urllib2
tagToMatch = 'id="login"'
valueTag = "value="
valueSize = len(valueTag) + 1
yopMailUrl = "http://www.yopmail.com/es/email-generator.php"
contents = urllib2.urlopen(yopMailUrl).readlines()
for line in contents :
	if tagToMatch in line :
		line = line[line.index(valueTag) + valueSize : -5].replace("&#64;","@")
		print line
