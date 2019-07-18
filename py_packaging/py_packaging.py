# -*- coding: utf-8 -*-
import pandas as pd

"""Main module."""
def hello_pypackage():
	print("Hello there  {{cookiecutter.location}} !") 
	file = pd.read_csv("../data/example.csv", sep=";", encoding="utf-8", header=None)
	print(file)
	
	
if __name__ == '__main__':
	hello_pypackage()