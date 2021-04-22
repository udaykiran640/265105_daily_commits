print("daily commits")
d1 = {"one":1,"two":2,"three":3}
d2 = {"four": 4,"five":5,"six":6}
print(d1)
print(d2)
print(d1.update(d2))
print(d1)

l1 = [1,2,5,8,6]

d3 = {i:l1 for i in l1 }

print(d3)
l1.sort()
print(l1)
print(l1[1])

"""for i in range(len(l1)):
    if(i == len(l1)):
        break

    else:
        
        l1[i] = l1[i+1]

print(l1)"""




