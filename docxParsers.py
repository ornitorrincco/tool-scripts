# docx parser
# -*- coding: utf-8 -*-

# pip install python-docx
import operator
from collections import Counter

import RAKE
import docx


def docxGetText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


def getKeywords(filename, fullText):
    Rake = RAKE.Rake(filename, 3, 2, 3)
    listKeywords = Rake.run(fullText)
    words = []

    words = [i[0] for i in listKeywords]
    if len(words) >= 10:
        keywords = words[0:10]
    else:
        keywords = words[0:len(words)]

    return keywords


def frequentWords(filename):
    fullText = docxGetText(filename)
    Words = dict(Counter(fullText.split()))
    numberOfWords = len(Words)
    sorted_x = list(reversed(sorted(Words.items(), key=operator.itemgetter(1))))
    frequentWords = []
    for i in range(0, 10):
        frequentWords = frequentWords + [sorted_x[i]]
    return frequentWords, numberOfWords


filename = 'test.docx'
frequentWords(filename)
fullText = docxGetText(filename)
filename = 'SmartStopList.txt'
keywords = getKeywords(filename, fullText)

print
keywords
# cosas = {'words':numberOfWords}
# print(json.dumps(cosas))


