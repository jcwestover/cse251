import pickle
from MyClass import Person

person1 = Person("Aaron", 85)
person2 = Person("Brandon", 100)
person3 = Person("Ryan", 75)

with open('grade.dat', 'wb') as f:
    pickle.dump(person1, f)
    pickle.dump(person2, f)
    pickle.dump(person3, f)