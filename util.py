import config

def needsSoil(type):
	if type == Entities.Carrot:
		return True
	return False


def make_till():
	if get_ground_type() != Grounds.Soil:
		till()

# Tills the whole Farm
def till_farm():
	for ii in range(get_world_size()):
		for i in range(get_world_size()):
			# Lets harvest what we can to not waste
			#if can_harvest():
			harvest()
	
			if get_ground_type() != Grounds.Soil:
				till()
			move(North)
		move(East)
	print("Done ")

def reset_position():
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)

def plant_tree():
	if (
		get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0
	) or (get_pos_x() % 2 == 1 and get_pos_y() % 2 == 1):
			plant(Entities.Tree)
	else:
		plant(Entities.Grass)

def try_water():
	if get_ground_type() != Grounds.Soil:
		return
	if num_items(Items.Water) < get_world_size() * get_world_size():
		return

	level = get_water()
	for i in range((1 - level) // 0.50):
		use_item(Items.Water)
	#print("new", get_water())

def plantNext():
	#if num_items(Items.Carrot) > config.goal_carrot:
	#	return plant(Entities.Pumpkin)
	if num_items(Items.Wood) > config.goal_wood:
		return plant(Entities.Carrot)
	else:
		plant_tree()
	
def random_elem(list):
	index = random() * len(list) // 1
	return list[index]

def random_hat():
	change_hat(
		random_elem([
			Hats.Brown_Hat,
			Hats.Gray_Hat,
			Hats.Green_Hat,
			Hats.Purple_Hat,
			Hats.Traffic_Cone,
		])
	)

def Harvest():
	type = get_entity_type()
	item = entity_to_item[type]

	prev = num_items(item)
	harvest()
	new = num_items(item)
	print("Harvested: ", new - prev, type)
