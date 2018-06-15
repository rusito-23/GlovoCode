
###Url de la api de users
https://api.glovoapp.com/v3/users/customer

###Objeto json a enviar en el post
Notese que no hay manejos de tokens en la creacion de usuarios
```
{
	"email":"egavetess-0765@yopmail.com",
	"password":"qwer1234",
	"name":"beta",
	"preferredLanguage":"es",
	"mediaSource":"Organic Web",
	"mediaCampaign":"Organic Web",
	"privacySettings":["DATA_POLICY"],
	"shownPermissions":["MARKETING_CAMPAIGNS","DATA_POLICY"]
}
```

Respuesta posible esperada
```
{
	"id":3518135,
	"type":"Customer",
	"urn":"glv:customer:548374e2-c96f-4b48-b76c-9a89a92986e3",
	"name":"beta",
	"picture":null,
	"email":"egavetess-0765@yopmail.com",
	"description":null,
	"facebookId":null,"
	preferredCityCode":null,
	"preferredLanguage":"es",
	"deviceUrn":null,
	"analyticsId":null,
	"mediaCampaign":"Organic Web",
	"mediaSource":"Organic Web",
	"os":null,
	"deliveredOrdersCount":0,
	"phoneNumber":null,
	"companyDetail":null,
	"virtualBalance":{"balance":0.0},
	"freeOrders":0,
	"paymentMethod":"CREDIT_CARD",
	"paymentWay":"PER_ORDER",
	"currentCard":null,
	"accumulatedDebt":0.0,
	"defaulter":false
}
```