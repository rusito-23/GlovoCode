import urllib2
tagToMatch = 'id="login"'
valueTag = "value="
valueSize = len(valueTag) + 1
yopMailUrl = "http://www.yopmail.com/es/email-generator.php"
contents = urllib2.urlopen(yopMailUrl).readlines()
for line in contents :
	if tagToMatch in line :
		line = line[line.index(valueTag) + valueSize : -5].replace("&#64;","@")
		print line




'''

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