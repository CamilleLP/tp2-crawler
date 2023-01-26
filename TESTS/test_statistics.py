from unittest import TestCase
from INDEX.statistics import Statistics

class TestStatistics(TestCase):
    def test_stats_one_url(self):
        '''
        check that results return by stats_one_url are consistents for one url
        '''
        # GIVEN
        ref_url = 'https://ensai.fr'
        # content_title = 'Ecole d\'ingénieur statistique, data science et big data | ENSAI Rennes'
        
        # we can count 11 tokens (by splitting with blank space)
        # data is present 2 times
        # the other tokens are only present once
        count = 11
        count_data = 2
        count_other = 1

        # WHEN
        stats = Statistics()
        res = stats.stats_one_url(ref_url)

        # THEN
        self.assertEqual(res['count'], count)
        self.assertEqual(res['count_tokens']['data'], count_data)
        for token in list(res['count_tokens'].keys()):
            if token != 'data':
                self.assertEqual(res['count_tokens'][token], count_other)

    def test_stat_urls(self):
        '''
        check that stat_urls results are consistent
        '''
        # GIVEN
        ref_url1 = 'https://ensai.fr'
        # content_title1 = 'Ecole d\'ingénieur statistique, data science et big data | ENSAI Rennes'

        ref_url2 = 'https://fr.wikipedia.org/wiki/Karine_Lacombe'
        # content_title1 = 'Karine Lacombe — Wikipédia'

        urls = [ref_url1, ref_url2]
        
        nb_tokens = 15 # 11 tokens in ref_url1 and 4 in ref_url2 without punctuation
        nb_docs = 2
        avg_tok = round(nb_tokens/nb_docs, 3)
        most_frequent_word = 'data'

        # WHEN
        stats = Statistics(urls) # None because we do not need any url to test stats_one_url
        res = stats.stats_urls()

        # THEN
        self.assertEqual(res['number of documents'], nb_docs)
        self.assertEqual(res['number of tokens'], nb_tokens)
        self.assertEqual(res['average number of tokens per document'], avg_tok)
        self.assertTrue(most_frequent_word in res['top of most frequent tokens'])
        self.assertEqual(res['top of most frequent tokens'][most_frequent_word], 2)
        
       