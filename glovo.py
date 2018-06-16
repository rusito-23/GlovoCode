import urllib2
from json import dumps, loads
from mails import generate_mail

DBG       = False
HOW_MANY  = 2
CODES     = ["nolitaglovoco","mostaglovoco"]
TEST_MAIL = "fofibiddas-1600@yopmail.com"
DATA_BASE = "-accounts"

def register(email, path = '/v3/users/customer') :
    print "Registrando [ %s ]" % email
    data = {
        "email":email,
        "password":"qwer1234",
        "name":"man23",
        "preferredLanguage":"es",
        "mediaSource":"Organic Web",
        "mediaCampaign":"Organic Web",
        "privacySettings":["DATA_POLICY"],
        "shownPermissions":["MARKETING_CAMPAIGNS","DATA_POLICY"]
    }
    return resolve (data,path)

def get_token(email,path = '/v3/oauth/token'):
    print "Obteniendo token [ %s ]" % email
    data = {
        "email":email,
        "password":"qwer1234",
        "grantType":"password"
    }
    return resolve (data,path)

def promotion_code(token, path = '/v3/promocodes'):
    print "Pidiendo codigo [ %s ]" % CODES[0]
    return resolve ({ "code" : CODES[0] },path,token)

def resolve(json, path, auth = None, url = "https://api.glovoapp.com"):
    req = urllib2.Request(url + path)
    req.add_header('Content-type','application/json') 
    if auth is not None : 
        req.add_header('Authorization',auth)
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
        return loads (json.decode('utf-8'))
    else :
        return { "reason" : json }


if __name__ == '__main__':
    for i in range(HOW_MANY):
        db = open(CODES[0].replace("glovoco","") + DATA_BASE,"a")
        #Register (debug or func) with dump
        mail = TEST_MAIL if DBG else generate_mail()
        code, res = register(mail)
        user = from_json(code,res)
        #print dumps(user, sort_keys=True, indent=4, separators=(',', ': '))
        #Login/Token de session
        code, res = get_token(mail)
        jtoken = from_json(code,res)
        #print dumps(jtoken, sort_keys=True, indent=4, separators=(',', ': '))
        #Promocode (debug or func) with dump
        code, res = promotion_code(jtoken["token"])
        prmo = from_json(code,res)
        #print dumps(prmo, sort_keys=True, indent=4, separators=(',', ': '))

        if not 'reason' in prmo : 
            print "Resultado : [ %s ]" % prmo["message"]
            db.write(dumps({
                "mail" : mail,
                "pass" : "qwer1234",
                "code" : CODES[0]
                },  
                sort_keys=True, indent=4, separators=(',', ': ')))
        else:
            print "Error de carga !"

    
