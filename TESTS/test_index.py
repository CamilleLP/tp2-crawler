from unittest import TestCase
from INDEX.index import Index

class TestIndex(TestCase):
    def test_tokenize_webpage(self):
        # GIVEN
        url = "https://fr.wikipedia.org/wiki/Stargate"
        # title = "Stargate — Wikipédia"
        true_tokens = {'stargate', '—', 'wikipédia'}

        # WHEN
        index = Index()
        tokens = index.tokenize_title(url)

        # THEN
        self.assertEqual(set(tokens), true_tokens)

    def test_index_page(self):
        url = 'https://www.gouvernement.fr/beneficiez-de-la-prime-a-la-conversion-des-chaudieres'
        # title = Bénéficiez de la prime à la conversion des chaudières | Gouvernement.fr
        # on observe 2 fois le token 'la' en position 2 et 5 (0 est la première position en python)

        # WHEN
        index = Index()
        res = index.index_page(url)

        # THEN
        self.assertTrue('la' in list(res.keys()))
        self.assertTrue(url in list(res['la'].keys()))
        self.assertEqual(set(res['la'][url]['positions']), {2, 5})

    def test_index_total_pos_url_name(self):
        # GIVEN
        url1 = 'https://www.gouvernement.fr/beneficiez-de-la-prime-a-la-conversion-des-chaudieres'
        # title = Bénéficiez de la prime à la conversion des chaudières | Gouvernement.fr
        url2 = 'https://tvmag.lefigaro.fr/programme-tv/ce_soir_la_tv.html'
        # title = Ce soir TV - Programme TV de ce soir à la télé - TV Magazine
        urls = [url1, url2]

        # 'la' présent pour les 2 URLs
        # en position 2 et 5 pour url1 et en position 10 pour url2

        # 'soir' présent dans url2 mais pas dans url1
        # en position 1 et 7 dans url2

        # WHEN
        index = Index(urls)
        res = index.index_total(position=True, url_name=True)

        # THEN
        self.assertTrue('la' in list(res.keys()))
        self.assertTrue('soir' in list(res.keys()))

        self.assertTrue(url1 in list(res['la'].keys()))
        self.assertTrue(url2 in list(res['la'].keys()))

        self.assertFalse(url1 in list(res['soir'].keys()))
        self.assertTrue(url2 in list(res['soir'].keys()))
        
        self.assertEqual(set(res['la'][url1]['positions']), {2, 5})
        self.assertEqual(set(res['la'][url2]['positions']), {10})
        self.assertEqual(set(res['soir'][url2]['positions']), {1, 8})

        self.assertEqual(res['la'][url1]['count'], 2)
        self.assertEqual(res['la'][url2]['count'], 1)
        self.assertEqual(res['soir'][url2]['count'], 2)

    def test_index_total_pos_url_index(self):
        # GIVEN
        url1 = 'https://www.gouvernement.fr/beneficiez-de-la-prime-a-la-conversion-des-chaudieres'
        # title = Bénéficiez de la prime à la conversion des chaudières | Gouvernement.fr
        url2 = 'https://tvmag.lefigaro.fr/programme-tv/ce_soir_la_tv.html'
        # title = Ce soir TV - Programme TV de ce soir à la télé - TV Magazine
        urls = [url1, url2]

        # 'la' présent pour les 2 URLs
        # en position 2 et 5 pour url1 et en position 10 pour url2

        # 'soir' présent dans url2 mais pas dans url1
        # en position 1 et 7 dans url2

        # WHEN
        index = Index(urls)
        res = index.index_total(position=True, url_name=False)

        # THEN
        self.assertTrue('la' in list(res.keys()))
        self.assertTrue('soir' in list(res.keys()))

        self.assertTrue(str(urls.index(url1)) in list(res['la'].keys()))
        self.assertTrue(str(urls.index(url2)) in list(res['la'].keys()))

        self.assertFalse(str(urls.index(url1)) in list(res['soir'].keys()))
        self.assertTrue(str(urls.index(url2)) in list(res['soir'].keys()))

        self.assertEqual(set(res['la'][str(urls.index(url1))]['positions']), {2, 5})
        self.assertEqual(set(res['la'][str(urls.index(url2))]['positions']), {10})
        self.assertEqual(set(res['soir'][str(urls.index(url2))]['positions']), {1, 8})

        self.assertEqual(res['la'][str(urls.index(url1))]['count'], 2)
        self.assertEqual(res['la'][str(urls.index(url2))]['count'], 1)
        self.assertEqual(res['soir'][str(urls.index(url2))]['count'], 2)

    def test_index_total_pos_url_name(self):
        # GIVEN
        url1 = 'https://www.gouvernement.fr/beneficiez-de-la-prime-a-la-conversion-des-chaudieres'
        # title = Bénéficiez de la prime à la conversion des chaudières | Gouvernement.fr
        url2 = 'https://tvmag.lefigaro.fr/programme-tv/ce_soir_la_tv.html'
        # title = Ce soir TV - Programme TV de ce soir à la télé - TV Magazine
        urls = [url1, url2]

        # 'la' présent pour les 2 URLs
        # en position 2 et 5 pour url1 et en position 10 pour url2

        # 'soir' présent dans url2 mais pas dans url1
        # en position 1 et 7 dans url2

        # WHEN
        index = Index(urls)
        res = index.index_total(position=False, url_name=True)

        # THEN
        self.assertTrue('la' in list(res.keys()))
        self.assertTrue('soir' in list(res.keys()))

        self.assertTrue(url1 in list(res['la'].keys()))
        self.assertTrue(url2 in list(res['la'].keys()))

        self.assertFalse(url1 in list(res['soir'].keys()))
        self.assertTrue(url2 in list(res['soir'].keys()))

        self.assertEqual(res['la'][url1]['count'], 2)
        self.assertEqual(res['la'][url2]['count'], 1)
        self.assertEqual(res['soir'][url2]['count'], 2)

    def test_index_total_npos_url_index(self):
        # GIVEN
        url1 = 'https://www.gouvernement.fr/beneficiez-de-la-prime-a-la-conversion-des-chaudieres'
        # title = Bénéficiez de la prime à la conversion des chaudières | Gouvernement.fr
        url2 = 'https://tvmag.lefigaro.fr/programme-tv/ce_soir_la_tv.html'
        # title = Ce soir TV - Programme TV de ce soir à la télé - TV Magazine
        urls = [url1, url2]

        # 'la' présent pour les 2 URLs
        # en position 2 et 5 pour url1 et en position 10 pour url2

        # 'soir' présent dans url2 mais pas dans url1
        # en position 1 et 7 dans url2

        # WHEN
        index = Index(urls)
        res = index.index_total(position=True, url_name=False)

        # THEN
        self.assertTrue('la' in list(res.keys()))
        self.assertTrue('soir' in list(res.keys()))

        self.assertTrue(str(urls.index(url1)) in list(res['la'].keys()))
        self.assertTrue(str(urls.index(url2)) in list(res['la'].keys()))

        self.assertFalse(str(urls.index(url1)) in list(res['soir'].keys()))
        self.assertTrue(str(urls.index(url2)) in list(res['soir'].keys()))

        self.assertEqual(res['la'][str(urls.index(url1))]['count'], 2)
        self.assertEqual(res['la'][str(urls.index(url2))]['count'], 1)
        self.assertEqual(res['soir'][str(urls.index(url2))]['count'], 2)
