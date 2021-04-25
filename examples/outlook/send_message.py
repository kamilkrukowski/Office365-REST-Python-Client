from examples import acquire_token_client_credentials
from office365.graph_client import GraphClient
from tests import test_user_principal_name, test_user_principal_name_alt

client = GraphClient(acquire_token_client_credentials)
message_json = {
    "Message": {
        "Subject": "Meet for lunch?",
        "Body": {
            "ContentType": "Text",
            "Content": "The new cafeteria is open."
        },
        "ToRecipients": [
            {
                "EmailAddress": {
                    "Address": test_user_principal_name_alt
                }
            }
        ]
    },
    "SaveToSentItems": "false"
}
target_user = client.users[test_user_principal_name]
target_user.send_mail(message_json).execute_query()
