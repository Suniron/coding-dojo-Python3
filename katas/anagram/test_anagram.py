import os
from anagram import getWordListFromString, getTextFromFile, getWordListFromFile, getLetterListFromTwoWords, isWordMatchWithLetterList, getTwoWordsAnagramsListForWord, getTwoWordsAnagramsListForWord

path = "./katas/anagram/wordlist.txt"


def test_getWordListFromString():
    wantedResult = ["We", "are", "words"]

    assert getWordListFromString("We are words") == wantedResult
    assert getWordListFromString(" We are words") == wantedResult
    assert getWordListFromString("We are   words") == wantedResult


def test_getTextFromFile():
    assert type(getTextFromFile(path)) is str


def test_getWordListFromFile():
    assert type(getWordListFromFile(path)) is list


def test_getLetterListFromTwoWords():
    assert type(getLetterListFromTwoWords("word1", "word2")) is list
    assert getLetterListFromTwoWords("this", "word") == [
        "t", "h", "i", "s", "w", "o", "r", "d"]
    assert getLetterListFromTwoWords("This", "Word") == [
        "t", "h", "i", "s", "w", "o", "r", "d"]


def test_isWordMatchWithLetterList():
    letterList1 = getLetterListFromTwoWords("tet", "ser")
    letterList2 = getLetterListFromTwoWords("Ing", "Try")

    assert type(isWordMatchWithLetterList("tester", letterList1)) is bool
    assert isWordMatchWithLetterList("tester", letterList1) == True
    assert isWordMatchWithLetterList("test", letterList1) == False
    assert isWordMatchWithLetterList("TRYING", letterList2) == True


def test_getTwoWordsAnagramsListForWord():
    wordList = ["Ing", "tet", "ser", "try"]
    wordListFromFile = getWordListFromFile(path)

    assert getTwoWordsAnagramsListForWord(
        wordList, "tester") == [['ser', 'tet']]
    assert getTwoWordsAnagramsListForWord(wordList, "testing") == []
    assert sorted(getTwoWordsAnagramsListForWord(
        wordListFromFile, "nliobastga")) == sorted([["atlas", "bingo"], ['basil', 'tango']])
