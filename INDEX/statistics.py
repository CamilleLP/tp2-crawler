from INDEX.index import Index

class Statistics:

    def __init__(self, urls=[]):
        self.urls = urls

    def stats_one_url(self, url):
        '''
        stats_url: return statistics on tokens of a specific webpage
        defined by its URL
        '''
        # tokenization
        index = Index()
        tokens = index.tokenize_webpage(url)
        infos = {}
        # number of tokens
        infos['count'] = len(tokens)
        # len_tokens = lenght of all tokens together 
        # (used after to compute average lenght of tokens)
        len_tokens = 0
        # count_tokens = dict with frequency of each token
        count_tokens = {}
        for token in tokens:
            len_tokens += len(token)
            if token in count_tokens.keys():
                count_tokens[token] += 1
            else:
                count_tokens[token] = 1
        infos['count_tokens'] = count_tokens
        infos['len'] = len_tokens
        return infos

    def stats_urls(self):
        '''
        stats_url: return statistics on tokens of several webpages
        defined by their URL (self.urls)
        '''
        # total number of tokens
        nb_tokens = 0
        # total length of all tokens together
        len_tokens = 0
        # frequency of each token
        count_tokens = {}
        for url in self.urls:
            infos = self.stats_one_url(url)
            nb_tokens += infos['count']
            len_tokens += infos['len']
            count = infos['count_tokens']
            for key in count.keys():
                if key not in count_tokens:
                    count_tokens[key] = count[key]
                else:
                     count_tokens[key] += count[key]
        count_final = dict(sorted(count_tokens.items(), key=lambda item: item[1], reverse=True))
        # return final results in a dictionnary
        infos = {}
        # number of docs
        infos['nb_docs'] = len(self.urls)
        # total number of tokens
        infos['nb_tokens'] = nb_tokens
        # average token
        infos['avg_len_tokens'] = round(len_tokens / nb_tokens , 3)
        # top 10 of most frequent tokens
        infos['count_tokens'] = list(count_final.keys())[0:10]
        return infos


