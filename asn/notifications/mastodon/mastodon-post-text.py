import mastodon
from mastodon import Mastodon

m = Mastodon(access_token="CHANGEME", api_base_url="https://mastodon.social")

m.toot("CHANGEME")