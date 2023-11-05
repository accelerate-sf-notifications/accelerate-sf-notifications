from mastodon import Mastodon, MastodonAPIError
import time

# Initialize the API with your access token, client_id, and client_secret
mastodon = Mastodon(
    client_id='CHANGEME',
    client_secret='CHANGEME',  # You need to include the client_secret here
    access_token='CHANGEME',
    api_base_url='https://mastodon.social'
)

# Upload the media
media = mastodon.media_post('./twitter_demo.mp4', 'video/mp4')

# Initialize variables for retry logic
max_retries = 10  # Maximum number of retries
retry_count = 0   # Current retry count
wait_time = 10    # Time to wait between retries in seconds
posted = False    # Flag to check if the post was successful

# Retry loop
while not posted and retry_count < max_retries:
    try:
        # Attempt to post the status
        mastodon.status_post('Your status message', media_ids=[media['id']])
        posted = True
    except MastodonAPIError as e:
        # Print out the contents of the error to understand its structure
        print(e)
        print(vars(e))

        # Check if the error message contains 'processing'
        if 'processing' in str(e):
            # If media is still processing, wait and then try again
            print(f"Media not processed yet, waiting {wait_time} seconds. Retry {retry_count + 1}/{max_retries}.")
            time.sleep(wait_time)
            retry_count += 1
        else:
            # If there is a different error, raise it
            raise

# Check if the post was successful
if posted:
    print("Status posted successfully.")
else:
    print("Failed to post status after retries.")
