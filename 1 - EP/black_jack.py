from random import randint


playerHand = []
dealerHand = []

def addCardHand(n, player):

    if(player):
        if(Card in playerHand):
            for i in range(0,n):
                playerHand.append(Card)
        elif
            giveCard()
    elif(dealer):
        if(Card in playerHand):
            for i in range(0,n):
                dealerHand.append(Card)
        elif
            giveCard()
            
def giveCard():

    
    NumberCard = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    NipeCard = ["C","P","O","E"]

    Number = NumberCad[randint(0,12)]
    Nipe = NipeCard[randint(0,3)]

    Card = (Number, Nipe)

    return Card


def newRound():
    
    choice = input("\nDeseja jogar mais uma (S) ou (N)?\n")

    if choice == 'S' or choice == 's':
        game_loop()
    if choice == 'N' or choice == 'n':
        return
        is_running = False 


def NumberCard():
    
    numVector = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    randomCardNumber = (randint(0,12))
    #Gera um numero entre 1 e 12
    
    cardNumber = numVector[randomCardNumber] 
    #Guarda o numero aleatorio da carta em cardNumber

    return (int(cardNumber))
    #Retorna em inteiro o valor da carta

def NipeCard():
        
    nipeVector = ["C","P","O","E"]
    randomNipeCardNumber = (randint(0,3))
    #Gera a nipe da carta

    cardNipe = nipeVector[randomNipeCardNumber] 
    #Guarda o nipe gerado em cardNipe 

    return (str(cardNipe))
    #Retorna como string o digito do nipe


def game_loop():
    is_running = True
    while is_running:
        user_choice = input('\n\nO que voce quer? (N)umero ou (S)air \n')
        if user_choice == 'N' or user_choice == 'n':
     
            print("\n ===================BLACK JACK===================\n")
    
            iconVector = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K'] #
            #Vetor que referencia o numero randomizado com o valor impresso da carta
            calcVector = [1,2,3,4,5,6,7,8,9,10,10,10,10]

            handPlayerNumber = [];
            #Numero das cartas que estão na mão do Player
            handPlayerNipe = []
            #Nipe das cartas que estão na mão do Player
            handDealerNumber = []
            #Numero das cartas que estão na mão do Dealer
            handDealerNipe = []
            #Nipe das cartas que estão na mão do Dealer
            handDealerVisible = False


            #Primeira Rodada
            rodada = 1
            if(rodada == 1):
                cartas = 0
                while cartas < 2:
                    handPlayerNumber.append(NumberCard())
                    handPlayerNipe.append(NipeCard())
                    handDealerNumber.append(NumberCard())
                    handDealerNipe.append(NipeCard())
                    cartas += 1
            
                                    
            print ('YOU \t',str(iconVector[handPlayerNumber[0] - 1]) + handPlayerNipe[0], '|', str(iconVector[handPlayerNumber[1] - 1]) + handPlayerNipe[1])
            
            print ('DEALER \t',str(iconVector[handDealerNumber[0] - 1]) + handDealerNipe[0], '|', '?')


            if(handPlayerNumber[0] == 1):
                if(handPlayerNumber[1] == 11 or handPlayerNumber[1] == 12 or handPlayerNumber[1] == 13):
                    handPlayerNumber[0] = 11
                    print("\n *****$$$$*********PLAYER WINS********$$$$*****\n")
                    break

            if(handDealerNumber[0] == 11 or handDealerNumber[0] == 12 or handDealerNumber[0] == 13):
                if(handDealerNumber[1] == 1):
                    print ('\nDEALER \t',str(iconVector[handDealerNumber[0] - 1]) + handDealerNipe[0], str(iconVector[handDealerNumber[1] - 1]) + handDealerNipe[1])
                    handDealerNumber[0] = 11

                    print("\n *****$$$$*********DEALER WINS********$$$$*****\n")
                    break
                            

            limitPlayer = calcVector[handPlayerNumber[0] - 1] + calcVector[handPlayerNumber[1] - 1]
            limitDealer = calcVector[handDealerNumber[0] - 1] + calcVector[handDealerNumber[1] - 1]
            
            print("p",limitPlayer)
            print("d",limitDealer)
                        
            
            if limitPlayer > 21:
                print('\n$-DEALER -> WINS-$', "\n", 'Dealer =', limitDealer,'Player =', limitPlayer)
                return
            elif limitPlayer == 21:
                print('\n$-PLAYER -> WINS -$', "\n", 'Dealer =', limitDealer,'Player =', limitPlayer)
                return   
            elif limitDealer > 21:
                print('\nPLAYER -> WINS -$', "\n", 'Dealer =', limitDealer,'Player =', limitPlayer)
                return
            elif limitDealer == 21:
                print('\n$-DEALER -> WINS-$', "\n", 'Dealer =', limitDealer,'Player =', limitPlayer)
                return

            for i in range (2,21):
                hit_stand = input('\n(H)it ou (S)tand\n')

                if hit_stand == '\nH' or hit_stand == 'h':
                        
                    handPlayerNumber.append(NumberCard())
                    handPlayerNipe.append(NipeCard())

                    l = 0
                    while(l < len(handPlayerNumber)):
                        if(l == 0):
                            print ('\nYOU \t', end = " ")
                        print(iconVector[handPlayerNumber[l] - 1], handPlayerNipe[l], '|', end = " ")
                        l += 1
                        
                    limitPlayer = limitPlayer + calcVector[handPlayerNumber[i] - 1]

                    if limitPlayer > 21:
                        print('\n$-DEALER -> WINS-$', "\n", 'Dealer =', limitDealer,'Player =', limitPlayer)
                        handDealerVisible = True
                        return
                    elif limitPlayer == 21:
                        print('\n$-PLAYER -> WINS -$', "\n", 'Dealer =', limitDealer,'Player =', limitPlayer)
                        handDealerVisible = True
                        return    
                    elif limitDealer > 21:
                        print('\nPLAYER -> WINS -$', "\n", 'Dealer =', limitDealer,'Player =', limitPlayer)
                        handDealerVisible = True
                        return
                    elif limitDealer == 21:
                        print('\n$-DEALER -> WINS-$', "\n", 'Dealer =', limitDealer,'Player =', limitPlayer)
                        handDealerVisible = True
                        return
                    if limitDealer > 21 and limitPlayer > 21:
                        if(limitDealer == limitPlayer):
                            print('!!!EMPATE!!! - DEALER WINS')
                            handDealerVisible = True
                            return

                    if(handDealerVisible == True):
                        d = 0
                        while(d < len(handDealerNumber)):
                            if(d == 0):
                                print('Dealer \t', end = " ")
                            print(iconVector[handDealerNumber[d] - 1], handDealerNipe[d], "|", end = " ")
                            d+=1
                            handDealerVisible = False
                    else:
                        print('\nDEALER \t', end = " ")
                        print(iconVector[handDealerNumber[0] - 1], handDealerNipe[0], '|', "?", "|", "\n")   
                    

                if hit_stand == 'S' or hit_stand == 's':
                #----- STAND -------#
    
                    limitDealerDif = abs(limitDealer - 21)
                    limitPlayerDif = abs(limitPlayer - 21)          

                    k = 0
                    while(k < len(handDealerNumber)):
                        if(k == 0):
                            print ('DEALER \t', end = " ")
                        print(iconVector[handDealerNumber[k] - 1], handDealerNipe[k], '|', end = " ")
                        k += 1

                    if(limitDealer >= 16 and limitDealer < 21):
                        if limitDealerDif < limitPlayerDif:
                            print('\n$-DEALER -> WINS-$', "\n", 'Dealer - 21 =', limitDealerDif,'Player - 21 =',limitPlayerDif)
                            return
                        elif limitDealerDif > limitPlayerDif:
                            print('\n$-PLAYER -> WINS-$', "\n", 'Dealer - 21 =', limitDealerDif,'Player - 21 =',limitPlayerDif)
                            return  
                    
                    p = 2
                    while(limitDealer <= 16):
                                           
                        handDealerNumber.append(NumberCard())
                        handDealerNipe.append(NipeCard())

                        f = 0
                        while(f < len(handDealerNumber)):
                            if(f == 0):
                                print('\nDEALER \t', end = " ")
                            print(iconVector[handDealerNumber[f] - 1], handDealerNipe[f], '|', end = " ")
                            f += 1

                        limitDealer = limitDealer + calcVector[handDealerNumber[p] - 1]

                        limitDealerDif = abs(limitDealer - 21)
                        limitPlayerDif = abs(limitPlayer - 21)          
 
    
                        if(limitDealer > 16 and limitDealer < 21):
                            if limitDealerDif < limitPlayerDif:
                                print('\n$-DEALER -> WINS-$', "\n", 'Dealer - 21 =', limitDealerDif,'Player - 21 =',limitPlayerDif)
                                return
                            elif limitDealerDif > limitPlayerDif:
                                print('\n$-PLAYER -> WINS-$', "\n", 'Dealer - 21 =', limitDealerDif,'Player - 21 =',limitPlayerDif)
                                return
                        if limitDealer > 21:
                            print('\nPLAYER -> WINS -$', "\n", 'Dealer =', limitDealer,'Player =', limitPlayer)
                            return
                        elif limitDealer == 21:
                            print('\n$-DEALER -> WINS-$', "\n", 'Dealer =', limitDealer,'Player =', limitPlayer)
                            return
                        if limitDealer > 21 and limitPlayer > 21:
                            if(limitDealer == limitPlayer):
                                print('!!!EMPATE!!! - DEALER WINS')

                            return
                   
                        p += 1
                
            #for inicial

        elif user_choice == 'S' or user_choice == 's':
            print('Tchau!')
            is_running = False

if __name__ == "__main__":
    newRound()
