# array <> set
t001 = [4, 5, 6, 7, 20, 30, 21]
t010 = set(range(1, 31))
t002 = set(t001)

a = {1, 5, 3, 7}
b = {1, 3, 4, 5}

# set union
c = a | b
print(c)

# set intersection
c = a & b
print(c)

# set difference
c = a - b
print(c)

set001 = set()
set001.add(12)
set001.add(20)
set001.add(3)
set001.add(3)
print(set001)

set002 = set(range(1, 31))
print(set002)
print(set002 - set001)
