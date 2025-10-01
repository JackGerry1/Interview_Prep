# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input()) 

country_stamps = set()

for i in range(N): 
    country_stamps.add(input())
    
print(len(country_stamps))
