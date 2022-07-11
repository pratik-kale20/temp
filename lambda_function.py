import os
import requests
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore

url = "https://api.interakt.ai/v1/public/message/"

def lambda_handler(event, context):
    visitorId = str(request.args['visitorId'])
    visitorMobile = str(request.args['vMob'])
    visitorNameb = str(request.args['vName'])
    empName = str(request.args['eName'])
    cars_ref = data.collection(u'visitors')
    docs = cars_ref.stream()
    visitors_list = []
    for doc in docs:
        if(doc.id == visitorId):
            if(doc.to_dict()['status'] == 'pending'):
                try:
                    payload = json.dumps({
                    "countryCode": "+91",
                    "phoneNumber": visitorMobile,
                    "callbackData": "Error message",
                    "type": "Template",
                    "template": {
                        "name": "denymsg",
                        "languageCode": "en",
                        "bodyValues": [
                            visitorNameb,
                            empName
                        ]
                    }
                    }
                    )
                    apikey = os.environ['apikey']
                    headers = {
                    'Authorization': 'Basic '+ apikey,
                    'Content-Type': 'application/json'
                    }
                    response = requests.request("POST", url, headers=headers, data=payload)

                    return {
                        'statusCode': 200,
                            'headers': {
                            'Access-Control-Allow-Headers': 'Content-Type',
                            'Access-Control-Allow-Origin': '*',
                            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                            },
                            'body': str(response.text)
          
                    }
                except:
                    return   {
                        'statusCode': 200,
                        'body': json.dumps('Please Try Again!')
                    }


      