import json
from office365.runtime.auth.user_credential import UserCredential
from office365.runtime.http.request_options import RequestOptions
from office365.sharepoint.client_context import ClientContext
site_url = "https://{your-tenant-prefix}.sharepoint.com"
ctx = ClientContext(site_url).with_credentials(UserCredential("{username}", "{password}"))
request = RequestOptions("{0}/_api/web/".format(site_url))
response = ctx.execute_request_direct(request)
json = json.loads(response.content)
web_title = json['d']['Title']
print("Web title: {0}".format(web_title))
