import enemies
import npc
import random
import time
import items





class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
      
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player): 
        pass

class StartTile(MapTile):
    def intro_text(self):
        return """
        \n You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """
        time.sleep(0.5)


class EnemyTile(MapTile):
    '''            
    def __init__(self, x, y):
    
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.GiantSpider()
            self.alive_text =  "\nA giant spider jumps down from " \
                              "its web in front of you!"
                              
            self.dead_text = "\nThe corpse of a dead spider " \
                             "rots on the ground."
        elif r < 0.80:
            self.enemy = enemies.Ogre()
            self.alive_text = "\n An ogre is blocking your path!"
            self.dead_text = "\nA dead ogre reminds you of your triumph."
        elif r < 0.95:
            self.enemy = enemies.BatColony()
            self.alive_text = "\nYou hear a squeaking noise growing louder" \
                              "...suddenly you are lost in swarm of bats!"
            self.dead_text = "\nDozens of dead bats are scattered on the ground."
        else:
            self.enemy = enemies.RockMonster()
            self.alive_text = "\nYou've disturbed a rock monster " \
                              "from his slumber!"
            self.dead_text = "\nDefeated, the monster has reverted " \
                             "into an ordinary rock."
        
        super().__init__(x, y)
    '''
<<<<<<< HEAD
    def intro_text(self,player):
=======
    def intro_text(self):
>>>>>>> 45bf0b496c1d4f59d90e5c29989043ba435b2ac7
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        '''
        text = txt
        if self.enemy.is_alive():
            txt = self.alive_text
        elif player.attack():
            txt = self.combat_text
        else:
            self.dead_text
        '''
        time.sleep(0.1)
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("{} does {} damage. You have {} HP remaining.".
                  format(self.enemy.name,self.enemy.damage, player.hp))
        if not self.enemy.is_alive():
            player.gold = player.gold + self.enemy.gold
            if self.enemy.gold == 0:
                pass
            player.exp = player.exp + self.enemy.exp
            total_exp = player.exp
            levels = [0,200,450,1012]
            if True:
                current_level = sum(1 for x in levels if x <= total_exp)
                player.player_lvl = current_level
        
                if not self.enemy.is_alive():
                    self.enemy.exp = 0
class CaveMonster(EnemyTile):
    def __init__(self,x,y):
        r = random.randint(1,4)
        if r == 1:
            self.enemy = enemies.GiantRat()
<<<<<<< HEAD
            self.alive_text = "\nLook at that R.O.U.S whats out it has sharp teeth."
=======
            self.alive_text = "\nLook at that ROUS whats out it has sharp teeth."
>>>>>>> 45bf0b496c1d4f59d90e5c29989043ba435b2ac7
            self.dead_text = "\nA body of a dead rat"
        elif r == 2:
            self.enemy = enemies.GiantSpider()
            self.alive_text =  "\nA giant spider jumps down from " \
                              "its web in front of you!"
                              
            self.dead_text = "\nThe corpse of a dead spider " \
                             "rots on the ground."
        elif r == 3:
            self.enemy = enemies.BatColony()
            self.alive_text = "\nYou hear a squeaking noise growing louder" \
                              "...suddenly you are lost in swarm of bats!"
            self.dead_text = "\nDozens of dead bats are scattered on the ground."
        else:
            self.enemy = enemies.RockMonster()
            self.alive_text = "\nYou've disturbed a rock monster " \
                              "from his slumber!"
            self.dead_text = "\nDefeated, the monster has reverted " \
                             "into an ordinary rock."
        
        super().__init__(x, y)

class GoblinScoutTile(EnemyTile):
    def __init__(self,x,y):
        self.enemy = enemies.GoblinScout()
        r = random.random()
        if r < .20:
            self.alive_text = "\nA small goblin jumps out at you its not much to look at..."\
                                "Lookout its got a knife!"
        elif r < 50:
            self.alive_text = "\nOut of a dark recess in the wall jumps a goblin"\
                                " ready to scewer you with his dagger"
        else:
            self.alive_text = "\nYou hear a gutteral voice out of the dark "\
                                "walks a goblin ready for battle!"
        self.dead_text = "\nA dead goblin body."
<<<<<<< HEAD

        super().__init__(x, y)

=======

        super().__init__(x, y)

>>>>>>> 45bf0b496c1d4f59d90e5c29989043ba435b2ac7
class GoblinBasherTile(EnemyTile):
    def __init__(self,x,y):
        self.enemy = enemies.GoblinBasher()
        self.alive_text = "\nLookout a Goblin basher and he is looking for a fight."

<<<<<<< HEAD
        self.combat_text = "\nGoblin Basher flinches back from the attack"

        self.dead_text = "\nThe body of a dead Goblin basher"
=======
        self.dead_text = "\n The body of a dead Goblin basher"
>>>>>>> 45bf0b496c1d4f59d90e5c29989043ba435b2ac7
        super().__init__(x,y)

class KoboldTile(EnemyTile):
    def __init__(self,x,y):
        self.enemy = enemies.Kobold()
        self.alive_text = "\nlook out a kobold harmless one at a time but deadly in groups or to"\
                            " and unsuspecting adventurer"
        self.dead_text = "\nThe dead body of a kobold"
        super().__init__(x,y)
class VictoryTile(MapTile):
    def modify_player(self,player):
    	player.victory = True
    
    def intro_text(self):
        return """
        \nYou see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
        Victory is yours!
        """

class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1, 50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return """
            Another unremarkable part of the cave. You must forge onwards.
            """
        else:
            return """
            Someone dropped some gold. You pick it up.
            """
         
class TrapRoomTile(MapTile):
    def __init__(self, x, y):
        self.trap = items.Trap
        r = random.randint(1,2)
        if r == 1:
            self.trap = items.PitFall()
            self.trap.tripped = True
            
            self.set_text = "\nThe floor in this hallway is unusually clean."
            time.sleep(1)
           
            self.tripped_text = "\nA pitfall trap opens in the tunnel."
        else:
            self.is_tripped = False
            self.set_text = "\nLooks like more bare stone... "

            self.tripped_text = "\nThere is a large hole in the hallway."
        super().__init__(x, y)
    
    def modify_player(self,player):
        if self.trap.is_tripped():
            player.hp = player.hp - self.trap.damage
            print("You stumbled into a trap!")
            time.sleep(1)
            print("\nTrap does {} damage. You have {} HP remaining.".
                  format(self.trap.damage, player.hp))
    
    def intro_text(self):
        text = self.tripped_text if self.trap.is_tripped() else self.set_text
        time.sleep(0.1)
        return text

class EmptyRoomTile(MapTile):
    def intro_text(self):
        r = random.random()
        if r < .10:
            return"""
            Rough hewn stone walls are all you can make out in the flickering tourch light.
            """
        elif r < .30:
            return"""
            There is nothing remarkable in this part of the tunnel keep moving onward!
            """
        elif r < .50:
            return"""
            The dirt in this part of th ecave is scuffed but otherise there is nothing
            remarkable here. best push on.
            """
        elif r < 70:
            return"""
            You've been walking for a while without finding anyone or anything.
            no sense in going back now better keep moving.
            """
        else:
            return"""
            Great more stone... Is that a breeze I feel better keep going.
            """
<<<<<<< HEAD

=======
>>>>>>> 45bf0b496c1d4f59d90e5c29989043ba435b2ac7

class WindObelisk(MapTile):
    def __init__(self,x,y):
        self.obelisk = npc.WindMagicObelisk()
        super().__init__(x,y)

    def check_if_learn_spell(self,player):
        while True:
            print('would ou like to (L)earn this spell? Or leave the obelisk alone (q)')
            user_input = input()
            if user_input in ['Q','q']:
                return
            elif user_input in ['L','l']:
                print("You can learn these spells")
                self.trade(buyer=player,seller=self.obelisk)
            else:
                print("invalid choice")
    def learn_spell(self,buyer,seller):
        for i,spell in enumerate(seller.spell_book,1):
            print("{}. {}".format(i,spell.name))
        while True:
            user_input = input("Choose a spell to learn: ")
            if user_input in ['Q','q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.spell_book[choice - 1]
                    self.swap(seller,buyer,to_swap)
                except ValueError:
                    print("Invalid choice!")
    def swap(self,seller,buyer,spell):
        seller.spell_book.remove(spell)
        buyer.spell_book.append(spell)
        print("you learned the Spell")    
    def intro_text(self):
        return"""
        You find a large strangly illuminated rock obelisk that gives off the 
        feeling of a light breeze mixed with a magical sensation.
        """

class WindObelisk(MapTile):
    def __init__(self,x,y):
        self.obelisk = npc.WindMagicObelisk()
        super().__init__(x,y)

    def check_if_learn_spell(self,player):
        while True:
            print('would ou like to (L)earn this spell? Or leave the obelisk alone (q)')
            user_input = input()
            if user_input in ['Q','q']:
                return
            elif user_input in ['L','l']:
                print("You can learn these spells")
                self.trade(buyer=player,seller=self.obelisk)
            else:
                print("invalid choice")
    def learn_spell(self,buyer,seller):
        for i,spell in enumerate(seller.spell_book,1):
            print("{}. {}".format(i,spell.name))
        while True:
            user_input = input("Choose a spell to learn: ")
            if user_input in ['Q','q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.spell_book[choice - 1]
                    self.swap(seller,buyer,to_swap)
                except ValueError:
                    print("Invalid choice!")
    def swap(self,seller,buyer,spell):
        seller.spell_book.remove(spell)
        buyer.spell_book.append(spell)
        print("you learned the Spell")    
    def intro_text(self):
        return"""
        You find a large strangly illuminated rock obelisk that gives off the 
        feeling of a light breeze mixed with a magical sensation.
        """

class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']:
                return
            elif user_input in ['B', 'b']:
                print("Here's whats available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['S', 's']:
                print("Here's whats available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = int(seller.gold) + int(item.value)
        buyer.gold = int(buyer.gold) - int(item.value)
        print("Trade complete!")


    def intro_text(self):
        return """
        A frail not-quite-human, not-quite-creature squats in the corner
        clinking his gold coins together. He looks willing to trade.
        """

world_dsl = """
<<<<<<< HEAD
|ST|GB|TR|ER|CM|  |ER|ER|ER|  |  |ER|  |  |ER|  |  |  |ER|ER|ER|
=======
|ST|WO|TR|ER|CM|  |ER|ER|ER|  |  |ER|  |  |ER|  |  |  |ER|ER|ER|
>>>>>>> 45bf0b496c1d4f59d90e5c29989043ba435b2ac7
|CM|  |  |  |ER|  |FG|  |ER|  |FG|ER|ER|ER|KT|ER|CM|  |FG|  |CM|
|ER|FG|GS|  |TT|  |  |  |ER|  |  |ER|  |  |  |  |ER|  |  |ER|ER|
|TT|  |ER|KT|CM|ER|CM|ER|GB|  |  |ER|  |  |ER|  |ER|ER|ER|ER|  |
|FG|  |TR|  |FG|  |  |  |ER|GS|ER|KT|ER|GB|TT|ER|CM|  |  |ER|ER|
|ER|GS|ER|  |ER|  |  |  |ER|  |  |ER|  |ER|  |  |ER|  |  |  |ER|
|  |ER|  |ER|TT|TR|KT|ER|CM|  |ER|ER|  |ER|  |ER|ER|  |ER|ER|ER|
|  |ER|  |GB|  |  |ER|  |ER|TT|ER|  |ER|GS|ER|ER|  |  |ER|  |  |
|TR|ER|  |ER|GS|  |CM|  |  |ER|  |  |ER|  |  |ER|  |ER|ER|ER|ER|
|ER|  |  |  |TR|  |ER|ER|ER|GS|ER|ER|ER|  |  |ER|  |ER|  |  |  |
|ER|ER|ER|  |ER|  |ER|  |  |  |  |ER|  |  |ER|TT|ER|ER|ER|  |ER|
|  |  |ER|TT|ER|GS|ER|  |ER|FG|ER|ER|ER|ER|  |ER|  |ER|ER|ER|  |
|FG|  |  |ER|  |ER|  |  |  |ER|ER|  |ER|  |  |  |ER|  |  |  |ER|
|ER|ER|ER|ER|ER|ER|  |ER|  |ER|  |  |ER|ER|ER|TT|ER|ER|  |  |ER|
|ER|  |  |  |  |ER|ER|TT|ER|ER|ER|  |  |  |  |ER|  |ER|ER|ER|TR|
|CM|ER|TT|ER|TR|  |  |ER|  |ER|  |ER|ER|TR|  |ER|  |  |ER|  |ER|
|  |  |ER|  |ER|ER|  |ER|ER|CM|ER|ER|  |ER|ER|CM|ER|  |ER|  |ER|
|ER|  |ER|  |  |ER|  |  |ER|  |  |  |  |ER|  |  |ER|ER|ER|ER|ER|
|ER|ER|CM|ER|  |ER|ER|ER|ER|ER|  |  |  |ER|ER|ER|  |  |VT|  |  |
"""


def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True

tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "FG": FindGoldTile,
                  "TT": TraderTile,
                  "GS": GoblinScoutTile,
                  "GB": GoblinBasherTile,
                  "ER": EmptyRoomTile,
                  "TR": TrapRoomTile,
                  "KT": KoboldTile,
                  "CM": CaveMonster,
                  "WO": WindObelisk,
                  "  ": None}


world_map = []

start_tile_location = None

def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None

