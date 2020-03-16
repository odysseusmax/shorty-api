import re

class URLValidator:
    def __init__(self):
        ul = '\u00a1-\uffff'  # unicode letters range (must not be a raw string)

        # IP patterns 
        ipv4_re = r'(?:25[0-5]|2[0-4]\d|[0-1]?\d?\d)(?:\.(?:25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}' 
        ipv6_re = r'\[[0-9a-f:\.]+\]'

        # Host patterns 
        hostname_re = r'[a-z' + ul + r'0-9](?:[a-z' + ul + r'0-9-]{0,61}[a-z' + ul + r'0-9])?'
        domain_re = r'(?:\.(?!-)[a-z' + ul + r'0-9-]{1,63}(?<!-))*' # domain names have max length of 63 characters
        tld_re = ( 
            r'\.'                                # dot 
            r'(?!-)'                             # can't start with a dash 
            r'(?:[a-z' + ul + '-]{2,63}'         # domain label 
            r'|xn--[a-z0-9]{1,59})'              # or punycode label 
            r'(?<!-)'                            # can't end with a dash 
            r'\.?'                               # may have a trailing dot 
        ) 
        host_re = '(' + hostname_re + domain_re + tld_re + '|localhost)'

        self.regex = re.compile( 
            r'^(?:http|ftp)s?://' # http(s):// or ftp(s)://
            r'(?:\S+(?::\S*)?@)?'  # user:pass authentication 
            r'(?:' + ipv4_re + '|' + ipv6_re + '|' + host_re + ')' # localhost or ip
            r'(?::\d{2,5})?'  # optional port
            r'(?:[/?#][^\s]*)?'  # resource path
            r'\Z', re.IGNORECASE)
    
    def is_valid(self, url):
        return url is not None and self.regex.search(url)
