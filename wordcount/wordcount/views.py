from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wordDictionary = {}
    for word in wordlist:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1

    return render(request, 'count.html',{'fulltext': fulltext,'count':len(wordlist), 'wordDictionary':wordDictionary.items})