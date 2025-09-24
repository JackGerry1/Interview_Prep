# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools 

string = input()

#res = [(len(list(freq)), int(val)) for val, freq in itertools.groupby(string)]

res = ""
for val, freq in itertools.groupby(string): 
    res += ''.join(f'({len(list(freq))}, {int(val)}) ')


print(res)
