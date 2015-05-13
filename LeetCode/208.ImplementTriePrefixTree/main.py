import pdb
from Solution import Trie 

def main():
	trie = Trie()
	trie.insert("abc")
	print trie.search("abc")
	print trie.search("ab")
	trie.insert("ab")
	print trie.search("ab")
	print trie.insert("ab")
	print trie.search("ab")

main()
