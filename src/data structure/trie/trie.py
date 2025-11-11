class TrieNode:
    def __init__(self):
        self.children={}
        self.end_word = 0 #How many words end here.
        self.count = 0 # count how many words pass through this node

class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert_count(self, word):
        node = self.root
        prefix_pairs = 0

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            prefix_pairs+= node.end_word

        prefix_pairs+=node.count

        node.end_word+=1

        node = self.root
        for ch in word:
            node = node.children[ch]
            node.count+=1

        return prefix_pairs

def solution(titles):
    trie = Trie()
    s=0
    for i in titles:
        s+=trie.insert_count(i)

    return s

titles = ["wall", "wallpaper", "wallet", "phil", "philosophy"]
print(solution(titles))
