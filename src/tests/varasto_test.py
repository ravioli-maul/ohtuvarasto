import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

# Laajennukset
    def test_uudella_varastolla_virheellinen_tilavuus(self):
        varasto = Varasto(-10)
        self.assertEqual(varasto.tilavuus, 0)

    def test_alkusaldo_negatiivinen(self):
        varasto = Varasto(10, -10)
        self.assertEqual(varasto.saldo, 0)
    
    def test_negatiivinen_lesäys_ei_sallittu(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.lisaa_varastoon(-5)

        self.assertEqual(self.varasto.saldo, 5)
    
    def test_lisaa_maksimi(self):
        self.varasto.lisaa_varastoon(self.varasto.tilavuus)

        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_lisaa_yli_maksimin(self):
        self.varasto.lisaa_varastoon(2 * self.varasto.tilavuus)

        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)
    
    def test_ota_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(5)
        saatu = self.varasto.ota_varastosta(-3)

        self.assertEqual(saatu, 0)

    def test_ota_kaikki_mita_saat(self):
        self.varasto.lisaa_varastoon(5)
        saatu = self.varasto.ota_varastosta(10)

        self.assertEqual(saatu, 5)
        self.assertEqual(self.varasto.saldo, 0)

    def test_str_metodi(self):
        self.varasto.lisaa_varastoon(5)
        tulos = 'saldo = 5, vielä tilaa 5'

        self.assertEqual(str(self.varasto), tulos)
# T11 muutos