goal_wood = 312 * 1000
goal_hay = 76.8 * 1000
goal_carrot = 1000


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
	change_hat(Hats.Traffic_Cone)
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

# Wraps func in infinite loop
def repeat(func):
	def inf():
		while True:
			func()
	return inf

entity_to_item = {
	Entities.Pumpkin: Items.Pumpkin,
	Entities.Tree: Items.Wood,
	Entities.Carrot: Items.Carrot,
	Entities.Grass: Items.Hay,
	Entities.Treasure: Items.Gold,
	Entities.Cactus: Items.Cactus,
}

entity_to_pretty = {
	Entities.Pumpkin: "Pumpkins",
	Entities.Tree: "Wood",
	Entities.Carrot: "Carrots",
	Entities.Grass: "Hay",
	Entities.Treasure: "Gold",
	Entities.Cactus: "Cacti",
}

def Harvest(time = None):
	type = get_entity_type()
	item = entity_to_item[type]

	prev = num_items(item)
	harvest()
	new = num_items(item)
	count = new - prev
	
	pretty = entity_to_pretty[type]
	
	harvest_str = "Harvested: " + str(count) + pretty
	
	if time == None:	
		print(harvest_str)
	else:
		time_str = "in " + str(time) + "s"
		rate_str = "("+ str(count/time) + pretty + "/sec)"
		print(harvest_str, time_str, rate_str)
	return count
