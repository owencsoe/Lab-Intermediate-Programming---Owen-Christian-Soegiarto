other_hash = {1:'Python'} 
other_hash[2] = 10

self_hash = {} 
self_hash[2] = other_hash 
self_hash[3] = 4 
self_hash["2"] = self_hash

print(self_hash["2"]["2"][2][2])
