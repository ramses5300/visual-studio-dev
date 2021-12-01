import msal
from office365.graph_client import GraphClient

def acquire_token():
    """
    Acquire token via MSAL
    """
    authority_url = 'https://login.microsoftonline.com/{tenant_id_or_name}'
    app = msal.ConfidentialClientApplication(
        authority=authority_url,
        client_id='{client_id}',
        client_credential='{client_secret}'
    )
    token = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
    return token


client = GraphClient(acquire_token)
