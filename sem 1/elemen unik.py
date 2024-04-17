def count(list1):
  uniqel = set(list1)
  return len(uniqel)

list1 = ["a", "b", "c", "a", "b", "d"]
jumlahuni = count(list1)
print(f"Unique elements in list: {jumlahuni}")
