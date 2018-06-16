##17/06 Update (Status : Warn)
Encontre una forma de setear el phoneNumber sin hacer la verificacion
Si uno en el register mete el numero de telefono como otro campo : 
```
{
  "email":"egavetess-0765@yopmail.com",
  "password":"qwer1234",
  "name":"beta",
  "phoneNumber" : { "number" : "+543516465313", "countryCode" : "ES" },
  "preferredLanguage":"es",
  "mediaSource":"Organic Web",
  "mediaCampaign":"Organic Web",
  "privacySettings":["DATA_POLICY"],
  "shownPermissions":["MARKETING_CAMPAIGNS","DATA_POLICY"]
}
```

Aun asi TIENEN OTRO CAMPO QUE DETERMINA SI ESTA VERIFICADO... VERY CLEVER
Si uno hace un 
GET https://api.glovoapp.com/v3/whats_up (token blah blah)

Viene un campo llamado : 
"phoneVerificationRequired" : false | true


##16/06 Update (Status : Warn)
Actualizaron el servidor y los front-end (tanto la app fecha 15/06) como la web.

* Phone BlackList : Ahora algunos telefonos (capaz aquellos que ya se usaron en
otra cuenta) estan en una blacklist la cual no te permite pasar la etapa de verificacion

Con header Authorization = token
Verificacion : https://api.glovoapp.com/v3/users/phonenumber/start_verification
Parametros : 
```
{
	"number":"+543516465313"
}
```
Response : 
```
{
    "error": {
        "userInfo": {},
        "code": "189654",
        "requestId": "PqT01TbX1XYV",
        "domain": "com.glovoapp.core-services",
        "message": "The number you are trying to verify is blacklisted for verification",
        "staticCode": "0"
    }
}
```
###Hipotesis
El punto es que el front-end en las cuentas que no tienen (CREO) asignado un telefono
requiere que se verifique por UNICA vez
Es decir una vez que pasa la etapa de verificacion NO SE VUELVE a verificar. SE GUARDA
Siendo esto cierto habria que setear el phone number BY-PASS-EANDO la verificacion de ser
asi jamas se pediria la verificacion

###Posibles Pruebas : 
Encontre una via para poder modificar el "name" de una cuenta en el endpoint :

https://api.glovoapp.com/v3/users/glv:customer:0b0790b4-76ac-4b1d-b104-1b61626607d1
Y por sorpresa el paquete que envia es : 
```
{  
   "name":"Joaquin Barcena P",
   "email":"joaqbarcena@gmail.com",
   "phoneNumber":{  
      "number":"+543516465313"
   }
}
```
Esto nos da cierta esperanza de la solucion en la api `/v3/users/` hay un modo de subir los cambios no solo del name o del mail, si no del PHONE NUMBER
ahora si nos fijamos bien el path `glv:customer:0b0790b4-76ac-4b1d-b104-1b61626607d1` es un parametro de una request que se pide : 
GET [ Con Authorization : <token> ] -> https://api.glovoapp.com/v3/me
O bien es tambien el resultado despues de un register !
ambos son el mismo json, la key "urn" es el path

Por alguna razon (que obviamente nos estamos perdiendo devuelve lo siguiente)
```
    "error": {
        "userInfo": {},
        "requestId": "UlAUbd3SHf7E",
        "domain": "com.glovoapp.core-services",
        "message": "/v3/users/glv:customer:548374e2-c96f-4b48-b76c-9a89a92986e3 NOT FOUND"
    }
```
Era PUT, pero ahora tira : 
```

    "error": {
        "userInfo": {},
        "requestId": "HjIeya8yCU7h",
        "domain": "com.glovoapp.core-services",
        "id": "789p6lc7m",
        "message": "Error: HjIeya8yCU7h"
    }
```
Al final logre hacer le PUT, recien me habia olvidado de setear el application/json
La buena es que si cambia el nombre, pero el phone NO CAMBIO sigue en estado = null

#API Reverse engineering

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
},

{  
   "id":3497583,
   "type":"Customer",
   "urn":"glv:customer:0b0790b4-76ac-4b1d-b104-1b61626607d1",
   "name":"Joaquin Barcena",
   "picture":null,
   "email":"joaqbarcena@gmail.com",
   "description":null,
   "facebookId":null,
   "preferredCityCode":"COR",
   "preferredLanguage":"es",
   "deviceUrn":null,
   "analyticsId":null,
   "mediaCampaign":"Organic",
   "mediaSource":"Organic",
   "os":null,
   "deliveredOrdersCount":1,
   "phoneNumber":{  
      "number":"+543516465313",
      "countryCode":"ES"
   },
   "companyDetail":null,
   "virtualBalance":{  
      "balance":0.0
   },
   "freeOrders":0,
   "paymentMethod":"CREDIT_CARD",
   "paymentWay":"PER_ORDER",
   "currentCard":null,
   "accumulatedDebt":0.0,
   "defaulter":false
}
```

###Encontramos las demas apis !!
Para todas fue necesario el header
Content-type : application/json
Para la del promocodes tambien requerimos 
Authorization : <token> (Obtenido luego del login)

###Login
https://api.glovoapp.com/v3/oauth/token
Parametros :
```
{
	"grantType":"password",
	"email":"egavetess-0765@yopmail.com",
	"password":"qwer1234"
}
```
Respuesta : 
```
{
	"token" : "<token>"
}
```

###Promocodes
https://api.glovoapp.com/v3/promocodes
Parametros : 
```
{
	"code":"mostaglovoco"
}
```
Respuesta : 
```
<No la recuerdo jaja salu3>
```



