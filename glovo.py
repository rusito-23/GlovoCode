from json import dumps, loads
from mails import generate_mail
from requests import post

DBG       = False
CODE      = "nolitaglovoco"
TEST_MAIL = "fofibiddas-1600@yopmail.com"

def register(email, path="/v3/users/customer"):
    print ("Registrando [ %s ]" % email)
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
    return resolve(data, path)

def promotion_code(path="/v3/promocodes"):
    print ("Pidiendo codigo [ %s ]" % CODE)
    data = {"code": CODE}
    return resolve(data, path)

def resolve(data, path, url="https://api.glovoapp.com"):
    headers = {'content-type': 'application/json'}
    res = post(url + path, data=dumps(data), headers=headers)
    code, reason, json = res.status_code, res.reason, loads(res.text)
    if code >= 200 and code <= 300:
        print ("Petición exitosa: "+str(code)+" : "+reason)
        return res
    if json["error"]["message"] == "Email already exists" :
        print ("El email ya existe: "+str(code)+" : "+reason)
        return -1
    else:
        print ("Error: "+str(code)+" : "+reason)
        return 0

if __name__ == '__main__':
    user = register(TEST_MAIL if DBG else generate_mail())
    user = login(user)
