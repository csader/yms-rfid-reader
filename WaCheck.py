__author__ = 'Chris Sader, chris.sader@gmail.com'

import WaApi
import urllib.parse
import json
import csv
import os


def get_badge_ids():
    params = {'$filter': 'badge ne NULL',
              '$async': 'false',
              '$select': 'badge,tools'
              }
    request_url = contactsUrl + '?' + urllib.parse.urlencode(params)
    print(request_url)
    return api.execute_request(request_url).Contacts


# How to obtain application credentials: https://help.wildapricot.com/display/DOC/API+V2+authentication#APIV2authentication-Authorizingyourapplication
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
api_key = os.environ['API_KEY']

api = WaApi.WaApiClient(client_id, client_secret, api_key)
api.authenticate_with_contact_credentials("ADMINISTRATOR_USERNAME", "ADMINISTRATOR_PASSWORD")
accounts = api.execute_request("/v2/accounts")
account = accounts[0]

print(account.PrimaryDomainName)

contactsUrl = next(res for res in account.Resources if res.Name == 'Contacts').Url


# get members with Badge IDs in the system and print them
contacts = get_badge_ids()

# create obj out of response. Ref: https://app.swaggerhub.com/apis-docs/WildApricot/wild-apricot_public_api/2.1.0#/Contacts/GetContactsList
obj = {}
with open('contacts.json', 'w') as outfile:
    for contact in contacts:
        obj[contact.Id] = {
            "firstName": contact.FirstName,
            "lastName": contact.LastName,
            "email": contact.Email,
        }
        for field in contact.FieldValues:
            if field.Value is not None:
                if field.FieldName == 'badge':
                    obj[contact.Id]["badgeId"] = field.Value
                else:
                    if isinstance(field.Value, list):
                        obj[contact.Id]["tools"] = []
                        for tool in field.Value:
                            obj[contact.Id]["tools"].append({
                                "id": tool.Id,
                                "label": tool.Label
                            }) 

# save object to json file
with open('contacts.json', 'w') as outfile:
    json.dump(obj, outfile, indent=4)

# verify the data was saved
with open('contacts.json') as json_file:
    data = json.load(json_file)
    print(data)
