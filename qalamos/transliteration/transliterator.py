from mishkal.tashkeel import TashkeelClass
from typing import Dict


class IJMESTransliterator:
    def __init__(self):
        self.vocalizer = TashkeelClass()

        # Consonants from IJMES guide
        self.consonants = {
            "\u0621": "",  # hamza ء (dropped when initial)
            "\u0623": "",  # hamza on alif أ (dropped when initial)
            "\u0625": "",  # hamza under alif إ (dropped when initial)
            "\u0626": "ʾ",  # hamza on ya ئ
            "\u0628": "b",  # ب
            "\u062A": "t",  # ت
            "\u062B": "th",  # ث
            "\u062C": "j",  # ج
            "\u062D": "ḥ",  # ح
            "\u062E": "kh",  # خ
            "\u062F": "d",  # د
            "\u0630": "dh",  # ذ
            "\u0631": "r",  # ر
            "\u0632": "z",  # ز
            "\u0633": "s",  # س
            "\u0634": "sh",  # ش
            "\u0635": "ṣ",  # ص
            "\u0636": "ḍ",  # ض
            "\u0637": "ṭ",  # ط
            "\u0638": "ẓ",  # ظ
            "\u0639": "ʿ",  # ع
            "\u063A": "gh",  # غ
            "\u0641": "f",  # ف
            "\u0642": "q",  # ق
            "\u0643": "k",  # ك
            "\u0644": "l",  # ل
            "\u0645": "m",  # م
            "\u0646": "n",  # ن
            "\u0647": "h",  # ه
            "\u0648": "w",  # و
            "\u064A": "y",  # ي
        }

        # Vowel marks
        self.vowels = {
            "\u064E": "a",  # fatḥa
            "\u0650": "i",  # kasra
            "\u064F": "u",  # ḍamma
            "\u0652": "",  # sukūn
        }

        # Special characters
        self.special = {
            "\u0629": "a",  # tā' marbūṭa ة (changes to 'at' in construct state)
            "\u0649": "ā",  # alif maqṣūra ى
        }

        # Prefixes that need hyphens
        self.prefixes = {
            "\u0628": "bi",  # ب
            "\u0648": "wa",  # و
            "\u0644": "li",  # ل
            "\u0641": "fa",  # ف
        }

    def _handle_cell(self, chars, start_idx):
        """Handle a consonant and its modifiers as a unit."""
        print("chars", chars)
        i = start_idx
        result = []
        base_char = chars[i]

        # Get the next characters (if they exist)
        shadda = (
            chars[i + 1] if i + 1 < len(chars) and chars[i + 1] == "\u0651" else None
        )
        vowel_idx = i + 2 if shadda else i + 1
        vowel = (
            chars[vowel_idx]
            if vowel_idx < len(chars) and chars[vowel_idx] in self.vowels
            else None
        )
        print("vowel", vowel)
        extension_idx = vowel_idx + 1 if vowel else None
        extension = (
            chars[extension_idx]
            if extension_idx and extension_idx < len(chars)
            else None
        )

        # Get base consonant mapping
        cons_mapped = self.consonants.get(base_char, base_char)

        # Handle shadda (doubling)
        if shadda:
            result.append(cons_mapped + cons_mapped)
            i += 1
        else:
            result.append(cons_mapped)

        # Handle vowel and extension combinations
        if vowel:
            # print("vowel, extension:", {hex(ord(vowel))}, {hex(ord(extension))})
            # Get the mapping, which could be empty string for sukūn
            vowel_mapping = self.vowels[vowel]

            if vowel == "\u064E" and extension == "\u0627":  # fatḥa + alif
                result.append("ā")
                i += 2
            elif vowel == "\u0650" and extension == "\u064A":  # kasra + ya
                result.append("ī")
                i += 2
            elif vowel == "\u064F" and extension == "\u0648":  # ḍamma + waw
                result.append("ū")
                i += 2
            else:
                if vowel_mapping:  # Only append non-empty vowel mappings
                    result.append(vowel_mapping)
                i += 1

        return "".join(result), i + 1

    def _handle_prefix(self, word):
        """Handle inseparable prefixes and their combinations with al-."""
        if not word:
            return "", word

        # Convert word to list of characters for easier manipulation
        chars = list(word)

        # Helper to check if chars starting at idx match pattern, ignoring diacritics
        def match_base_chars(idx, pattern):
            i = idx
            for p in pattern:
                # Skip diacritics until we find a base character
                while i < len(chars) and chars[i] in self.vowels:
                    i += 1
                if i >= len(chars) or chars[i] != p:
                    return False
                i += 1
            return True, i

        # Check for prefix + al
        for prefix_char, prefix_trans in self.prefixes.items():
            if chars[0] == prefix_char:
                # Find where the actual prefix char ends (after any diacritics)
                matched, next_idx = match_base_chars(1, "ال")
                if matched:
                    # Skip diacritic after ل if present
                    if next_idx < len(chars) and chars[next_idx] in self.vowels:
                        next_idx += 1
                    # Return the standard prefix form and the remaining text
                    return prefix_trans + "-l-", "".join(chars[next_idx:])
                return prefix_trans + "-", "".join(chars[1:])

        # Handle just al-
        if chars[0] == "ا":
            matched, next_idx = match_base_chars(1, "ل")
            if matched:
                # Skip diacritic if present
                if next_idx < len(chars) and chars[next_idx] in self.vowels:
                    next_idx += 1
                return "al-", "".join(chars[next_idx:])

        return "", word

    def transliterate(self, text):
        """Main transliteration function."""
        diacriticized = self.vocalizer.tashkeel(text)

        words = diacriticized.split()
        result = []

        for word in words:
            chars = list(word)
            i = 0
            word_result = []

            # Handle prefixes first
            prefix, remaining = self._handle_prefix(word)

            if prefix:
                word_result.append(prefix)
                chars = list(remaining)

            # Process each character cell
            while i < len(chars):
                trans, new_i = self._handle_cell(chars, i)
                word_result.append(trans)
                i = new_i

            result.append("".join(word_result))

        return {"diacriticized": text, "transliterated": " ".join(result)}


def transliterate_text(text: str) -> Dict[str, str]:
    """Wrapper function for compatibility."""
    transliterator = IJMESTransliterator()
    return transliterator.transliterate(text)
