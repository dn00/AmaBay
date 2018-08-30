""" EBAY CONFIG
"""
def init_options():
   # Trading API - https://www.x.com/developers/ebay/products/trading-api
    compatability= '967'
    appid= '#'
    certid= '#'
    devid= '#'
    token= ''
   # token isn't valid =P
    return appid, certid, devid, token

#
# if __name__ == "__main__":
#     (opts, args) = init_options()

eBayConfig = {
  "name": "ebay_api_config",
  "api.sandbox.ebay.com": {
    "compatability": 967,
    "appid": "#",
    "certid": "#",
    "devid": "#",
  "token": 
  },
  "api.ebay.com": {
    "compatability": 967,
    "appid": "#",
    "certid": "#",
    "devid": "#",
  "token": 
  },
  "svcs.ebay.com": {
    "appid": "#",
    "version": "1.0.0"
  },
  "open.api.ebay.com": {
    "appid": "#",
    "version": 671
  }
}
