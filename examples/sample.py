# This file was generated by liblab | https://liblab.com/

from postman_restapi import PostmanRestapi, Environment

sdk = PostmanRestapi(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
)

result = sdk.billing.get_accounts()

print(result)
