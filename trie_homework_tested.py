
from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise ValueError("Suffix pattern must be a string.")
        count = 0
        for key in self:
            if key.endswith(pattern):
                count += 1
        return count

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise ValueError("Prefix must be a string.")
        return any(True for key in self if key.startswith(prefix))


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Test count_words_with_suffix
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat
    assert trie.count_words_with_suffix("x") == 0  # no match

    # Test has_prefix
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat
    assert trie.has_prefix("dog") == False

    print("✅ All tests passed successfully!")
