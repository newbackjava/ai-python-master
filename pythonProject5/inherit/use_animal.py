from inherit.animal import Animal, Dog, Duck

d1 = Dog('m')
d2 = Dog('m2')
d1.move()
d1.speak()

du1 = Duck('d')
du1.move()
du1.speak()


a1 = Animal('hong')
a2 = Animal('happy')
print(a1.name)
print(a2.name)
a1.move()