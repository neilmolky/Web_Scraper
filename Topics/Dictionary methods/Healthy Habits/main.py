# the list "walks" is already defined
# your code here

distance_walked = sum(walk.get("distance") for walk in walks)
average_distance = distance_walked // len(walks)
print(average_distance)