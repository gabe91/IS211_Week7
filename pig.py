import argparse
import random


def throw_the_die(sides=6):


    return random.randint(1, sides)



class player2:

    def __init__(self, name):
        self.name = name 
        self.total = 0
        self.comp_total = 0
    def __str__(self):
        return f"{self.name}"

    def round(self):
        
        if self.total < 20:
            die = throw_the_die()
            print(f"player2 rolls {die}")
            if die != 1:
                self.total += die
                print(f"Round score is {self.total}")
                self.round()
                self.total = 0
            else: 
                ("You pigged it")
                self.total = 0
                self.comp_total += self.total
                print(f"player2 total is {self.comp_total}")
        else:
            print("player2 holds")
            self.comp_total += self.total
            print(f"player2 total {self.comp_total}")
            self.total = 0

        
class Player:

    def __init__(self, name):
        self.name = name
        self.total = 0
        self.turn_total = 0


    #def show(self):
    #    return(f"{self}")

    def __str__(self):
        return f"{self.name}'s total = {self.total}"

    def turn(self):

        roll_hold = 'r'
        
        while roll_hold != "h":
            #die = throw_the_die()

            roll_hold = input("Roll(r) or Hold(h)? ").lower()
            if roll_hold == 'h':
                break 
            die = throw_the_die()
            print(f'rolled {die}')

            if die != 1:
                self.total += die
                print(f'Your score for this round is {self.total}')
            else:
                print('You pigged it!')
                self.total = 0
                break
        self.turn_total += self.total
        print(f"Your total score is {self.turn_total}")
        self.turn_total = 0


            

      


        
            

        #self.show()

class Game:
    def __init__(self):
        self.player2 = player2("player 2")
        self.player = Player("Player")

    def choose_player(self):
        rng = random.randint(1, 10)
        if rng < 6:
            print("player2 goes first")
            while self.player2.total < 100 and self.player.total < 100:
                self.player2.round()
                self.player.turn()

            if self.player2.total >= 100:
                print("player2 wins")
            else:
                print("Player wins")
                return
        else:
            print("Player goes first")
            while self.player2.total < 100 and self.player.total < 100:
                self.player.turn()
                self.player2.round()
            if self.player2.total >= 100:
                print("player2 wins")
            else:
                print("Player wins")
                return


    def check_winner(self):


        for player in self.players:

            if player.total >= 100:
                self.winner = player
                return
        
        return False
 
        
   
    def play_game(self):
        current_player = self.players[0]
        while not self.check_winner():
            self.check_winner()
            current_player.turn()




        self.play_game()



def main():
    game = Game()
    game.choose_player()

if __name__ == '__main__':
   main()