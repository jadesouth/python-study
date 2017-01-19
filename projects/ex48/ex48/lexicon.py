# encoding=utf-8
class Lexicon(object):

    # 方向词 
    direction = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
    verb = ('go', 'stop', 'kill', 'eat')
    stop = ('the', 'in', 'of', 'from', 'at', 'it')
    noun = ('door', 'bear', 'princess', 'cabinet')

    def scan(self, sentence):
        words = sentece.split()
        res = []
        for word in words:
            try: # 数字
                word = int(word)
                word_type = 'number'
            except ValueError: # 单词
                if word in Lexicon.direction:
                    word_type = 'direction'
                elif word in Lexicon.verb:
                    word_type = 'verb'
                elif word in Lexicon.stop:
                    word_type = 'stop'
                elif word in Lexicon.noun:
                    word_type = 'noun'
                else:
                    word_type = 'error'

                res.append((word_type, word))

        return res

# 方向词 
direction = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verb = ('go', 'stop', 'kill', 'eat')
stop = ('the', 'in', 'of', 'from', 'at', 'it')
noun = ('door', 'bear', 'princess', 'cabinet')

def scan(sentence):
    words = sentence.split()
    res = []
    for word in words:
        try: # 数字
            word = int(word)
            word_type = 'number'
        except ValueError: # 单词
            if word in direction:
                word_type = 'direction'
            elif word in verb:
                word_type = 'verb'
            elif word in stop:
                word_type = 'stop'
            elif word in noun:
                word_type = 'noun'
            else:
                word_type = 'error'

        res.append((word_type, word))

    return res
