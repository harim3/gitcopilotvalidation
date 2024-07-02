import snowflake.connector
import requests

# Snowflake OAuth configuration
snowflake_account = 'your_account_name'
oauth_client_id = 'your_client_id'
oauth_client_secret = 'your_client_secret'
oauth_token_url = f'https://{snowflake_account}.snowflakecomputing.com/oauth/token-request'

# Get OAuth Access Token
def get_oauth_token():
    data = {
        'grant_type': 'client_credentials',
        'client_id': oauth_client_id,
        'client_secret': oauth_client_secret
    }
    response = requests.post(oauth_token_url, data=data)
    response_data = response.json()
    return response_data['access_token']

# Connect to Snowflake using OAuth token
def connect_to_snowflake(oauth_token):
    conn = snowflake.connector.connect(
        user='<your_snowflake_username>',
        account=snowflake_account,
        authenticator='oauth',
        token=oauth_token
    )
    return conn

if __name__ == "__main__":
    # Get OAuth token
    token = get_oauth_token()

    # Connect to Snowflake using OAuth token
    snowflake_conn = connect_to_snowflake(token)

    # Now, you can use the 'snowflake_conn' object to execute SQL queries or perform other operations.
