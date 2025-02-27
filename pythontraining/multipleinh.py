class Father:
    print("Im the father")
    def earn(self):
        return "Father can earn"
class Mother:
    print("Im the mother")
    def care(self):
        return "Mother takes care"
class Child(Father,Mother):
    print("Im the child")
    def love(self):
        return "Im kid"
child=Child()
print(child.earn())
print(child.care())
print(child.love())
print("************************")
f1=Father()
f1=child
print(f1.love())