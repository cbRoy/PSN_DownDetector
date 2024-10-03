import requests

'''
Country codes and matching region code

country	"AR|BO|BR|CA|CL|CO|CR|EC|GT|HN|NI|MX|PA|PE|PY|SV|US|UY"
region	"SCEA"

country	"AE|AT|AU|BE|BG|BH|CH|CY|CZ|DE|DK|ES|FI|FR|GB|GR|HR|HU|IE|IL|IN|IS|IT|KW|LB|LU|MT|NL|NO|NZ|OM|PL|PT|QA|RO|RU|SA|SE|SI|SK|TR|UA|ZA"
region	"SCEE"

country	"CN|HK|ID|JP|KR|MY|PH|RS|SG|TH|TW|VN"
region "SCEJA"
'''



response = requests.get("https://status.playstation.com/data/statuses/region/SCEA.json")
data = response.json()

# if everything is running, an empty status array is returned

# if there is an outage in one particular country within a region
# statusType will be 'Outage' and would require checking the returned devices affected and their locale
# not really interested in doing that right now as there's no reliable way of testing unless some service is actually out somewhere

if not data['status'] : 
    print ("All services up and running!")
else :
    #lookup table for comparing part of messageKey
    networks = {"accountManagement":"Account Management",
                "gamingAndSocial":  "Gaming And Social",
                "playStationStore": "PlayStation Store",
                "playStationVideo": "PlayStation Video",    #not sure if this is correct as i guess russia doesn't have ps video or direct
                "playStationDirect": "PlayStation Direct"}
    
    for status in data['status']:
        type = status['statusType']
        service = status['message']['messageKey'].split('.')[1]
        locale = status['devices'][0]['deviceLocalized'][0]['locale']
        print(networks[service] + ":\t" + type + "\t" + locale)

        #so far have only been able to test this with Russia (region: SCEE) at the moment.
        #Not sure how the response looks if there are more locales within the region with outages 

        
# Can check a specific country by country code. Much more reliable way of seeing if the networks are down in your area
# be sure to change the request region .json

for country in data['countries']:
    if country['countryCode'] == "US" :
        for service in country['services']:
            print(service['serviceName'] + ":\t" + ("Up!" if not service['status'] else "Down :("))