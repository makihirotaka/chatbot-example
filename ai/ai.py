import re

from ai.import_text import ImportText
from ai.markov import Markov
from ai.morpheme_analyzer import MorphemeAnalyzer
from ai.fixed_phrase import FixedPhrase

class Ai:
    def nanako_answer(input_text):
        import_text = ImportText('library/import.txt')
        fixed_phrase = FixedPhrase('library/pattern.csv')
        morpheme_analyzer = MorphemeAnalyzer()
        markov = Markov(morpheme_analyzer.analyze(import_text.read()))

        # ユーザー入力をインポートテキストに追記する
        if (re.match('@|＠', input_text)):
            add_text = re.sub('^@|^＠', '', input_text)
            import_text.add(add_text)
            markov.add(morpheme_analyzer.analyze(add_text))
            output_text = "覚えたよ！"
        else:
            # 定型文から回答を取得
            output_text = fixed_phrase.answer(input_text)

        # 定型文の回答がなければユーザー入力の名詞を起点にマルコフ連鎖で回答
        if output_text == "":
            nouns = morpheme_analyzer.extract_noun(input_text)
            output_text = markov.answer(nouns)

        if output_text == "":
            output_text = "ななこにも分かる言葉で言ってよぉ～☆"

        return output_text
