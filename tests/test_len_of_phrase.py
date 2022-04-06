class TestShortPhrase:
    def test_length_of_string(self):
        phrase = input("Set a phrase: ")

        assert len(phrase) < 15, f"This string has more than 15 symbols. Count of symbols: {len(phrase)}"