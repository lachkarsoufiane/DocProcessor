import re

TITLE_RE = re.compile(r'[A-Z][a-zA-Z -]+(?=:$)')

MANUFACTURE_RE = re.compile(r'[^ ,][a-zA-Z!@#$&()\\-`+\’ ]+\([a-zA-Z]+\)')

CERTIFICATE_RE = re.compile(r'\d{2,3}[A-Z](?:[rev]{3}\d)?(?=, )')

EXTRA_RE = re.compile(r'(Extension|Revision): [a-zA-Z. ]+')

REVISION_RE = re.compile(r'rev\d{1}')

URL_RE = re.compile(r'^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\/')

DSCC_TITLES_RE = re.compile(r'[A-Z][a-zA-Z ]+(?=:)')