PORT = 443

# name -> secret (32 hex chars)
USERS = {
    "tg":  "65e4b057b44a07fad14d660ee4a5d201"
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "habr.com"

# Tag for advertising, obtainable from @MTProxybot
AD_TAG = "0855c56d9efcd6e464438060934426fb"
