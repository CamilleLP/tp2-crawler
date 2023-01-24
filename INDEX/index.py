from bs4 import BeautifulSoup
import re
from INDEX.crawl import Crawl

class Index:

    def __init__(self, urls=[]):
        self.urls = urls

    def tokenize_webpage(self, url):
        '''
        tokenize_webpage: extracts content in paragraphs and header tags and tokenize them
        '''
        crawl = Crawl()
        tokens = []
        html = crawl.download_url(url)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            list_tags = []
            for i in range(6):
                list_tags.append('h' + str(i+1))
            text = ''
            for word in soup.find_all(list_tags, recursive=True):
                text += " " + word.text
            text = re.sub(r"[:«»\"|,.;@#?!&$\[\]\(\)…]", " ", text)
            text = text.replace("’", "' ")
            text = text.replace("'", "' ")
            text = text.lower()
            tokens = text.split()
        return tokens

    def index_page(self, url):
        '''
        index_page create a positional index for only one webpage with given URL
        '''
        tokens = self.tokenize_webpage(url)
        index = []
        if tokens:
            for pos_token in range(len(tokens)):
                new = True
                for token_dict in index:
                    if token_dict['token'] == tokens[pos_token]:
                        token_dict['position'].append(pos_token)
                        new = False
                        break
                if new:
                    new_token = {}
                    new_token['token'] = tokens[pos_token]
                    new_token['position'] = [pos_token]
                    new_token['url'] = url
                    index.append(new_token)
        return index

    def index_total(self, position = True):
        '''
        index_total create a positional index (position = True) or a
        simple one for all webpages (self.urls)
        '''
        index = []
        for url in self.urls:
            index_url = self.index_page(url)
            for token in index_url:
                new = True
                for token_index in index:
                    if token['token'] == token_index['token']:
                        token_index[token['url']] = {}
                        if position:
                            token_index[token['url']]['positions'] = token['position']
                        token_index[token['url']]['nb'] = len(token['position'])
                        new = False
                        break
                if new:
                    new_token = {}
                    new_token['token'] = token['token']
                    new_token[token['url']] = {}
                    if position:
                        new_token[token['url']]['positions'] = token['position']
                    new_token[token['url']]['nb'] = len(token['position'])
                    index.append(new_token)
        return index
                    


                





    
    
    