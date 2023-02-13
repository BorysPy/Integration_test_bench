from bynder_sdk import BynderClient

#When using OAuth2, create an instance of the client and use the flow to receive a token:
bynder_client = BynderClient(
    domain='portal.getbynder.com',
    redirect_uri='https://...',
    client_id='',
    client_secret='',
    token_saver=token_saver
)

print(bynder_client.get_authorization_url())
code = input('Code: ')
bynder_client.fetch_token(code)

#When using a permanent token, the client instance can be created like this:
bynder_client = BynderClient(
  domain='portal.getbynder.com',
  permanent_token=''
)

#Finally call one of the API's endpoints through one of the clients:
asset_bank_client = bynder_client.asset_bank_client
media_list = asset_bank_client.media_list({
    'limit': 2,
    'type': 'image'
})