d = {1: 1, 3: 9, 4: 16, 5: 25, 2: 4, 6: 36, 7: 64, 8: 49, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
d1=dict(sorted(d.items())) # by item
print(d1)
print(dict(sorted(d.items(), key= lambda item:item[1]))) # by value
print(dict(sorted(d.items(), key= lambda item:item[0]))) # by key
