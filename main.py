import pandas as pd
from INDEX.statistics import Statistics
from INDEX.index import Index
from INDEX.crawl import Crawl
import argparse

if __name__ == '__main__':
    # configure arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("crawled_urls", help = "name of the file containing the URLs")
    parser.add_argument("--type", help = "type of index: positional or classic (classic by default)")
    parser.add_argument("--url_name", help = "if True, create an index with URLs \
        names instead of URLs indexes (False by default)")
    parser.add_argument("--use_stemmer", help = "if True, use stemmer on tokens (False by default)")
    parser.add_argument("--tags", help = "Tags used to construct the index, only accept:\
         title, p, h1, h2, h3, h4, h5, h6 (title by default)")


    # extract arguments given by user
    args = parser.parse_args()
    urls_file = args.crawled_urls

    if args.type and args.type.lower() == 'positional':
        positional = True
    else:
        positional = False
    
    if args.url_name and args.url_name.lower() == 'true':
        url_name = True
    else:
        url_name = False

    if args.use_stemmer and args.use_stemmer.lower() == 'true':
        use_stemmer = True
    else:
        use_stemmer = False

    if args.tags and args.tags.lower() in ['title', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        tags = args.tags.lower()
    else:
        tags = 'title'

    # import crawled URLs
    df = pd.read_json(urls_file)   
    urls = list(df[0])

    # compute statistics
    stats = Statistics(urls)
    infos = stats.stats_urls()

    # construct index
    index = Index(urls)
    res = index.index_total(position=positional, url_name=url_name, use_stemmer=use_stemmer, tags=tags)

    print(infos)
    print(res)