<<<<<<< HEAD
from postman import Postman, Environment

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
=======
# This file was generated by liblab | https://liblab.com/

from postman import Postman, Environment

sdk = Postman(
>>>>>>> 95da91c (initial commit)
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
)

result = sdk.billing.get_accounts()

print(result)
