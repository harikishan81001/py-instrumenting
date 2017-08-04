from __future__ import absolute_import

import requests

from httplogger.utils.compat import string_types
from httplogger.transports.base import Transport
from httplogger.utils.http import urlopen
from httplogger.utils.compat import urllib2
from httplogger.utils import defaults


class HTTPTransport(Transport):
    scheme = ['sync+http', 'sync+https']

    def __init__(
            self, parsed_url, timeout=defaults.TIMEOUT,
            verify_ssl=False):
        self._url = parsed_url
        self.timeout = timeout
        self.verify_ssl = verify_ssl

    def send(self, data, headers):
        """
        Sends a request to a remote webserver using HTTP POST.
        """
        try:
	    response = requests.post(
                self._url,
		data=body,
		headers=headers)
            return response
        except urllib2.HTTPError as exc:
            print exc
