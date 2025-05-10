#!/usr/bin/env python3

class Dog:
   def __init__(self, name,breed = "Mutt"):
       self.name = name
       self.breed = breed
K9 = Dog("K9","Max")
print(K9.name)
print(K9.breed)