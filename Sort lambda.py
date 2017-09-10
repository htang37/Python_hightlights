# Enter your code here. Read input from STDIN. Print output to STDOUT
S = list(raw_input())
S.sort(key = lambda x: (0 if x.islower() else 1 if x.isupper() else 2 if int(x)%2!=0 else 3, x))
print ''.join(S)
