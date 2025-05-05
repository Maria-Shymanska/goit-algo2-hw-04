
class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def put(self, key, value=None):
        if not isinstance(key, str) or not key:
            raise TypeError("Word must be a non-empty string")
        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        if current.value is None:
            self.size += 1
            current.value = value

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise TypeError("Suffix pattern must be a string")

        count = 0

        def dfs(node, path):
            nonlocal count
            if node.value is not None and path.endswith(pattern):
                count += 1
            for char, child in node.children.items():
                dfs(child, path + char)

        dfs(self.root, "")
        return count

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise TypeError("Prefix must be a string")

        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    
    
if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Тести на суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat
    assert trie.count_words_with_suffix("z") == 0  # немає

    # Тести на префікс
    assert trie.has_prefix("app") == True
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True
    assert trie.has_prefix("ca") == True
    assert trie.has_prefix("z") == False

    print("All tests passed.")


