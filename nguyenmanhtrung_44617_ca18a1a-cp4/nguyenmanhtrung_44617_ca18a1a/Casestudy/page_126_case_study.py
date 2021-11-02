"""
Author:Nguyễn Manh Trung
Date: 24/09/2021

Problem: Write a program that computes the Flesch Index and grade level for text stored in a
text file

Solution:
    ....
"""
import os

dire = os.getcwd()
listOfdir=os.listdir(dire)
while True:
    UserFileName=raw_input("Nhập tên file:")
    if (UserFileName in listOfdir) and (UserFileName.endswith('.txt')):
        InputFile=open(UserFileName,'r')
        text=InputFile.read()
        sentence=text.count(".")+text.count('!')+\
            text.count(";")+text.count(":")+\
            text.count("?")
        words=len(text.split())
        syllable=0
        for word in text.split():
            for vowel in ['a','e','i','o','u']:
                syllable+=word.count(vowel)
                for ending in ['es','ed','e']:
                    if word.endswith(ending):
                        syllable-=1
                        if word.endswith('le'):
                            syllable+=1
                            ID=206.835 - 1.015 * (words / sentences) -\
                            84.6 * (syllable / words)
                            G=round((0.39*words)/sentence+(11.8*syllable)/words-15.59)
                            print(" Chỉ số ID", ID)
                            print("Cấp tương đương là", G)
                            print(sentences, "sentences")
                            print(words, "words")
                            print(syllable, "syllables")
                            sentences = int(input("Sentences: "))
                            words = int(input("Words: "))
                            syllable = int(input("Syllables: "))





