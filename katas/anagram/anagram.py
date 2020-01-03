import os
from collections import Counter


def getWordListFromString(stringToParse):

    wordList = stringToParse.split()

    return wordList


def getTextFromFile(filePath):
    file = open(filePath, "r")
    return file.read()


def getWordListFromFile(filePath):

    fileText = getTextFromFile(filePath)
    wordList = getWordListFromString(fileText)

    return wordList


def getLetterListFromTwoWords(word1, word2):
    return list(word1.lower()) + list(word2.lower())


def isWordMatchWithLetterList(word, letterList):
    # force to lower case
    word = word.lower()

    # Size check
    if len(word) != len(letterList):
        return False

    # check if match
    if Counter(list(word)) == Counter(letterList):
        return True

    return False


def getTwoWordsAnagramsListForWord(wordList, word):
    "Return a list of two words annagrams for gived word or an empty list if none"

    matches = []  # to store results

    # get matches:
    for word1 in wordList:
        for word2 in wordList:
            if word1 == word2:
                pass
            # if not same word:
            letters = getLetterListFromTwoWords(word1, word2)

            if isWordMatchWithLetterList(word, letters):
                # check if already inside matches
                if sorted([word1, word2]) in matches:
                    pass
                else:
                    matches.append(sorted([word1, word2]))
    return matches


if __name__ == "__main__":
    # Use case (note: no match for "documenting", trying "nliobastga" is ok):
    filePath = './wordlist.txt'
    wordList = getWordListFromFile(filePath)
    results = getTwoWordsAnagramsListForWord(wordList, "documenting")
    print("This is the list of 2-words anagrams for 'documenting':" + str(results))
