import requests
import json
from mails import generate_mail

def register(email):
    print("REGISTRANDO USUARIO: %s" % email)
    url = "https://api.glovoapp.com/v3/users/customer"
    headers = {'content-type': 'application/json'}
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

    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(r.status_code, r.reason)
    return r

def promotion_code(user):
    print("PIDIENDO CODIGO: NOLITAGLOVOCO")

    url = "https://api.glovoapp.com/v3/promocodes"
    headers = {'content-type': 'application/json'}
    data = {"code":"nolitaglovoco"}

    r = requests.post(url,
            data=json.dumps(data),
            headers=headers,
            cookies=user.cookies)
    print(r.status_code, r.reason)
    print(r.text)

if __name__ == '__main__':
    user = register(generate_mail())
    promotion_code(user)
