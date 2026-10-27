s1 = {1,2,3,4,5,5,3,2,1}
print(s1)

s1.add(6)
print(s1)

s1.add(5)
print(s1)

s1.clear()
print(s1)

s2 = {1,2,3,2,1}
s3 = s2.copy()
print(s2)
print(s3)

s3.add(4)
s3.add(5)
print(s3.difference(s2))
print(s2.difference(s3))

# s2.difference_update(s3)
# print(s2)

s3.difference_update(s2)
print(s3)

