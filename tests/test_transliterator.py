import unittest
from qalamos.transliteration.transliterator import IJMESTransliterator


class TestArabicTransliteration(unittest.TestCase):
    def setUp(self):
        self.transliterator = IJMESTransliterator()
        # Test cases with their expected transliterations
        self.test_cases = {
            # Original test case
            "إِعْرَابُ الْجَمَلِ": "iʿrābu al-jamali",
            # Initial hamza cases
            "أَكَلَ": "akala",  # Simple hamza on alif
            "إِيمَان": "īmān",  # Hamza with yā for long ī
            # Double letter (shadda) cases
            "مُدَرِّس": "mudarris",  # Shadda mid-word
            "حَجّ": "hajj",  # Shadda at end
            # Long vowel cases
            "كِتَاب": "kitāb",  # Long ā
            "حَزِين": "hazīn",  # Long ī
            "سُكُون": "sukūn",  # Long ū
            # Special character cases
            "مَدْرَسَة": "madrasa",  # Tā' marbūṭa
            "مُوسَى": "mūsā",  # Alif maqṣūra
            # Multiple prefixes
            "وَبِالْمَدْرَسَةِ": "wa-bil-madrasa",  # Multiple prefixes
            "فَالْعِلْمُ": "fa-al-ʿilm",  # fa + al
            # Special letter combinations
            "مُعَلِّمُ الْعَرَبِيَّةِ": "muʿallim al-ʿarabiyya",  # Multiple shaddas
            "الْآن": "al-ān",  # Madda
            # Sun and moon letters
            "الشَّمْس": "al-shams",  # Sun letter
            "الْقَمَر": "al-qamar",  # Moon letter
            # Complex combinations
            "الْإِسْلَامِيَّة": "al-islāmiyya",  # Hamza + shadda + long vowel
            "الْمُؤْمِنُون": "al-muʿminūn",  # Hamza in middle + long vowel
        }

    def test_transliterations(self):
        for arabic, expected in self.test_cases.items():
            print(f"\nTesting: {arabic}")
            result = self.transliterator.transliterate(arabic)

            # Print Unicode analysis for debugging
            print("Character analysis:")
            for i, char in enumerate(arabic):
                print(f"Position {i}: '{char}' (Unicode: {hex(ord(char))})")

            print(f"Diacriticized: {result['diacriticized']}")
            print(f"Got: {result['transliterated']}")
            print(f"Expected: {expected}")

            self.assertEqual(
                result["transliterated"].strip(),
                expected,
                f"Incorrect transliteration for '{arabic}'\nExpected: {expected}\nGot: {result['transliterated']}",
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
