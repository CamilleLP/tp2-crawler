import pandas as pd
from INDEX import statistics
from INDEX import index

if __name__ == '__main__':
    df = pd.read_json("crawled_urls.json")   
    urls = list(df[0])
    sample_urls = urls[0:20]

    # compute statistics
    s = statistics.Statistics(urls=sample_urls)
    stats  = s.stats_urls()
    print('nb docs', stats['nb_docs'], "\n")
    print('nb tokens', stats['nb_tokens'], "\n")
    print('average token', stats['avg_len_tokens'], "\n")
    print('frequency of tokens', stats['count_tokens'], "\n")

    # compute simple index
    i = index.Index(urls=sample_urls)
    simple_index = i.index_total(position=False)
    for elem in simple_index:
        print(elem, '\n')

    # compute positional index
    i = index.Index(urls=sample_urls)
    simple_index = i.index_total(position=True)
    for elem in simple_index:
        print(elem, '\n')



    # print(urls)
    
    # infos = s.info_tokens(urls[0])
    # print(infos['count_tokens'])
    # print(infos['count'])
    # print(infos['len'])
    # print(s.download_url(urls[1]))
    # nb_docs = s.nb_docs()
    # infos = s.infos_tokens_urls()
    # print(nb_docs)
    # print(infos)




    # i = index.Index()
    # tokenized = i.tokenize_webpage(url)
    # print(tokenized)
    # index_page = i.index_page(url)
    # print(index_page)



    # df = pd.DataFrame()
    # token_list = []
    # token_pos = []
    # for token in index_page:
    #     token_list.append(token['token'])
    #     len_token = len(token['position'])
    #     token_pos.append(len_token)
    # df['token'] = token_list
    # df['order'] = token_pos
    # df2 = df.sort_values(by='order', ascending=False)
    # print(df2.head(10))
