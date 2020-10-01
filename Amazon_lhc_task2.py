# #----------  problem 2  ----------#
# Given a list of all railroads connecting pairs of cities,
# output whether it's possible to travel from an origin city to a destination city by train
 
# #----------  method signature  ----------#
# public boolean canTravel(String[][] railroads, String originCity, String destinationCity)
 
# #----------  examples  ----------#
# String[][] railroads = {
#     {"Sydney", "Melbourne"},
#     {"Perth", "Sydney"},
#     {"Melbourne", "Brisbane"},
#     {"New York", "Seattle"},
#     {"New York", "San Francisco"},
#     {"San Francisco", "Portland"},
#     {"Seattle", "Portland"},
#     {"Austin", "Seattle"},
# };;
 
# originCity: "Seattle"
# destinationCity: "New York"
# ouput: true
 
# originCity: "San Francisco"
# destinationCity: "Seattle"
# ouput: true
 
# originCity: "Sydney"
# destinationCity: "Seattle"
# ouput: false
 
# originCity: "Seattle"
# destinationCity: "Melbourne"
# ouput: false
 
# originCity: "Perth"
# destinationCity: "Brisbane"
# ouput: true


class treeNode:
	def __init__(self, city, next):
		self.city=city
		self.next=next

	def __repr__(self):
		return "({} | {})".format(self.city, self.next)	



def canTravel(railroads, originCity, destinationCity):
	if originCity in [road for roadlist in railroads for road in roadlist]:
		tree=treeNode(originCity, list())
	else: 
		return False	
	return add_new_nodes(tree, railroads, destinationCity)
				


def add_new_nodes(tree, roads, destinationCity):
	to_delete=[]
	for road in roads:
		if road[0]==tree.city:
			new_node=treeNode(road[1], list())
			tree.next.append(new_node)
			to_delete.append(road)

		if road[1]==tree.city:
			new_node=treeNode(road[0], list())
			tree.next.append(new_node)
			to_delete.append(road)

	if len(to_delete)==0:
		return False

	for item in to_delete:
		roads.remove(item)

	for node in tree.next:
		if node.city==destinationCity:
			return True
		else:
			return add_new_nodes(node, roads, destinationCity)		

			
railroads = [
    ["Sydney", "Melbourne"],
    ["Perth", "Sydney"],
    ["Melbourne", "Brisbane"],
    ["New York", "Seattle"],
    ["New York", "San Francisco"],
    ["San Francisco", "Portland"],
    ["Seattle", "Portland"],
    ["Austin", "Seattle"]]


print(canTravel(railroads[:], "San Francisco", "New York"))
print(canTravel(railroads[:], "San Francisco", "Seattle"))
print(canTravel(railroads[:], "Sydney", "Seattle"))
print(canTravel(railroads[:], "Seattle", "Melbourne"))
print(canTravel(railroads[:], "Perth", "Brisbane"))
