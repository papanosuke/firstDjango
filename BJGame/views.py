from django.shortcuts import render
from django.template.context_processors import csrf
from django.http import HttpResponse
import random
import BJGame.redis_helper as r
import BJGame.blackjack as bj

def game(request):
    if request.method == "GET":
        token = str(random.random())
        request.session["token"] = token
        
        r.set_redis(token,"game_now",False)
        
        deck = bj.make_deck()
        r.set_redis(token,"deck",deck)
        r.set_redis(token,"money",100)
        r.set_redis(token,"bet",0)
        
        r.set_redis(token,"player_hands",[])
        r.set_redis(token,"dealer_hands",[])
        dictionary = {
            "msg" : "ベットしてください。",
            "dealer_cards" : [],
            "dealer_point" : 0,
            "player_cards" : [],
            "player_point" : 0,
            "able_bet" : True,
            "money" : 100,
            "dealer_cards" : [],
        }
        dictionary.update(csrf(request))
        
        return render(request,"bjgame.html",dictionary)
