import os
import json

def play():
	print("Escape the Cave of Terror!")
	world.parse_world_dsl()
	player = Player()
	while player.is_alive() and not player.victory:
		room = world.tile_at(player.x,player.y)
		print(room.intro_text())
		room.modify_player(player)
		if player.is_alive() and not player.victory:
			choose_action(room,player)
		elif not player.is_alive():
			"Your Journy has come to an early end."



def choose_action(room,player):
	action = None
	while not action:
		available_actions = get_available_actions(room,player)
		action_input = input("Action: ")
		action = available_actions.get(action_input)
		if action:
			action()
		else:
			print("Invalid action!")


def get_available_actions(room,player):
	
	actions = OrderedDict()
	print("\nchoose an Action: ")
	if player.player_stats:
		action_adder(actions, 'p',player.player_stats, "Print Stats")
	if player.spell_book:
		action_adder(actions, 'sb',player.print_spellbook,"Print Spell Book")
	if player.inventory:
		action_adder(actions, 'i',player.print_inventory,"Print Inventory")
	if isinstance(room,world.TraderTile):
		action_adder(actions,'t',player.trade, "Trade")
	if isinstance(room,world.EnemyTile) and room.enemy.is_alive():
		action_adder(actions, 'a', player.attack,"Attack")
	else:
		if world.tile_at(room.x,room.y -1):
			action_adder(actions,'n', player.move_north,"Go North")
		if world.tile_at(room.x, room.y +1):
			action_adder(actions,'s', player.move_south,"Go South")
		if world.tile_at(room.x + 1,room.y):
			action_adder(actions,'e',player.move_east,"Go East")
		if world.tile_at(room.x -1,room.y):
			action_adder(actions,'w',player.move_west,"Go West")
	if player.hp <100:
		action_adder(actions,'h',player.heal,"Heal")
	if player.mp <100:
		action_adder(actions, 'r', player.mana, "Restore Mana")

	return actions


def action_adder(action_dict,hotkey,action,name):
	action_dict[hotkey.lower()] = action
	action_dict[hotkey.upper()] = action
	print("{}: {}".format(hotkey,name))


play()

