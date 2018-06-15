from json import dumps, loads
from mails import generate_mail
from requests import post

DBG       = False
CODE      = "nolitaglovoco"
TEST_MAIL = "iandruskiewitsch854@famaf.unc.edu.ar"

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
    (code, reason, json) = resolve(data, path)
    try:
        msg = json["error"]["message"]
        if msg == "Email already exists":
            print ("El email ya existe: "+str(code)+" : "+reason)
            return 0
        else:
            return 1
    except KeyError:
        return email

def promotion_code(token, path="/v3/promocodes"):
    print ("Pidiendo codigo [ %s ]" % CODE)
    data = {"code": CODE}
    return resolve(data, path, auth=token)

def login(email, path="/v3/oauth/token"):
    print ("Loggeando [ %s ]" % email)
    data = {
        "grantType":"password",
        "email":email,
        "password":"qwer1234"
    }
    (code, reason, json) = resolve(data, path)
    return json["token"]

def resolve(data, path, auth=False, url="https://api.glovoapp.com"):
    headers = {'content-type': 'application/json'}
    if auth:
        headers['Authorization'] = auth
    res = post(url + path, data=dumps(data), headers=headers, )
    code, reason, json = res.status_code, res.reason, loads(res.text)
    return (code, reason, json)

if __name__ == '__main__':
    user = register(TEST_MAIL if DBG else generate_mail())
    if user != 0:
        (code, reason, json) = promotion_code(login(user))
        try:
            print(json['message'])
        except KeyError:
            print ("Error al cargar el código")
            print(json)
