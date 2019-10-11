class Node():
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.word_finished = False  # last letter of the word
        self.freq = 1 

    ''' Set word_finished to given Boolean value
    '''
    def set_word(self, Bool):
        self.word_finished = Bool


class Trie():
    def __init__(self):
        self.root = Node(None)


    ''' insert given string into Trie
    '''
    def insert(self, string):
#        # string exists in Trie
#        if self.find(string) != None:
#            self.find(string).set_word(True)
#            return
#
        curr_node = self.root
        for s in string:
            if s not in curr_node.children:
                curr_node.children[s] = Node(s)
            else:  # node already exists
                curr_node.children[s].freq += 1
            curr_node = curr_node.children[s]
        curr_node.set_word(True)


    ''' Find the input string in this Trie.
        Return the number of letters needed for distinct search
    '''
    def find(self, string):
        curr_node = self.root
        cnt = 0
        for s in string:
            if s in curr_node.children:
                cnt += 1
                curr_node = curr_node.children[s]
                if curr_node.freq == 1:
                    return cnt
            else:
                return None
        if curr_node.word_finished:
            return cnt


def solution(words):
    answer = 0
    my_trie = Trie()
    for w in words:
        my_trie.insert(w)
    for w in words:
        answer += my_trie.find(w)
    return answer


if __name__ == "__main__":
    words = [["go", "gone", "guild"], ["abc", "def", "ghi", "jklm"], ["word", "war", "warrior", "world"]]
    for w in words:
        print(solution(w))  # 7, 4, 15
