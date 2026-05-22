import re
import os
from collections import Counter
from itertools import pairwise
import pickle

class BpeTrain(): 
    def __init__(self) -> None:
        self.vocab = set()
        self.corpus = []
        self.corpus_len = 0
        self.rules = []

    def create_vocab(self, text):
        text = re.sub(r'(\s+)', "_", text)
        self.vocab.update(set(text))
        self.corpus.extend(list(text))
        self.corpus_len = len(self.corpus)

    def pair_counting(self):
        pairs = Counter(pairwise(self.corpus)).most_common()
        for pair in pairs:
            chars = pair[0]
            if len(chars[0]) > 1 and ("_" in chars[0] and chars[0][-1] =="_"):
                continue
            else:
                selected = chars
                break
            

        try:
            mc = "".join(selected)
            self.vocab.add(mc)
            self.rules.append(mc)
            
            for i in range(2, self.corpus_len, 1): 
                pair = "".join(self.corpus[i-2:i])
                if pair == mc: 
                    self.corpus[i-2:i] = [pair]
                else:
                    continue
        except:
            print("no pairs left without crossing whitespace")
            return False

    def save(self, save_path="./"):
        vocab_path = os.path.join(save_path, "vocab.pkl")
        rules_path = os.path.join(save_path, "rules.pkl")

        pickle.dump(self.vocab, open(vocab_path, 'wb'))
        pickle.dump(self.vocab, open(rules_path, 'wb'))

    def load(self, vocab, rules):
        self.vocab = pickle.load(open(vocab, 'rb'))
        self.rules = pickle.load(open(rules, 'rb'))
    
    def apply_rules(self, text):
        text = re.sub(r'(\s+)', "_", text)
        text = list(text)
        for rule in self.rules:
            for i in range(2, len(text), 1): 
                pair = "".join(text[i-2:i])
                if pair == rule: 
                    text[i-2:i] = [pair]
                else:
                    continue
        return text

    
def main():
    test_data="set new new renew reset renew"
    bpe = BpeTrain()
    bpe.create_vocab(test_data)
    for i in range(15):
           if bpe.pair_counting() == False:
               break
    
    

    

    bpe.save()
    
    bpe2 = BpeTrain()
    bpe2.load("vocab.pkl", "rules.pkl")
    print(bpe2.rules)
    print(bpe2.vocab)



if __name__ == "__main__":
        main()
