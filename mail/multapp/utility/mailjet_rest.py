from mailjet_rest import Client

import os


class SendMailJet:
    api_key = '37d1c2ba02075351cb0c260440711462' # os.environ['MJ_APIKEY_PUBLIC']
    api_secret = '74bdb6cb5a469a99a1da0f1c3dae4df2' # os.environ['MJ_APIKEY_PRIVATE']

    def ussing_mail_jet(self, mail, subject, content_data):
        mailjet = Client(auth=(self.api_key, self.api_secret), version='v3.1')
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": "infomercadigital@gmail.com",
                        "Name": "TOURES BALON"
                    },
                    "To": [
                        {
                            "Email": mail,
                            "Name": content_data['offender_name']
                        }
                    ],
                    "Subject": subject,
                    "TextPart": content_data['body_message']+"! Fecha: "+content_data['date'],
                    "HTMLPart": "<h3>Nos encanta saludarte! "+content_data['offender_name']+" </h3><br><p>"+content_data['body_message']+"</p><br />Fecha !"+content_data['date']
                }
            ]
        }
        result = mailjet.send.create(data=data)
        print(result.status_code)
        print(result.json())