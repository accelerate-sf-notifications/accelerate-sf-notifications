import sys
sys.path.append('../../')
import config

from mastodon import Mastodon, MastodonAPIError
import time

# Initialize the API with your access token, client_id, and client_secret
mastodon = Mastodon(
    client_id=config.vars["mastodon"]["client_id"],
    client_secret=config.vars["mastodon"]["client_secret"],
    access_token=config.vars["mastodon"]["access_token"],
    api_base_url=config.vars["mastodon"]["api_base_url"]
)

# Upload the media
media = mastodon.media_post(config.vars["mastodon"]["video_filename"], config.vars["mastodon"]["video_filetype"])

# Initialize variables for retry logic
max_retries = 10  # Maximum number of retries
retry_count = 0   # Current retry count
wait_time = 10    # Time to wait between retries in seconds
posted = False    # Flag to check if the post was successful

# Retry loop
while not posted and retry_count < max_retries:
    try:
        # Attempt to post the status
        mastodon.status_post(config.vars["mastodon"]["video_status"], media_ids=[media['id']])
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
