"""
Configuration reading
"""
from rcfile import rcfile

class ConfigurationError(Exception):
    """
    Raised when something is wrong with the config,
    such as missing settings.
    """
    pass

required = [
    "host",
    "port",
    "protocol"
]

CONFIG = rcfile("viewser")
print(CONFIG)

for rq in required:
    try:
        CONFIG[rq]
    except KeyError as key_err:
        e = f"Value for required setting \"{rq}\" not provided"
        raise ConfigurationError(e) from key_err

BASE_URL = f"{CONFIG['protocol']}://{CONFIG['host']}:{CONFIG['port']}"
