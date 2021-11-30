import random
import time



class Game:

    def __init__(self):
        self.player_win = False
        self.carts = self.shuffle()
        player_play = input('Do You wanna play')
        if player_play == 'YES' or player_play == 'yes' or player_play == 'ok' or player_play == 'OK' or player_play == 'okey' or player_play == 'OKEY':
            player_play = True
        else: player_play = False

        while player_play:
            if len(self.carts)< 20:
                self.carts = self.shuffle()
                print('THE CARD IS SHUFFLING')
                time.sleep(1)
            self.dealer = []
            self.player = []
            self.play_game()
            result =self.for_player(self.carts)
            if result == None:
                player_play = True
            elif result == True:
                print('YOU WIN THE GAME')
                player_play = self.check_player_wants()
            else:
                print('YOU Lost THE GAME')
                player_play = self.check_player_wants()

    def check_player_wants(self): # KULLANICIYA OYUNU OYNAMASI ICIN SORU SORUYOR
        player_play = input('Do You wanna play')
        if player_play == 'YES' or player_play == 'yes' or player_play == 'ok' or player_play == 'OK' or player_play == 'okey' or player_play == 'OKEY':
            return True
        else:
            return False

    def check_winner(self): # OYUNUN SONUCUNU GOSTERIYOR
        if sum(self.dealer) > 21:
            return True
        elif sum(self.dealer)< sum(self.player):
                return True
        elif sum(self.dealer) == sum(self.player):
            if len(self.player) < len(self.dealer) and len(self.dealer)==2:
                return True
            elif len(self.player) ==2 and len(self.dealer) ==2 :
                return None
            else:
                return False
        else:
            return False

    def play_game(self): # KARTLAR DAGITILIYOR

        self.player.append(self.carts[0])
        self.dealer.append(self.carts[1])
        self.player.append(self.carts[2])
        self.dealer.append(self.carts[3])
        self.carts.pop(0)
        self.carts.pop(0)
        self.carts.pop(0)
        self.carts.pop(0)
        '''
        print(self.player)
        print(self.dealer)
        '''


    def for_player(self, carts): # KULLANININ OYUNU OYNAMASI SAGLAYAN KOD
        result = None
        self.player = self.show_hands_for_user()

        self.game= True
        while self.game:

            if sum(self.player) == 21: # ELI 21 E ESITSE KULLANICI DAHA FAZLA KART SECEMIYOR
                result = self.check_winner() # OYUNU KIM KAZANDI ONU KONTROL EDIYOR
                self.game = False
                print('YOU WIN')
            elif sum(self.player) < 21 : # 21 ALTINDA ELI OLDUGU ICIN KULLANICININ ,KART CEKMESI VEYA ELINI DURDURMASI GEREK BU YUZDEN SORU SORULUYOR

                print('If You want to hit the card , write "HIT" \nIf You want to stop , write "STOP" ')
                user = input('YOUR RESULT:')
                if user == "HIT":
                    self.player.append(self.carts[0])

                    self.carts.pop(0)
                    self.player = self.show_hands_for_user()
                elif user == "STOP": # DUR DEDIGI ICIN SIRA RAKIBE GECIYOR
                    result = self.dealer_game() # DEALER IN SIRASI
                    self.game = False

            else:
                result = False
                self.game = False
                print('YOU LOST')
        return result
    def dealer_game(self):
        result = None
        self.dealer = self.show_hands_for_dealer() # DEALER ELINDEKI KARTLARDAKI A VE 1 DURUMA GORE SEKIL VEREN FONKSIYON
        game = True
        while game:
            if sum(self.dealer) >= 17: # DEALIRIN ELI 17 OLUR VEYA 17 YI GECER GECMEZ DESTEYE HIT ATMAYI BIRAKIYOR DEALER
                result = self.check_winner()
                game = False

            elif sum(self.dealer) < 17 : # KUCUKSE EGER ELI EN AZ 17 OLUNCAYA KADAR KART CEKMEYE DEVAM EDIYOR

                self.dealer.append(self.carts[0])
                self.carts.pop(0)
                self.dealer = self.show_hands_for_dealer()
                game = True
            print(f"\nTOTAL :  {sum(self.dealer)}")
        return result

    def show_hands_for_dealer(self):

        print('user =', end=' ')
        self.total_player = 0

        x = sum(self.dealer)
        if x > 21:
            for spot2, j in enumerate(self.dealer):
                if j == 11:
                    self.dealer[spot2] = 1
                    break


        elif x <= 11:
            for spot2, j in enumerate(self.dealer):
                if j == 1 :
                    self.dealer[spot2] = 11
                    break
        for i in self.player:
            print(i, end=' ')
        print(f"\nTOTAL :  {sum(self.player)}", end=' ')
        self.total_dealer = sum(self.dealer)

        print(f'\nDealer = ', end=' ')
        for i in self.dealer :
            print(i,end=' ')


        return self.dealer

    def show_hands_for_user(self,):

        print('user =',end="  ")
        x = sum(self.player)
        if x > 21:
            for spot2, j in enumerate(self.player):
                if j == 11 :
                    self.player[spot2] = 1
                    break

        elif x <= 11:
            for spot2, j in enumerate(self.player):
                if j == 1:
                    self.player[spot2] = 11
                    break
        for i in self.player:
            print(i,end=' ')

        print(f"\nTOTAL :  {sum(self.player)}",end=' ')
        self.total_dealer = self.dealer[1]
        print(f'\nDealer =  X {self.dealer[1]}',end=' ')
        print(f"\nTOTAL :  {self.total_dealer}")

        return self.player


    def shuffle(self): # desteyi karan fonksiyon
        while True:
            try:
                decks = int(input('HOW MANY DECK DO YOU WANNA PLAY '))

                self.carts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1] * decks
                break
            except ValueError:
                print('GET IN NUMBER')


        self.carts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1] * decks
        num = 0

        for _ in self.carts:
            x = random.randint(0, len(self.carts) - 1)

            z = self.carts[num]
            self.carts[num] = self.carts[x]
            self.carts[x] = z
            num += 1
        return self.carts

Game()


