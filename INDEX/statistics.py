from INDEX.index import Index
import json

class Statistics:

    def __init__(self, urls = None):
        self.urls = urls

    def stats_one_url(self, url):
        '''
        stats_url: return statistics on tokens of a specific webpage
        defined by its URL
        '''
        # tokenization
        index = Index(self.urls)
        tokens = index.tokenize_title(url)
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
        infos['number of documents'] = len(self.urls)
        # total number of tokens
        infos['number of tokens'] = nb_tokens
        # average number of tokens token
        infos['average number of tokens per document'] = round(nb_tokens / len(self.urls) , 3)
        # average length of tokens in documents
        infos['average length of tokens (in all documents)'] = round(len_tokens / nb_tokens , 3)
        # top 10 of most frequent tokens
        top = {}
        max_top = min(len(list(count_final.keys())), 10)
        for token in list(count_final.keys())[0:max_top]:
            top[token] = count_final[token]
        infos['top of most frequent tokens'] = top

        res_json = json.dumps(infos, indent = 4, ensure_ascii=False)

        with open('metadata.json', "w") as outfile:
            outfile.write(res_json)

        return infos


