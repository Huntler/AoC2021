import numpy as np
import pandas as pd

input_file = "./inputs.txt"

#
#
# Exercise 1
directions = ["forward", "up", "down"]
df = pd.read_csv(input_file, sep=" ", names=["Direction", "Units"])

forward = df.loc[df["Direction"] == "forward"]["Units"].sum()
up = df.loc[df["Direction"] == "up"]["Units"].sum()
down = df.loc[df["Direction"] == "down"]["Units"].sum()

final = forward * (down - up)
print(final)

#
#
# Exercise 2: i hate this solution
df.loc[df["Direction"] == "up", "Units"] *= -1
aim = horizontal = depth = 0
for idx, row in df.iterrows():
    if row.Direction == "up" or row.Direction == "down":
        aim += row.Units
    
    else:
        horizontal += row.Units
        depth += aim * row.Units

final = horizontal * depth
print(final)


