# 📚 Task: Extending Trie with Suffix and Prefix Search

🔧 Description This project implements a Homework class that extends a standard
Trie (prefix tree) data structure with additional functionality:

Insertion of words with associated values

Checking whether any word starts with a given prefix

Counting how many stored words end with a given suffix

🧠 Implemented Methods put(word: str, value: Any = None) Inserts a word into the
Trie with an optional value (e.g., an index). If the word already exists, it
won't be duplicated. Only unique words are stored.

has_prefix(prefix: str) -> bool Returns True if there is at least one word in
the Trie that starts with the given prefix.

count_words_with_suffix(suffix: str) -> int Returns the number of words that end
with the specified suffix. Internally, the method performs a depth-first search
(DFS) through the Trie and checks whether each full word ends with the given
suffix.

✅ Example Usage

trie = Homework() words = ["apple", "application", "banana", "cat"] for i, word
in enumerate(words): trie.put(word, i)

assert trie.count_words_with_suffix("e") == 1 # "apple" assert
trie.count_words_with_suffix("ion") == 1 # "application" assert
trie.count_words_with_suffix("a") == 1 # "banana" assert trie.has_prefix("app")
is True # "apple", "application" assert trie.has_prefix("bat") is False 🧪
Testing The implementation has been tested with multiple prefixes and suffixes.

The code includes input validation and raises appropriate errors when non-string
inputs are used.

🧩 Possible Extensions Implementing word deletion (delete)

Fetching all words with a given prefix or suffix (get_words_with_prefix/suffix)

## 🔍 Task 2: Longest Common Prefix using Trie

📘 Description This task extends the Trie data structure to solve a classic
problem: finding the longest common prefix among a list of words.

A new class LongestCommonWord, inheriting from Trie, implements a method that
returns the longest prefix shared by all input strings.

📌 Requirements The class LongestCommonWord must inherit from Trie.

The method find_longest_common_word(strings):

Accepts a list of strings.

Returns the longest common prefix.

Handles empty input and invalid data gracefully.

Time complexity: O(S), where S is the total number of characters in all strings.

🧠 Implemented Method find_longest_common_word(strings: List[str]) -> str Builds
a Trie from all input strings.

Traverses the Trie while:

There is only one child in the current node.

The current node is not the end of a word.

Accumulates characters along this unique path to form the common prefix.

Returns:

The longest common prefix (e.g., "fl").

An empty string if no common prefix exists or the input is empty.

✅ Example Usage

trie = LongestCommonWord() assert trie.find_longest_common_word(["flower",
"flow", "flight"]) == "fl"

trie = LongestCommonWord() assert trie.find_longest_common_word(["interspecies",
"interstellar", "interstate"]) == "inters"

trie = LongestCommonWord() assert trie.find_longest_common_word(["dog",
"racecar", "car"]) == ""

trie = LongestCommonWord() assert trie.find_longest_common_word([]) == "" ⚠️
Input Handling If the input is not a list of strings, the method raises a
ValueError.

If the input list is empty, it returns an empty string.
