entity_to_item = {
	Entities.Pumpkin: Items.Pumpkin,
	Entities.Tree: Items.Wood,
	Entities.Carrot: Items.Carrot,
	Entities.Grass: Items.Hay,
	Entities.Treasure: Items.Gold,
}


if can_harvest():
	type = get_entity_type()
	item = entity_to_item[type]

	prev = num_items(item)
	harvest()
	new = num_items(item)
	print("Harvested: ", new - prev)