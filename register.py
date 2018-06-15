import requests

url = "https://api.glovoapp.com/v3/users/customer"
data = {
    "email":"egavetess-0765@yopmail.com",
    "password":"qwer1234",
    "name":"beta",
    "preferredLanguage":"es",
    "mediaSource":"Organic Web",
    "mediaCampaign":"Organic Web",
    "privacySettings":["DATA_POLICY"],
    "shownPermissions":["MARKETING_CAMPAIGNS","DATA_POLICY"]
}

r = requests.post(url, data=data)

print(r.status_code, r.reason)
print(r.text)
