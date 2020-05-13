from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def aboutpage(request):
    return render(request,'about.html')


def count(request):
    testo_immesso= request.GET['fulltext'] #catturi il testo immesso sull'entry form - fulltext è il name dell'area in home.html
    #print(testo_immesso)
    wordlist = testo_immesso.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    parole_ordinate = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request,'count.html', {'fulltext':testo_immesso, 'count':len(wordlist), 'sortedwords': parole_ordinate}) #aggiunto key,value per wordlist