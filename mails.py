#Python3
import urllib.request as get
import re
from bs4 import BeautifulSoup

def generate_mail():
    #GET FULL WEBPAGE
    url = 'http://www.yopmail.com/en/email-generator.php'
    content = get.urlopen(url).read()

    #PARSE THE TAG
    #TO FIND THE EMAIL
    soup = BeautifulSoup(content, "html.parser")
    attributes = soup.find('input',{'id':'login'}).attrs
    email = attributes['value']
    return email
