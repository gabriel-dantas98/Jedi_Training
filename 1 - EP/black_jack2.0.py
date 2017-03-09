from random import randint

playerHand = []
dealerHand = []


def playGame():
    
    print('-------------------------WELCOME TO-------------------------\n')
    print('-------------------------BLACK JACK-------------------------\n')
    playerHand.clear()
    dealerHand.clear()

    firstRound()
    HitStand()

def firstRound():
    
    dealerVisible = False

    addCardHand(2,'player')
    addCardHand(2,'dealer')

    showCards('player', dealerVisible)
    showCards('dealer', dealerVisible)

    JQK= [11,12,13]

    for i in range(0,2):
        for j in range(0,2):
            if(playerHand[i][0] == 1 and playerHand[j][0] in JQK):  
                print("\n*********FIRST HIT WIN*******\n")
                print("\nGAME OVER -- 21 -- PLAYER-WINS\n")
                game_loop()
            elif(dealerHand[i][0] == 1 and dealerHand[j][0] in JQK):
                dealerVisible = True 
                print("\n*********FIRST HIT WIN*******\n")
                showCards('dealer', dealerVisible)
                print("\nGAME OVER -- 21 -- DEALER-WINS\n")
                game_loop()

def HitStand():
    
    dealerVisible = False

    Hit = True

    while(Hit == True):
        user_choice = input("\n(H)IT OU (S)TAND ?\t")
        if(user_choice == 'H' or user_choice == 'h'):
            addCardHand(1,'player')
            playerS = sumCards()
            showCards('ambos', dealerVisible)
            Hit = twentyOne(playerS[0], playerS[1])

        elif(user_choice == 'S' or user_choice == 's'):
            Hit = False
            dealerVisible = True
            dealerS = sumCards()
            while(dealerS[1] < 16): 
                addCardHand(1,'dealer')
                dealerS = sumCards()
                showCards('dealer', dealerVisible)
            if(dealerS[1] >= 21):
                twentyOne(dealerS[0],dealerS[1])
            elif(dealerS[1] < 21):
                dif(dealerS[0],dealerS[1])

def giveCard():
    
    NumberCard = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    NipeCard = ["C","P","O","E"]

    Number = NumberCard[randint(0,12)]
    Nipe = NipeCard[randint(0,3)]

    Card = (Number, Nipe)

    return Card

def addCardHand(n,p):
    
    Card = giveCard()

    if(p == 'player'):
        for i in range(0, n):
            while(Card in playerHand):
                Card = giveCard()
            if((Card in playerHand) == False and (Card in dealerHand) == False):
                playerHand.append(Card)
    if(p == 'dealer'):
        for j in range(0, n):
            while(Card in dealerHand):
                Card = giveCard()
            if((Card in dealerHand) == False and (Card in dealerHand) == False):
                dealerHand.append(Card)

def showCards(p, dealerVisible):
    
    exibitionCards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']

    if(p == "player"):
        for i in range(len(playerHand)):
            if (i == 0):
                print('\nYOU ->', end = " ")
            print(exibitionCards[playerHand[i][0] - 1], playerHand[i][1], "|", end = " ")

    if(p == "dealer"):
        print('\nDEALER ->', end = " ") 
        for j in range(len(dealerHand)):
            if(dealerVisible == True):
                print(exibitionCards[dealerHand[j][0] - 1], dealerHand[j][1], "|", end = " ")
            elif(j <= 0 and dealerVisible == False):
                print(exibitionCards[dealerHand[0][0] - 1], dealerHand[0][1], "|", "?\n") 

    if(p == "ambos"):
        for k in range(len(playerHand)):
            if (k == 0):
                print('\nYOU ->', end = " ")
            print(exibitionCards[playerHand[k][0] - 1], playerHand[k][1], "|", end = " ")

        for y in range(len(dealerHand)):
            if(y == 0):
                print('\nDEALER ->', end = " ")
                if(dealerVisible == True):
                    print(exibitionCards[dealerHand[y][0] - 1], dealerHand[y][1], "|", end = " ")
                elif(y < 2 and dealerVisible == False):
                    print(exibitionCards[dealerHand[0][0] - 1], dealerHand[0][1], "|", "?")
                    return dealerVisible

def sumCards():
    
    valorCards = [1,2,3,4,5,6,7,8,9,10,10,10,10]

    totalDealer = 0
    totalPlayer = 0

    for i in range(len(playerHand)):
       totalPlayer += valorCards[playerHand[i][0] - 1]

    for j in range(len(dealerHand)):
        totalDealer += valorCards[dealerHand[j][0] - 1]

    return totalPlayer,totalDealer


def twentyOne(totalPlayer,totalDealer):

    dealerVisible = False

    if totalPlayer == 21 or totalDealer > 21:
        print('\nTOTAL => Dealer ->', totalDealer,'Player ->', totalPlayer)
        print('\nGAME OVER -- 21 -- PLAYERWINS')
        return False

    elif totalDealer == 21 or totalPlayer > 21:
        print('\nTOTAL => Dealer ->', totalDealer,'Player ->', totalPlayer)
        print('\nGAME OVER -- 21 -- DEALERWINS')
        return False

    elif totalDealer == 21 and totalPlayer == 21:
        print('\nTOTAL => Dealer ->', totalDealer,'Player ->', totalPlayer)
        print('\nGAME OVER -- 21 -- DEALERWINS')
        return False

    else:
        return True

def dif(totalPlayer,totalDealer):
    
    dealerVisible = True
    difPlayer = abs(totalPlayer - 21)
    difDealer = abs(totalDealer - 21)

    if(difDealer < difPlayer):        
        showCards('dealer', dealerVisible)
        print('\nDIF => Dealer ->', difDealer, 'Player ->', difPlayer)
        print('\nGAME OVER -- 21 -- DEALERWINS')
        return False
    elif(difPlayer < difDealer):        
        showCards('dealer', dealerVisible)
        print('\nDIF => Dealer ->', difDealer, 'Player ->', difPlayer, "\n")
        print('\nGAME OVER -- 21 -- PLAYERWINS')
        return False
    else:
        return True

def dif(totalPlayer,totalDealer):
    
    dealerVisible = True
    difPlayer = abs(totalPlayer - 21)
    difDealer = abs(totalDealer - 21)

    if(difDealer < difPlayer):        
        showCards('dealer', dealerVisible)
        print('\nDIF => Dealer ->', difDealer, 'Player ->', difPlayer)
        print('\nGAME OVER -- 21 -- DEALERWINS')
        return False
    elif(difPlayer < difDealer):        
        showCards('dealer', dealerVisible)
        print('\nDIF => Dealer ->', difDealer, 'Player ->', difPlayer, "\n")
        print('\nGAME OVER -- 21 -- PLAYERWINS')
        return False
    else:
        return True

def game_loop():
    is_running = True
    while is_running:
        user_choice = input('\nLet.s Play? (S)im - (N)ão \n')
        if user_choice == 'S' or user_choice == 's':

           playGame()

        elif user_choice == 'N' or user_choice == 'n':
            print('Tchau!')
            is_running = False

if __name__ == "__main__":
    game_loop()
