n=int(input("Enter number of nodes:"))
s=int(input("Enter source:"))
d=int(input("Enter dest:"))
heiuristic=[]
print("Enter heiuristic values:")
for i in range(n):
    a=int(input())
    heiuristic.append(a)
cost=[]
path=[]
for x in range (n):
    y=[]
    for z in range(n):
        b=int(input())
        y.append(b)
    cost.append(y)
print(cost)
print(heiuristic)
curr=s;
sum=0
path=[]
path.append(s)
while curr!=d:
    min=999
    minval=0
    for i in range(0,n):
     if i!=curr:
        x=heiuristic[i]+cost[curr][i]
        if x<min and i not in path:
            min=x
            minval=i
    sum=sum+min
    curr=minval
    path.append(curr)
print(path)
print("Total cost:",sum)
