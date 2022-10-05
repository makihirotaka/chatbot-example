import random

class Markov:
    def __init__(self, words):
        self.words = words
        self.table = self.__build_table()

    def add(self, words):
        self.words += words
        self.table = self.__build_table()

    # ユーザー入力文からランダムに取得した形態素を起点に、マルコフ連鎖で回答文を生成
    def answer(self, user_morphemes):
        sentence = ""

        w1 = ''
        w2 = ''
        keys = list(self.table.keys())
        random.shuffle(keys)

        for key in keys:
            if key[0] in user_morphemes:
                w1 = key[0]
                w2 = key[1]
                break

        sentence = w1 + w2
        count = 0
        while w2 not in ["。", "！", "？", "!", "?", "."]:
            words = self.table.get((w1, w2))
            if words is None:break
            tmp = random.choice(words)
            sentence += tmp
            w1, w2 = w2, tmp
            count += 1
            if count > len(self.table):break
        return sentence

    def __build_table(self):
        table = {}
        w1 = ""
        w2 = ""
        for word in self.words:
            if w1 and w2:
                if (w1, w2) not in table:
                    table[(w1, w2)] = []
                table[(w1, w2)].append(word)
            w1, w2 = w2, word
        return table
