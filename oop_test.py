import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):": "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)": "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)": "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()": "Set *** to an instance of class %%%.",
    "***.***(@@@)": "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'": "From *** get the *** attribute and set it to '***'."
}
#print '*' * 30
#print 'PHRASES: ', PHRASES

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

#print '*' * 30
#print 'WORDS: ', WORDS
#print '*' * 30

def convert(snippet, phrase):
#    print "into convert: \nargs,\nsnippet: %r\nphrase %r" % (snippet, phrase)
#    print random.sample(WORDS, snippet.count('%%%'))
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
#    print "class_name: ", class_names
    other_name = random.sample(WORDS, snippet.count("***"))
#    print "other_name: ", other_name
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_name:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL-D
try:
    while True:
        snippets = PHRASES.keys()
#        print '-' * 30
#        print "PHRASES.keys: ", snippets
        random.shuffle(snippets)
#        print '-' * 30
#        print "PHRASES.keys.shuffle: ", snippets

        for snippet in snippets:
            phrase = PHRASES[snippet]
#            print '+' * 30
#            print "PHRASES[phrase], ", phrase
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input("> ")
            print "ANSWER: %s\n\n" % answer
except EOFError:
    print "\nBye"
