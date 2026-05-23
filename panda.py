import pandas
import numpy as np
def main():
    data = pandas.read_csv("data.csv")
    print(data)
    print(data["name"])
    print(data["age"])
    print(data["age"].mean())
    print(data["age"].max())
    print(data["age"].min())
    print(data["age"].std())
    print(data["age"].var())
    print(data["age"].median())
    print(data["age"].mode())
    print(data["age"].quantile(0.25))
    print(data["age"].quantile(0.5))
    print(data["age"].quantile(0.75))