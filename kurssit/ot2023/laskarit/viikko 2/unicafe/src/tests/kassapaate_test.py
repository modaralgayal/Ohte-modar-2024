import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassa = Kassapaate()
        assert self.kassa.kassassa_rahaa == 100000
        assert self.kassa.edulliset == 0
        assert self.kassa.maukkaat == 0

    def test_kateinen_maukkaalle_riittava(self):

        kassa = Kassapaate()

        kassa.syo_maukkaasti_kateisella(500)
        assert kassa.kassassa_rahaa == 100400
        assert kassa.maukkaat == 1
        assert kassa.syo_maukkaasti_kateisella(500) == 500 - 400

    def test_kateinen_maukkaalle_ei_riittava(self):

        kassa = Kassapaate()

        kassa.syo_maukkaasti_kateisella(300)
        assert kassa.syo_maukkaasti_kateisella(300) == 300

    def test_kateinen_edulliselle_riittava(self):

        kassa = Kassapaate()

        kassa.syo_edullisesti_kateisella(300)
        assert kassa.kassassa_rahaa == 100240
        assert kassa.edulliset == 1
        assert kassa.syo_edullisesti_kateisella(300) == 60

        kassa = Kassapaate()

        kassa.syo_edullisesti_kateisella(240)
        assert kassa.kassassa_rahaa == 100240
        assert kassa.edulliset == 1
        assert kassa.syo_edullisesti_kateisella(240) == 0

    def test_kateinen_edulliselle_ei_riittava(self):

        kassa = Kassapaate()

        kassa.syo_edullisesti_kateisella(100)
        assert kassa.kassassa_rahaa == 100000
        assert kassa.edulliset == 0
        assert kassa.syo_edullisesti_kateisella(100) == 100

    def test_kortti_edulliselle(self):

        kassa = Kassapaate()
        kortti = Maksukortti(500)

        assert kassa.syo_edullisesti_kortilla(kortti) == True
        assert kassa.edulliset == 1
        assert kortti.saldo == 260

        kortti = Maksukortti(100)

        assert kassa.syo_edullisesti_kortilla(kortti) == False
        assert kassa.edulliset == 1
        assert kortti.saldo == 100

    def test_toimiiko_maksukortti(self):

        kortti = Maksukortti(100)

        kortti.saldo = 100

    def test_kortti_maukkaalle(self):

        kassa = Kassapaate()
        kortti = Maksukortti(500)

        assert kassa.syo_maukkaasti_kortilla(kortti) == True
        assert kassa.maukkaat == 1
        assert kortti.saldo == 100
        assert kassa.kassassa_rahaa == 100000

        kortti = Maksukortti(100)

        assert kassa.syo_maukkaasti_kortilla(kortti) == False
        assert kassa.edulliset == 0
        assert kortti.saldo == 100
        assert kassa.kassassa_rahaa == 100000

    def test_kortti_edulliselle(self):

        kassa = Kassapaate()
        kortti = Maksukortti(500)

        assert kassa.syo_edullisesti_kortilla(kortti) == True
        assert kassa.edulliset == 1
        assert kortti.saldo == 260
        assert kassa.kassassa_rahaa == 100000

        kortti = Maksukortti(100)

        assert kassa.syo_edullisesti_kortilla(kortti) == False
        assert kassa.edulliset == 1
        assert kortti.saldo == 100
        assert kassa.kassassa_rahaa == 100000

    def test_lataus_kortille_toimii(self):

        kassa = Kassapaate()
        kortti = Maksukortti(100)

        kassa.lataa_rahaa_kortille(kortti, 200)

        assert kassa.kassassa_rahaa == 100200
        assert kortti.saldo == 300

        kassa = Kassapaate()
        kortti = Maksukortti(100)

        kassa.lataa_rahaa_kortille(kortti, -200)

        assert kassa.kassassa_rahaa == 100000
        assert kortti.saldo == 100
        assert kassa.lataa_rahaa_kortille(kortti, -200) == None

    def test_kassassa_rahaa_euroina_toimii(self):
        kassa = Kassapaate()
        kortti = Maksukortti(100)

        self.kassa.lataa_rahaa_kortille(kortti, 500)
        self.assertEqual(kassa.kassassa_rahaa_euroina(), 1000.00)

if __name__ == '__main__':
    unittest.main()

