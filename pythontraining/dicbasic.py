d1={}
d2={'spam':2,'eggs':3}
print(d2)
d3={'food':{'ham':1,'egg':2}}
print(d3['food']['egg'])
d4=dict(name='Bob',age=40)
print(d4)
keyslist = ['name', 'age', 'city', 'occupation']
valslist = ['Alice', 30, 'Mumbai', 'Engineer']
d5=dict(zip(keyslist,valslist))
print(d5)
d6=dict.fromkeys(['a','b'])
print(d6)
d7=d2['eggs']
d8=d3['food']['ham']
print(d7,d8)