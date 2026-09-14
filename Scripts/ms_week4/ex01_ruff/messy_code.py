import os,sys
import json
from collections import OrderedDict

def calculate(x,y):
    if x > 0:
        if y > 0:
            return x+y
    return 0

def process_data(data):
    result=[]
    for item in data:
        if item != None:
            result.append(item)
    return result

class MyClass:
    def __init__(self,name,value):
        self.name=name
        self.value=value
    def get_info(self):
        return f"{self.name}: {self.value}"

unused_var = 42
