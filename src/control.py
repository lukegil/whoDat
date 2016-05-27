import requests
from ua_parser import user_agent_parser


def parse_ua(ua):
    """ Parses a User Agent String
    Params : 
    ua : type - unicode
    ua : about - user agent string from request header

    Return : 
    ua_dict : type - Dictionary
    ua_dict : about - https://github.com/ua-parser/uap-python#retrieve-data-on-a-user-agent-string
    """

    assert isinstance(ua, unicode)
    parsed = user_agent_parser.Parse(ua)
    
    ua_dict = {
        "browser" : parsed["user_agent"]["family"],
        "browser_version" : parsed["user_agent"]["major"],
        "device" : parsed["device"]["brand"],
        "device_model" : parsed["device"]["model"],
        "os" : parsed["os"]["family"],
        "os_v" : parsed["os"]["major"],
        "os_v2" : parsed["os"]["minor"]
        }
    return ua_dict


def get_geo(ip):
    """ Gets a users location
    Params : 
    ip : type - unicode
    ip : about - a user's ip address

    Return : 
    geo_dict : type - Dictionary
    geo_dict : about - a dictionary of city, state, country, and lat-long
    """
    assert isinstance(ip, str)

    try: 
        r = requests.get("http://freegeoip.net/json/{}".format(ip))
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        #API limited to 10k requests/hr
        if (r.status_code == 403):
            return {}
        if (r.status_code == 404):
            return {}

    geo_dict = r.json()
    return geo_dict
