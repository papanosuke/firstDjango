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
    elif request.method == "POST":
        token = request.session["token"]
        deck = r.get_redis(token,"deck")
        money = r.get_redis(token,"money")
        
        player_hands = r.get_redis(token,"player_hands")
        dealer_hands = r.get_redis(token,"dealer_hands")
        
        if (r.get_redis(token,"game_now") == False):
            r.set_redis(token,"game_now",True)
            money -= int(request.POST["bet"]
            r.set_redis(token,"bet",int(request.POST["bet"]))
            dealer_hands = []
            dealer_hands.append(deck.pop())
            player_hands = []
            player_hands.append(deck.pop())
            player_hands.append(deck.pop())
        
            r.set_redis(token,"dealer_hands",dealer_hands)
            r.set_redis(token,"player_hands",player_hands)
            
            dealer_point = bj.get_point(dealer_hands)
            player_point = bj.get_point(player_hands)
            
            r.set_redis(token,"deck",deck)

            dictionary = {
                "msg" : "選択してください。",
                "dealer_cards" : dealer_hands,
                "dealer_point" : dealer_point,
                "player_cards" : player_hands,
                "player_point" : player_point,
                "able_bet" : True,
                "able_double" : True,
                "money" : money,
                "dealer_cards" : int(request.POST["bet"],
            }
            dictionary.update(csrf(request))
        
            return render(request,"bjgame.html",dictionary)
    
