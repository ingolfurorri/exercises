class Sentence:
    def __init__(self, sent):
        self.sent = sent
    
    def get_first_word(self):
        self.words = self.sent.strip().split()
        return self.words[0]
        
    def get_all_words(self):
        return self.words 

    def replace(self, index, new_word):
        if not index > len(words)
            self.words[index] = new_word
        return self.words

sent = Sentance("This is a test")
print(sent.get_first_word())
print(sent.get_all_words())
sent.replace(3, "must")
print(sent.get_all_words())