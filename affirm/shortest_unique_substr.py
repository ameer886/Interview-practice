# // Input: ["cheapair", "cheapoair", "peloton", "pelican"]
# // Output:
# // "cheapair": "pa"  // every other 1-2 length substring overlaps with cheapoair
# // "cheapoair": "po" // "oa" would also be acceptable
# // "pelican": "ca"   // "li", "ic", or "an" would also be acceptable
# // "peloton": "t"    // this single letter doesn't occur in any other string

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, start_index, full_string):
        node = self.root
        for i in range(start_index, len(full_string)):
            char = full_string[i]
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
    
    def find_unique_substring(self, s):
        node = self.root
        unique_substr = ""
        for char in s:
            if char in node.children:
                node = node.children[char]
                unique_substr += char
                if node.count == 1:
                    return unique_substr
            else:
                break
        return ""
    
    def print_trie(self, node=None, level=0, prefix=''):
        if node is None:
            node = self.root
        
        for char, child_node in node.children.items():
            print(' ' * level * 2 + f"{prefix + char} (count: {child_node.count})")
            self.print_trie(child_node, level + 1, prefix + char)

def find_shortest_unique_substrings(strings):
    trie = Trie()
    
    # Insert all substrings into the Trie
    for s in strings:
        length = len(s)
        for i in range(length):
            trie.insert(i, s)

    trie.print_trie()
    
    # Find the shortest unique substring for each string
    result = []
    for s in strings:
        shortest_unique_substr = ""
        length = len(s)
        for i in range(length):
            candidate = trie.find_unique_substring(s[i:])
            if candidate:
                if not shortest_unique_substr or len(candidate) < len(shortest_unique_substr):
                    shortest_unique_substr = candidate
        result.append(shortest_unique_substr)
    
    return result

# Example usage
strings = ["cheapair", "cheapoair", "peloton", "pelican", "pel"]
shortest_unique_substrings = find_shortest_unique_substrings(strings)
print(shortest_unique_substrings)

