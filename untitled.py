








class Person(object):
	def __init__(self, name, age,gender):
		self.name=name
		self.age=age
		self.gender=gender


	def talk(self):
		print "Hi I'm talking"

	def changeAge(self, newAge):
		self.age = newAge


Gaya= Person("Gaya",15,"female")
print Gaya.age # Age befor we change
print Gaya.name

Gaya.changeAge(16)

print Gaya.age # after















class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
			self.sound=sound
			self.name=name
			self.age=age
			self.favorite_color=favorite_color
	

	def eat(self,food):
		print("Yummy!! "+self.name+" is eating "+food)

	def make_sound(self):
		i=0
		for i in range(3):
			print(self.sound)




simba = Animal("rawr","Simba",5,"red")

simba.eat("meet")
simba.make_sound()




class Dog(Animal):
	def __init__(self,owners):
		Animal.__init__(self)
		self.owners=owners

	def barkOneTime(self):
		print self.sound



cooper= Dog("woof","Cooper",3,"blue")
cooper.make_sound()

cooper.barkOneTime()

















# Functions


def fun1(num1,num2):
	for 
	print (num1+num2)



fun1(4, 7)



class Square
































