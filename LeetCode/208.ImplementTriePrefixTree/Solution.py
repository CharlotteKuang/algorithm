import pdb

#start with is different from search
#I add a flag to tell whether a word lie on this node.

class TrieNode:
	# Initialize your data structure here.
	def __init__(self):
		self.end = False
		self.letterToChild = {}

class Trie:

	def __init__(self):
		self.root = TrieNode()

	# @param {string} word
	# @return {void}
	# Inserts a word into the trie.
	def insert(self, word):
		#pdb.set_trace()
		node = self.root
		for letter in word:
			if not letter in node.letterToChild:
				child = TrieNode()
				node.letterToChild[letter] = child
			node = node.letterToChild[letter]
		node.end = True

	# @param {TrieNode} node 
	# @param {string} word
	# @return {boolean}
	# Returns if the word is in the trie.
	def search(self, word):
		node = self.root 
		for letter in word:
			if letter in node.letterToChild:
				node = node.letterToChild[letter]
			else:
				return False
		return node.end 

	# @param {string} prefix
	# @return {boolean}
	# Returns if there is any word in the trie
	# that starts with the given prefix.
	def startsWith(self, prefix):
		node = self.root 
		for letter in prefix:
			if letter in node.letterToChild:
				node = node.letterToChild[letter]
			else:
				return False 
		return True

	#def print(self):


# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
