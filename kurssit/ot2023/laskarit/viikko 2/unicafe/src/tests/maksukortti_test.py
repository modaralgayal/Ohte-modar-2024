import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_saldo_ei_muutu_jos_ei_ole_tarpeeksi(self):
        kortti = Maksukortti(200)
        kortti.ota_rahaa(300)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_rahan_ottaminen_toimii(self):
        kortti = Maksukortti(1000) 
        kortti.ota_rahaa(500)  
        self.assertEqual(str(kortti), "Kortilla on rahaa 5.00 euroa") 
    
    def test_rahan_lataaminen_toimii(self):
        kortti = Maksukortti(500)  
        kortti.lataa_rahaa(200)
        self.assertEqual(str(kortti), "Kortilla on rahaa 7.00 euroa") 
    def test_saldo_euroina_toimii(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)  # Alkusaldon tulee olla 10 euroa
    
    def test_saldo_euroina_kun_saldo_muuttuu(self):
        self.maksukortti.lataa_rahaa(500)  # Lisätään 5 euroa
        self.assertEqual(self.maksukortti.saldo_euroina(), 15.00)  # Saldon tulee olla nyt 15 euroa

if __name__ == '__main__':
    unittest.main()
