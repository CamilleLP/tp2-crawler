import pandas as pd
from INDEX.statistics import Statistics
from INDEX.index import Index
from INDEX.crawl import Crawl
import argparse

if __name__ == '__main__':
    # configure arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("crawled_urls", help = "name of the file containing the URLs")
    parser.add_argument("--type", help = "type of index: positional or classic")

    # extract arguments given by user
    args = parser.parse_args()
    urls_file = args.crawled_urls
    if args.type:
        if args.type == 'positional':
            positional = True
        elif args.type == 'classic':
            positional = False
        else:
            print("Incorrect argument for type: it will compute classic index by default")
            positional = False
    else:
        positional = False
    
    df = pd.read_json(urls_file)   
    urls = list(df[0])

    stats = Statistics(urls)
    infos = stats.stats_urls()

    index = Index(urls)
    res = index.index_total(position=positional)

    print(infos)
    print(res)