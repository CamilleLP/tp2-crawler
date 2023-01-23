import logging
import requests
import time
from urllib.parse import urljoin
import urllib.robotparser
from urllib.parse import urlparse
from usp.tree import sitemap_tree_for_homepage
from bs4 import BeautifulSoup
import re
import pandas as pd
import urllib.request as r


class Statistiques:

    def __init__(self, urls=[]):
        self.urls = urls

    def download_url(self, url):
        '''
        download_url: downloads a webpage (specified with url argument)
        return an error if the download has failed
        '''
        try:
            # get_url = r.urlopen(url).read()
            get_url = requests.get(url).text
            return get_url
        except Exception:
            logging.exception(f'Failed to get: {url}')

    def find_domain(self, url):
        '''
        find_domain: extract the domain part of an url to get the homepage url
        '''
        scheme = urlparse(url).scheme # http or https
        domain = urlparse(url).netloc # domain name
        url_domain = scheme + '://' + domain + '/'
        return url_domain
    
    def info_crawl(self, url):
        '''
        info_crawl: gives information about a webpage (possibility to crawl 
        and minimum delay to respect between each crawl)
        '''
        url_domain = self.find_domain(url)
        url_robots = url_domain + 'robots.txt'
        infos = {}
        try:
            rp = urllib.robotparser.RobotFileParser()
            rp.set_url(url_robots)
            rp.read()
            infos['is_crawlable'] = rp.can_fetch("*", url)
            infos['min_delay'] = rp.crawl_delay("*")
        except Exception:
            logging.exception(f'Failed to get: {url_robots}')
        finally:
            return infos

    def tokenize_webpage(self, url):
        '''
        tokenize_webpage: extracts content in paragraphs and header tags and tokenize them
        '''
        infos = self.info_crawl(url)
        tokens = []
        if infos and infos['is_crawlable']:
            html = self.download_url(url)
            soup = BeautifulSoup(html, 'html.parser')
            liste_tokens = []
            for i in range(6):
                liste_tokens.append('h' + str(i+1))
            text = ''
            for word in soup.find_all(liste_tokens, recursive=True):
                text += " " + word.text
            text = text.replace("’", "’ ")
            text = re.sub(r'[^\w\s]', '', text)

            tokens = text.split()
        return tokens
    
    def info_tokens(self, url):
        tokens = self.tokenize_webpage(url)
        infos = {}
        infos['count'] = len(tokens)
        len_tokens = 0
        for token in tokens:
            len_tokens += len(token)
        infos['len'] = len_tokens
        return infos

    def nb_docs(self):
        return len(self.urls)

    def infos_tokens_urls(self):
        nb_tokens = 0
        len_tokens = 0
        for url in self.urls:
            infos = self.info_tokens(url)
            nb_tokens += infos['count']
            len_tokens += infos['len']
        infos = {}
        infos['nb_tokens'] = nb_tokens
        infos['avg_len_tokens'] = round(len_tokens / nb_tokens , 3)

        return infos


