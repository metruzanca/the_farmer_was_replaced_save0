def foreach(list, processor):
	for index in range(len(list)):
		item = list[index]
		processor(item, index)

def map(list, mapper):
	new_list = []
	for index in range(len(list)):
		item = list[index]
		res = processor(item, index)
		new_list.append(res)
	return new_list
