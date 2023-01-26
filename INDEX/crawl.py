import logging
import requests

class Crawl:

    def __init__(self, urls=[]):
        self.urls = urls

    def download_url(self, url):
        '''
        download_url: downloads a webpage (specified with url argument)
        return an error if the download has failed
        '''
        res = None
        try:
            get_url = requests.get(url, timeout=2, verify=False)
            # timeout = 2 avoid to loose time if the connection is impossible
            # verify=False resolve problem of certificate in some cases
            if get_url.status_code == 200:
                res = get_url.text
            return res
        except Exception:
            logging.exception(f'Failed to get: {url}')