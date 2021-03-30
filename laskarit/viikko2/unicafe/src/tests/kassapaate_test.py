import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kassassa_rahaa = 1000
    
    def test_saldo_oikein_luonnissa(self):
        self.assertEqual(self.kassassa_rahaa, 1000)
    
    def test_kateisosto_edullinen_kassa_kasvaa(self):
        self.kassa.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
    def test_myydyt_lounaat_kasvaa_edullinen_kateinen(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.edulliset, 1)
    def test_kateisosto_maukas_kassa_kasvaa(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
    def test_kateisosto_edullinen_vaihtoraha(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(500), 260)
    def test_myydyt_lounaat_kasvaa_edullinen_kateinen(self):
        self.kassa.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassa.edulliset, 1)
    def test_edullinen_maksu_ei_riita_kateinen_summa(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.edulliset, 0)
    def test_edullinen_maksu_ei_riita_kateinen_kassanraha(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    def test_edullinen_maksu_ei_riita_kateinen_vaihtoraha(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(200), 200)

    def test_kateisosto_maukas_kassa_kasvaa(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
    def test_kateisosto_maukas_vaihtoraha(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500), 100)
    def test_myydyt_lounaat_kasvaa_maukas_kateinen(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.maukkaat, 1)
    def test_maukas_maksu_ei_riita_kateinen_summa(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.maukkaat, 0)
    def test_maukas_maksu_ei_riita_kateinen_kassanraha(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    def test_maukas_maksu_ei_riita_kateinen_vaihtoraha(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(200), 200)
    
    def test_korttiosto_edullinen_raha_riittaa(self):
        self.kortti = Maksukortti(1000)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 7.6")
    def test_korttiosto_edullinen_raha_riittaa_palautus(self):
        self.kortti = Maksukortti(1000)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)

    def test_korttiosto_maukas_raha_riittaa_saldo(self):
        self.kortti = Maksukortti(1000)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 6.0")
    def test_korttiosto_maukas_raha_riittaa_palautus(self):
        self.kortti = Maksukortti(1000)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)
    
    def test_korttiosto_edullinen_myydyt_kasvaa(self):
        self.kortti = Maksukortti(1000)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)
    def test_korttiosto_maukas_myydyt_kasvaa(self):
        self.kortti = Maksukortti(1000)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_korttiosto_edullinen_rahatLoppu_KortinSaldo(self):
        self.kortti = Maksukortti(200)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 2.0")
    def test_korttiosto_maukas_rahatLoppu_KortinSaldo(self):
        self.kortti = Maksukortti(200)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 2.0")
    
    def test_korttiosto_edullinen_rahatLoppu_myydyt(self):
        self.kortti = Maksukortti(200)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 0)
    def test_korttiosto_maukas_rahatLoppu_myydyt(self):
        self.kortti = Maksukortti(200)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_korttiosto_edullinen_rahatLoppu_palautus(self):
        self.kortti = Maksukortti(200)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), False)
    def test_korttiosto_maukas_rahatLoppu_palautus(self):
        self.kortti = Maksukortti(200)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), False)

    def test_korttiosto_kassan_saldo(self):
        self.kortti = Maksukortti(500)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortin_saldo_muuttuu(self):
        self.kortti = Maksukortti(500)
        self.kortti.lataa_rahaa(200)
        self.assertEqual(self.kortti.saldo, 700)
    def test_kassan_rahat_kasvaa(self):
        self.kortti = Maksukortti(500)
        self.kassa.lataa_rahaa_kortille(self.kortti, 200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100200)

    def test_kassan_rahat_kasvaa_negatiivinen_lisays(self):
        self.kortti = Maksukortti(500)
        self.kassa.lataa_rahaa_kortille(self.kortti, -200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)