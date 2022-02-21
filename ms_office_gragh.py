from office365.graph_client import GraphClient

client = GraphClient(acquire_token_func)

message = client.me.messages.new()  # type: Message
message.subject = "Meet for lunch?"
message.body = "The new cafeteria is open."
message.to_recipients = ["fannyd@contoso.onmicrosoft.com"]

client.me.send_mail(message).execute_query()
