import random

# define Player class
class Player:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        
    def attack(self, enemy):
        # calculate damage based on attack and defense stats
        damage = max(0, self.atk - enemy.defense)
        enemy.hp -= damage
        print(f"{self.name} attacks {enemy.name} and deals {damage} damage!")
        if enemy.hp <= 0:
            print(f"{enemy.name} has been defeated!")
        
# define Enemy class
class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        
    def attack(self, player):
        # calculate damage based on attack and defense stats
        damage = max(0, self.atk - player.defense)
        player.hp -= damage
        print(f"{self.name} attacks {player.name} and deals {damage} damage!")
        if player.hp <= 0:
            print(f"{player.name} has been defeated!")
    
# define game function
def game():
    # prompt player to enter their name
    player_name = input("Enter your name: ")
    
    # initialize player and enemy
    player = Player(player_name, 20, 5, 2)
    enemy = Enemy("Dragon", 30, 7, 3)
    
    # game loop
    while player.hp > 0 and enemy.hp > 0:
        # player turn
        print(f"Player HP: {player.hp}    Enemy HP: {enemy.hp}")
        choice = input("Attack or Defend? ")
        if choice.lower() == "attack":
            player.attack(enemy)
        elif choice.lower() == "defend":
            player.defense += 1
            print(f"{player.name} defends!")
        
        # enemy turn
        if enemy.hp > 0:
            enemy.attack(player)
        
    # game over
    if player.hp <= 0:
        print(f"{player.name} has been defeated!")
    elif enemy.hp <= 0:
        print(f"{enemy.name} has been defeated!")
        
# run game
game()
