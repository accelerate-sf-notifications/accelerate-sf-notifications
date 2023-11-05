import sys
sys.path.append('../../')
import config

import mastodon
from mastodon import Mastodon

m = Mastodon(access_token=config.vars["mastodon"]["access_token"], api_base_url=config.vars["mastodon"]["api_base_url"])
m.toot(config.vars["mastodon"]["text"])
