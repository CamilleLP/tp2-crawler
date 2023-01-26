from bs4 import BeautifulSoup
import re
import json
from INDEX.crawl import Crawl

class Index:

    def __init__(self, urls):
        self.urls = urls

    def tokenize_webpage(self, url):
        '''
        tokenize_webpage: extracts content in paragraphs and header tags and tokenize them
        '''
        crawl = Crawl()
        tokens = []
        html = crawl.download_url(url)
        if html:
            # extract title of the webpage
            soup = BeautifulSoup(html, 'html.parser')
            text = ''
            for word in soup.find_all("title", recursive=True):
                text += " " + word.text
            
            # handle special characters
            text = re.sub(r"[:«»\"|,.;@#?!&$\[\]\(\)…]", " ", text)
            text = text.replace("’", "' ")
            text = text.replace("'", "' ")
            text = text.lower()

            # tokenization
            tokens = text.split()
        return tokens

    def index_page(self, url):
        '''
        index_page create a positional index for only one webpage with a given URL
        '''
        tokens = self.tokenize_webpage(url)
        index = {}
        if tokens:
            for pos_token in range(len(tokens)):
                new = True # indicate if the token is new or not
                for token_dict in list(index.keys()):
                    # if it is not (it has already appeared in the title), then
                    # add the position to the existant list:
                    if token_dict == tokens[pos_token]:
                        index[token_dict][url]['positions'].append(pos_token)
                        new = False
                        break
                # if it is the first time that the word appear, then
                # initialise new dictionnary and give the first position
                if new:
                    index[tokens[pos_token]] = {}
                    index[tokens[pos_token]][url] = {}
                    index[tokens[pos_token]][url]['positions'] = [pos_token]
        return index

    def index_total(self, position = True):
        '''
        index_total create a positional index (position = True) or a
        simple one for all webpages (self.urls)
        '''
        index = {}
        for url in self.urls:
            index_url = self.index_page(url)
            for token in list(index_url.keys()):
                new = True
                for token_index in list(index.keys()):
                    # if the token has already appeared for another webpage, 
                    # then add url, position and count
                    if token == token_index:
                        index[token_index][url] = {}
                        if position:
                            index[token_index][url]['positions'] = index_url[token][url]['positions']
                        index[token_index][url]['count'] = len(index_url[token][url]['positions'])
                        new = False
                        break
                if new:
                    # if it has not appeared, then instanciate a new token with url, 
                    # position and count
                    index[token] = {}
                    index[token][url] = {}
                    if position:
                        index[token][url]['positions'] = index_url[token][url]['positions']
                    index[token][url]['count'] = len(index_url[token][url]['positions'])
        
        # write the result in a json file
        res_json = json.dumps(index, indent = 4, ensure_ascii=False)
        if position:
            file_name = 'title.pos_index.json'
        else:
            file_name = 'title.non_pos_index.json'

        with open(file_name, "w") as outfile:
            outfile.write(res_json)
        return index
                    


                





    
    
    