"""
Marks all items (messages) in folder as read
"""

from office365.graph_client import GraphClient
from tests import test_client_id, test_password, test_tenant, test_username

client = GraphClient(tenant=test_tenant).with_username_and_password(
    test_client_id, test_username, test_password
)
client.me.mail_folders["Inbox"].mark_all_items_as_unread().execute_query()
print("All messages marked as read")
