import urllib2

#Constants
YOP_MAIL_URL = "http://www.yopmail.com/es/email-generator.php"
VALUE_TAG 	 = "value="
VALUE_SIZE 	 = len(VALUE_TAG) + 1
TAG_TO_MATCH = 'id="login"'

#Mail generator
def generate_mail():
	contents = urllib2.urlopen(YOP_MAIL_URL).readlines()
	for line in contents :
		if TAG_TO_MATCH in line :
			from_idx = line.index(VALUE_TAG) + VALUE_SIZE
			return line[ from_idx : -5 ].replace("&#64;","@")

#Entrada para llamarlo como proceso
if __name__ == '__main__':
	print generate_mail()