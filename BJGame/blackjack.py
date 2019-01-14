#
##########################################################################
# ブラックジャック
##########################################################################
##########################################################################
# インポート
##########################################################################
import random
##########################################################################
# 変数
##########################################################################
#(RANK)=数字
#(SUIT)=スート
RANK,SUIT = 0,1
##########################################################################
# サブルーチン
##########################################################################
##########################################################################
# 勝敗判定
##########################################################################
def win_lose(dealer_hand,player_hand,bet,player_money):
    player_point = get_point(player_hand)
    dealer_point = get_point(dealer_hand)
    if player_point <= 21:
        if (player_point > dealer_point) or (dealer_point > 21):
            if player_point == 21:
                return ("<<プレイヤーの勝ち>>",player_money + int(bet*2.5))
            else:
                return ("<<プレイヤーの勝ち>>",player_money + bet*2)
        elif player_point == dealer_point:
                return ("<<プッシュ>>",player_money + bet)
        else:
            return ("<<プレイヤーの負け>>",player_money)
    else:
        return ("<<プレイヤーの負け>>",player_money)
                        
#
##########################################################################
# プレイヤーターン
##########################################################################
def player_op(deck,player_hand,op):
    #戻り値初期化
    doubled,ending = False,False
    if op == "1":
        print("[プレイヤー：スタンド ]")
#       スタンドの処理
        doubled,ending = False,True
    elif op == "2":
        print("[プレイヤー：ヒット　 ]")
#       ヒットの処理
        player_hand.append(deck.pop())
        print_player_hand(player_hand)
        doubled,ending = False,False
    elif op == "3":
#       ダブルの処理
        if len(player_hand) == 2:
            print("[プレイヤー：ダブル　 ]")
            player_hand.append(deck.pop())
            print_player_hand(player_hand)
            doubled,ending = True,True
        else:
            print("[ダブルはできません。]")
#
    if get_point(player_hand) > 21:
        print("[プレイヤーはバストした]")
        ending = True
#
    if get_point(player_hand) == 21:
        print("[ブラックジャック２１！]")
        ending = True
#
    return doubled,ending
#
##########################################################################
# ディーラーターン
##########################################################################
def dealer_op(deck,player_hand,dealer_hand):
    while get_point(player_hand) <= 21:
        if get_point(dealer_hand) >= 17:
            print("[ディーラー：スタンド ]")
            break
        else:
            print("[ディーラー：ヒット　 ]")
            dealer_hand.append(deck.pop())
        print_dealer_hand(dealer_hand,False)
#
##########################################################################
# ポイント計算
##########################################################################
def get_point(hand):
    result = 0
    ace_flag = False
    for card in hand:

        #Aが含まれているか
        if card[RANK] == 1:
            ace_flag = True

        #ＪＱＫが含まれているか
        if card[RANK] > 10:
            num = 10
        else:
            num = card[RANK]
        result = result + num
#	Aが含まれていて合計が11以下の場合、Aを11とみなして加算
    if ace_flag == True and result <= 11:
        result +=10
    return result
#
##########################################################################
# プレイヤーの手札表示
##########################################################################
def print_player_hand(player_hand):
    print("プレイヤー（",get_point(player_hand),"）：　　　")
    for card in player_hand:
        print("[",card[SUIT],card[RANK],"]")
    print()
#
##########################################################################
# ディーラーの手札表示
##########################################################################
def print_dealer_hand(dealer_hand,uncoverd):
    if uncoverd:
        print("ディーラー（",get_point(dealer_hand),"）：　　　")
    else:
        print("ディーラー（??）：　　　")
#
#uncoverd=TRUE、flagの設定で1枚目は見れる
#uncoverdがFALSEで最初から見れない
    #
    flag = True
    for card in dealer_hand:
        if flag or uncoverd:
            print("[",card[SUIT],card[RANK],"]")
            flag = False
        else:
            print("[ ** ]")
    print()
#
##########################################################################
# デッキ作成
##########################################################################
def make_deck():
    suits = ["S","H","D","C"]
    ranks = range(1,14)
    deck = [(x,y) for x in ranks for y in suits]
    random.shuffle(deck)
    return deck
#
##########################################################################
# メインルーチン
##########################################################################
def main():
    turn = 1
    player_money = 100
#
#   デッキ作成
    deck = make_deck()
    #print(deck)
#
#  デッキを作る
    while(player_money > 0):
#
#   ターンのはじめにターン数と所持金の情報を表示
        print("-"*20)
        print("ターン：",turn)
        print("所持金：",player_money)
        print("-"*20)
#
#   プレイヤーの手札格納用リスト初期化
        player_hand = []
#   ディーラーの手札格納用リスト初期化
        dealer_hand = []
#
#   ベット
        try:
            bet = int(input("ベット額 > "))
        except:
            print("整数で入力してください")
            continue
#   入力値が所持金を超えていたらやり直し
            if bet > player_money:
                print("所持金が不足しています")
                continue
#   入力値がゼロより小さかったらやり直し
            if bet > player_money:
                print("別途できる額は１以上です")
                continue
#
        player_money -= bet
#
#   デッキの残りが１０枚以下ならデッキを再構築＆シャッフル
        if len(deck) < 10:
            deck = make_deck()
#
        for i in range(2):
    #   デッキからプレイヤーの手札へ
            player_hand.append(deck.pop())
    #   デッキからディーラーの手札へ
            dealer_hand.append(deck.pop())

#
#   ターンのはじめにターン数と所持金の情報を表示
        print("-"*20)
#        print(player_hand)
        print_player_hand(player_hand)
#        print(get_point(player_hand))
#        print(dealer_hand)
        print_dealer_hand(dealer_hand,False)
#        print(get_point(dealer_hand))
        print("-"*20)
#
#		プレイヤーターン
        while True:
            op = input("スタンド：1　ヒット：2　ダブル：3>>")
            doubled,ending = player_op(deck,player_hand,op)
            if doubled:
                player_money -= bet
                bet += bet
            if ending:
                break
#
#		ディーラーターン
        dealer_op(deck,player_hand,dealer_hand)
#
#       手札の情報を表示
        print("-"*20)
        print_player_hand(player_hand)
        print_dealer_hand(dealer_hand,True) #ゲーム終了時はディーラーの手蓋すべてを表示
        print("-"*20)
#
        message,player_money = win_lose(dealer_hand,player_hand,bet,player_money)
        print(message)
#
        turn += 1
        input("次のターンへ")
#
    print("-"*20)
    print("ゲームオーバー")
    print("-"*20)

if __name__ == "__main__":
    main()
