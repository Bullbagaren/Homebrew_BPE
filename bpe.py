import re
from collections import Counter
from itertools import pairwise

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


    
    print(bpe.corpus)





if __name__ == "__main__":
        main()
