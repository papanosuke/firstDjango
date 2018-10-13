from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('こんにちは')
def card(request):
    return render(request,'card.html')
#
def welcome(request):
    name = "田中"
    dictionary = {"name" : name}
    return render(request,'name.html',dictionary)
#
def cards(request):
    rank_str = []
    rank = list(range(1,14))
    for x in rank:
        rank_str.append(str(x).zfill(2))
#
    return render(request,"cards.html",{"card_rank":rank_str})
#
def random_cards(request):
#
    import random
    suits = ["S","H","D","C"]
    ranks = range(1,14)
    deck = [(x,y) for x in ranks for y in suits]
    random.shuffle(deck)
#
    card1 = deck.pop()
    card2 = deck.pop()
#
    dictionary = {
        "suit" : card1[1],
        "rank" : str(card1[0]).zfill(2),
        "suit2" : card2[1],
        "rank2" : str(card2[0]).zfill(2),
   }
    return render(request,"display_cards.html",dictionary)
