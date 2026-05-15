# Given list: [45, 78, 12, 89, 34, 67, 23]
# Find the maximum number WITHOUT using max() function
# Use loop and if condition
n= [45, 78, 12, 89, 34, 67, 23]
max=n[0]
for i in range(len(n)):
    if n[i]>max:
        max=n[i]
    print(max)

# Given list: [10, 20, 30, 40, 50]
# Reverse it WITHOUT using reverse() or [::-1]
# Create a new list and use loop
# Expected output: [50, 40, 30, 20, 10]

n=[10, 20, 30, 40, 50]
rev=[]
for i in range(len(n)-1,0,-1):
    rev.append(n[i])
    print(rev)
    

