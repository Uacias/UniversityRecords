import unittest

from src.pesel import decode_pesel, validate_pesel


class TestPeselFunctions(unittest.TestCase):

    def test_validate_pesel_valid(self):
        valid_pesels = [
            "57010124545",
            "54051956544",
            "79010323588",
            "75091945785",
            "94052255884",
            "76120282222",
        ]
        for pesel in valid_pesels:
            with self.subTest(pesel=pesel):
                self.assertTrue(validate_pesel(pesel))

    def test_validate_pesel_invalid(self):
        # Test niepoprawnych numerów PESEL
        invalid_pesels = [
            "0x",
            "0xdeadbeefdeadbeefdeadbeefdeadbeef",
            "123123123",
            "5ba8815 bbasdasd",
        ]
        for pesel in invalid_pesels:
            with self.subTest(pesel=pesel):
                self.assertFalse(validate_pesel(pesel))

    def test_decode_pesel_valid(self):
        valid_pesels_with_data = [
            ("48030665857", "1948-03-06", "Mężczyzna"),
            ("03210122447", "2003-01-01", "Kobieta"),
            ("86020799483", "1986-02-07", "Kobieta"),
            ("86020731791", "1986-02-07", "Mężczyzna"),
            ("25212411833", "2025-01-24", "Mężczyzna"),
            ("88091996927", "1988-09-19", "Kobieta"),
        ]
        for pesel, expected_date, expected_gender in valid_pesels_with_data:
            with self.subTest(pesel=pesel):
                result = decode_pesel(pesel)
                self.assertIsNotNone(result)
                self.assertEqual(result["data_urodzenia"], expected_date)
                self.assertEqual(result["płeć"], expected_gender)

    def test_decode_pesel_invalid(self):
        invalid_pesels = [
            "05x3ed51205691029619120659",
            "0xdeadbeefdeadbeefdeadbeef",
            "0xbeefdead123123",
            "0x",
        ]
        for pesel in invalid_pesels:
            with self.subTest(pesel=pesel):
                result = decode_pesel(pesel)
                self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
