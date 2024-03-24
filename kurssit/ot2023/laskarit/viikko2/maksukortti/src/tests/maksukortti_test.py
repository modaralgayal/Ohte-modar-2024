import unittest
from maksukortti import Maksukortti

EDULLINEN = 250
MAUKAS = 400

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")


    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()

        self.assertEqual(self.kortti.saldo_euroina(), 7.5)

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()

        self.assertEqual(self.kortti.saldo_euroina(), 6.0)

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_edullisesti()

        self.assertEqual(kortti.saldo_euroina(), 2.0)
    
    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(2500)

        self.assertEqual(self.kortti.saldo_euroina(), 35.0)

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(20000)

        self.assertEqual(self.kortti.saldo_euroina(), 150.0)
    
    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(500)
        kortti.syo_edullisesti()
        self.assertEqual(kortti.saldo_euroina(), 2.50)

    def test_negatiivisen_lataaminen_ei_muuta_saldoa(self):
        kortti = Maksukortti(1000)  
        kortti.lataa_rahaa(-500)  
        self.assertEqual(kortti.saldo_euroina(), 10.00) 

    def test_kortilla_pystyy_ostamaan_edullisen_lounaan_kun_riittaa_rahaa(self):
        kortti = Maksukortti(EDULLINEN) 
        kortti.syo_edullisesti()
        self.assertEqual(kortti.saldo_euroina(), 0.00)  

    def test_kortilla_pystyy_ostamaan_maukkaan_lounaan_kun_riittaa_rahaa(self):
        kortti = Maksukortti(MAUKAS) 
        kortti.syo_maukkaasti()
        self.assertEqual(kortti.saldo_euroina(), 0.00) 

