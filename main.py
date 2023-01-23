from INDEX import statistiques
import pandas as pd

if __name__ == '__main__':
    df = pd.read_json("crawled_urls.json")   
    urls = list(df[0])
    urls = urls[0:10]
    # print(urls)
    s = statistiques.Statistiques(urls=urls)
    # print(s.download_url(urls[1]))
    nb_docs = s.nb_docs()
    infos = s.infos_tokens_urls()
    print(nb_docs)
    print(infos)