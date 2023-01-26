# tp2-crawler

## Description
This project can be used to construct an index on titles of URLs given in input. *crawled_urls.json* is an example for the file containing the URL (input).
The titles are first extract from the html file corresponding to each url. Then, the titles are splited in tokens. Each token is finally used to construct the index.
The user can choose between a positional index or a simple index. Moreover, it is possible to create an index with URL names or with URL indexes (position of URLs in the URLs file).

## Contributors
Camille Le Potier

## Requirements
Python 3.8

## Installation
```shell
git clone https://github.com/CamilleLP/tp2-index.git
cd tp2-index
pip3 install -r requirements.txt
```

## Launch the index creation
The user must provide the file containing the URLs (*crawled_urls.json* for example).

## Example without optionnal arguments:

The example below create a non positional index with URLs listed in *crawled_urls.json* file
```shell
python3 main.py "crawled_urls.json"
```

The corresponding index is printed on the terminal and saved in ***title.non_pos_index.json***

## Examples with optionnal arguments:

### Use of **--type** argument:
It is possible to compute a positional index instead with optional argument **--type**.
The example below create a positional index with URLs listed in *crawled_urls.json* file.
```shell
python3 main.py "crawled_urls.json" --type positional
```

The corresponding index is printed on the terminal and saved in ***title.pos_index.json***

**--type classic** compute a non positional index (classic)

### Use of **--url_name** argument:
It is also possible to create an index with either URL names or URL indexes with **--url_name**.
The example below create a positional index with URL names instead of URL indexes listed in *crawled_urls.json* file.
```shell
python3 main.py "crawled_urls.json" --type positional --url_name true
```
The corresponding index is printed on the terminal and saved in ***title.non_pos_index.json***

### Use of **--use_stemmer** argument:
**--use_stemmer = true** uses a stemmer on tokens.
The example below create a non positional index of URL names listed in *crawled_urls.json* file and use a stemmer on the tokens.
```shell
python3 main.py "crawled_urls.json" --use_stemmer true
```
The corresponding index is printed on the terminal and saved in ***mon_stemmer.title.non_pos_index.json***

### Use of **--tags** argument:
**--tags** change the tags on which the index is constructed. Tags used by default are ***title***
The example below create a non positional index on paragraphs **p** (instead of titles) of URL names listed in *crawled_urls.json* file 
```shell
python3 main.py "crawled_urls.json" --tags p
```
The corresponding index is printed on the terminal and saved in ***p.non_pos_index.json***


For more information about arguments:
```shell
python3 main.py -h
```

## Launch tests

### Launch tests on index:

```shell
python3 -m unittest TESTS/test_index.py
```

### Launch tests on statistics:
```shell
python3 -m unittest TESTS/test_statistics.py
```