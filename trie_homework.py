class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def put(self, word: str) -> None:
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        if word == "":
            raise ValueError("Cannot insert empty word")

        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def has_prefix(self, prefix: str) -> bool:
        if not isinstance(prefix, str):
            raise TypeError("Prefix must be a string")
        if prefix == "":
            raise ValueError("Prefix must be non-empty")

        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True


class Homework(Trie):
    def __init__(self):
        super().__init__()

    def count_words_with_suffix(self, suffix: str) -> int:
        if not isinstance(suffix, str):
            raise TypeError("Suffix must be a string")
        if suffix == "":
            raise ValueError("Suffix must be non-empty")

        count = 0

        def dfs(node: TrieNode, path: str):
            nonlocal count
            if node.is_end_of_word and path.endswith(suffix):
                count += 1
            for char, child in node.children.items():
                dfs(child, path + char)

        dfs(self.root, "")
        return count


if __name__ == "__main__":
    words = ["apple", "application", "banana", "cat"]
    trie = Homework()
    for word in words:
        trie.put(word)

    print("Has prefix 'app':", trie.has_prefix("app"))
    print("Has prefix 'ba':", trie.has_prefix("ba"))
    print("Has prefix 'cat':", trie.has_prefix("cat"))
    print("Has prefix 'dog':", trie.has_prefix("dog"))

    print("Words with suffix 'le':", trie.count_words_with_suffix("le"))       # apple
    print("Words with suffix 'ion':", trie.count_words_with_suffix("ion"))     # application
    print("Words with suffix 'na':", trie.count_words_with_suffix("na"))       # banana
    print("Words with suffix 'at':", trie.count_words_with_suffix("at"))       # cat
    print("Words with suffix 'xyz':", trie.count_words_with_suffix("xyz"))     # none
