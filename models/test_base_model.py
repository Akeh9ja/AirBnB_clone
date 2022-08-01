#!/usr/bin/env python3
from base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print("My model before saving")
print("="*20)
print(my_model)

my_model.save()
print("\nMy model after saving")
print("="*20)
print(my_model)


my_model_json = my_model.to_dict()
print("\nJSON of my model:")
for key in my_model_json.keys():
    print("\t{}: ({}) -{}".format(key, type(my_model_json[key]), my_model_json[key]))
