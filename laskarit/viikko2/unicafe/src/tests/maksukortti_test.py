import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
    
    def test_rahan_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 10.1")

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 9.0")
    
    def test_saldo_ei_muutu_rahan_loppuessa(self):
        self.maksukortti.ota_rahaa(1001)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
    
    def test_otarahaa_metodi_palauttaa_oikein(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1001), False)
        self.assertEqual(self.maksukortti.ota_rahaa(2), True)
