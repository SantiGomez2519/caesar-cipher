import unittest
from caesar import encrypt, decrypt


class TestCaesarCipher(unittest.TestCase):
    # Tests for Caesar cipher encrypt/decrypt with numeric key.

    def test_1_encrypt_simple_text_key_3(self):
        """Test 1: Encrypt 'HELLO' with key 3 must yield 'KHOOR'."""
        result = encrypt("HELLO", 3)
        self.assertEqual(result, "KHOOR")

    def test_2_decrypt_returns_original(self):
        """Test 2: Decrypting the result of encrypt must return the original text."""
        original = "Cybersecurity"
        key = 7
        encrypted = encrypt(original, key)
        decrypted = decrypt(encrypted, key)
        self.assertEqual(decrypted, original)

    def test_3_key_zero_leaves_text_unchanged(self):
        """Test 3: With key 0 the text must not change."""
        text = "Python"
        self.assertEqual(encrypt(text, 0), text)
        self.assertEqual(decrypt(text, 0), text)

    def test_4_key_larger_than_26_normalizes(self):
        """Test 4: Key 30 equals key 4 (30 mod 26 = 4)."""
        text = "A"
        self.assertEqual(encrypt(text, 4), encrypt(text, 30))
        self.assertEqual(encrypt(text, 3), encrypt(text, 3 + 26))

    def test_5_preserves_spaces_and_symbols(self):
        """Test 5: Spaces, digits and symbols are not modified."""
        text = "Hello, world! 2025"
        encrypted = encrypt(text, 5)
        self.assertIn(" ", encrypted)
        self.assertIn(",", encrypted)
        self.assertIn("!", encrypted)
        self.assertIn("2025", encrypted)
        decrypted = decrypt(encrypted, 5)
        self.assertEqual(decrypted, text)


if __name__ == "__main__":
    unittest.main()
