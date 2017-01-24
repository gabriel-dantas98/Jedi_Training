from random import randint

def NumberCard():
    
    numVector = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    randomCardNumber = (randint(0,12))
    #Gera um numero entre 1 e 12
    
    cardNumber = numVector[randomCardNumber] 
    #Guarda o numero aleatorio da carta em cardNumber

    return (int(cardNumber))

def NipeCard():
        
    nipeVector = ["C","P","O","E"]
    randomNipeCardNumber = (randint(0,3))
    #Gera a nipe da carta

    cardNipe = nipeVector[randomNipeCardNumber] 
    #Guarda o nipe gerado em cardNipe 

    return (str(cardNipe))

def game_loop():
    is_running = True
    while is_running:
        user_choice = input('O que voce quer? (N)umero ou (S)air \n')
        if user_choice == 'N' or user_choice == 'n':
     
            print("\n ===================BLACK JACK===================\n")
            
            iconVector = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K'] #0,12
            deckPlayerNumber = []
            deckPlayerNipe = []
            deckDealerNumber = []
            deckDealerNipe = []

            #Primeira Rodada
            rodada = 1
            if(rodada == 1):
                cartas = 0
                while cartas < 2:
                    deckPlayerNumber.append(NumberCard())
                    deckPlayerNipe.append(NipeCard())
                    deckDealerNumber.append(NumberCard())
                    deckDealerNipe.append(NipeCard())
                    cartas += 1
            
                                    
            print ('YOU \t',str(iconVector[deckPlayerNumber[0] - 1]) + deckPlayerNipe[0], str(iconVector[deckPlayerNumber[1] - 1]) + deckPlayerNipe[1])
            
            print ('DEALER \t',str(iconVector[deckDealerNumber[0] - 1]) + deckDealerNipe[0], '?')


            if(deckPlayerNumber[0] == 1):
                if(deckPlayerNumber[1] == 11 or deckPlayerNumber[1] == 12 or deckPlayerNumber[1] == 13):

                    print("\n *****$$$$****21*****$$$$*****\n")
                    print("\n *****$$$$*********PLAYER WINS********$$$$*****\n")
                    

            if(deckDealerNumber[0] == 11 or deckDealerNumber[0] == 12 or deckDealerNumber[0] == 13):
                if(deckDealerNumber[1] == 1):
                    print ('DEALER \t\n',str(iconVector[deckDealerNumber[0] - 1]) + deckDealerNipe[0], str(iconVector[deckDealerNumber[1] - 1]) + deckDealerNipe[1])
                    
                    print("\n *****$$$$****21*****$$$$*****\n")
                    print("\n *****$$$$*********DEALER WINS********$$$$*****\n")
            
            rodada = 2

            limitPlayer = 0
            limitDealer = 0

            for i in range (0,21):
                hit_stand = input('(H)it ou (S)tand\n')
                if hit_stand == 'H' or hit_stand == 'h':
                    
                    deckPlayerNumber.append(NumberCard())
                    deckPlayerNipe.append(NipeCard())
                    deckDealerNumber.append(NumberCard())
                    deckDealerNipe.append(NipeCard())
                    
                    limitPlayer = limitPlayer + deckPlayerNumber[i]
                    limitDealer = limitDealer + deckDealerNumber[i]

                    print('Player Hand -> \t', iconVector[deckPlayerNumber[i] - 1],  deckPlayerNipe[i])
                    print('Dealer Hand -> \t', iconVector[deckDealerNumber[0] - 1],  deckDealerNipe[0])

                    print('\nSoma Player', limitPlayer)
                    print('\nSoma Dealer', limitDealer)

                    if limitPlayer > 21:
                        print('PLAYER -> LOSE -$- DEALER -> WINS \.0./ ')
                    elif limitPlayer == 21:
                        print('PLAYER -> WINS -$- DEALER -> LOSE \.0./ ')    
                    elif limitDealer > 21:
                        print('PLAYER -> WINS -$- DEALER -> LOSE \.0./ ')
                    elif limitDealer == 21:
                        print('PLAYER -> LOSE -$- DEALER -> WINS \.0./ ')
             
                if hit_stand == 'S' or hit_stand == 's':
                    j = 0
                    for j in range(0,i):
                        print(iconVector[deckDealerNumber[j] - 1], deckDealerNipe[j], '|', end = " ")
                        j = j + 1 
                        print(iconVector[deckDealerNumber[j] - 1], deckDealerNipe[j], '|', end = " ")
                        j = j + 1
                        print(iconVector[deckDealerNumber[j] - 1], deckDealerNipe[j])
                    
            i += 1
                    
        elif user_choice == 'S' or user_choice == 's':
            print('Tchau!')
            is_running = False

if __name__ == "__main__":
    game_loop()
