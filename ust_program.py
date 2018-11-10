import re
def frame (sent_words):
    size = max(len(word) for word in sent_words)
    print('*' * (size + 4))
    for word in sent_words:
        print('* {:<{}} *'.format(word, size))
    print('*' * (size + 4))
sentence = raw_input("Enter the string:")
reg=re.compile('^[a-zA-z\s\.]+$')
if reg.match(sentence):
    sent_words=sentence.split()
    frame(sent_words)
else:
    print("Please enter string without special characters and numbers")
