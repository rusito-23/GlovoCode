import urllib2
from json import dumps, loads
from mails import generate_mail

DBG       = False
CODE      = "nolitaglovoco"
TEST_MAIL = "fofibiddas-1600@yopmail.com"

def register(email, path = '/v3/users/customer') :
    print "Registrando [ %s ]" % email
    data = {
        "email":email,
        "password":"qwer1234",
        "name":"beta",
        "preferredLanguage":"es",
        "mediaSource":"Organic Web",
        "mediaCampaign":"Organic Web",
        "privacySettings":["DATA_POLICY"],
        "shownPermissions":["MARKETING_CAMPAIGNS","DATA_POLICY"]
    }
    return resolve (data,path)

def promotion_code(user, path = '/v3/promocodes'):
    print "Pidiendo codigo [ %s ]" % CODE
    return resolve ({ "code" : CODE },path)

def resolve(json, path, url = "https://api.glovoapp.com"):
    req = urllib2.Request(url + path)
    req.add_header('Content-type','application/json')
    req.add_data(dumps(json))
    res = (0,"")
    try:
        call = urllib2.urlopen(req)
        res = (call.getcode(),call.read())
    except urllib2.HTTPError as err:
        res = (err.code,err.reason)
    return res

def from_json(code,json):
    if code >= 200 and code <= 300:
        return loads (json)
    else :
        return { "reason" : json }


if __name__ == '__main__':
    #Register (debug or func) with dump
    code, res = register(TEST_MAIL if DBG else generate_mail())
    user = from_json(code,res)
    print dumps(user, sort_keys=True, indent=4, separators=(',', ': '))

    #Promocode (debug or func) with dump
    code, res = promotion_code(user)
    prmo = from_json(code,res)
    print dumps(prmo, sort_keys=True, indent=4, separators=(',', ': '))
    
