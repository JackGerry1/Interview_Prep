# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(input())
BC = int(input())

res = math.degrees(math.atan2(AB, BC))

print(f"{round(res)}{chr(176)}")



