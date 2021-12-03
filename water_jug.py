from collections import deque
def water_jug_problem(x,y,target,jug):
    visited=[]
    queue=deque()
    list=[]
    queue.append([0,0])
    while True:
       try:
        list=queue.popleft()
       except:
         print("No solution found!")
         break
       if(list not in visited):
        print(list)
        visited.append(list)
        if(list[jug-1]==target):
            break
        if([x,list[1]] not in visited):
            queue.append([x,list[1]])
        if([list[0],y] not in visited):
            queue.append([list[0],y])
        if([list[0],0]not in visited):
            queue.append([list[0],0])
        if([0,list[1]]not in visited):
            queue.append([0,list[1]])
        if(list[0]+list[1]<=x):
            if([list[0]+list[1],0] not in visited):
                queue.append([list[0]+list[1],0])
        if(list[0]+list[1]<=y):
            if([0,list[0]+list[1]] not in visited):
                queue.append([0,list[0]+list[1]])
        a=list[1]-(x-list[0])
        b=list[0]-(y-list[1])
        if((a>=0 and a<=x) and (b>=0 and b<=y)):
            if([x,a] not in visited):
                queue.append([x,a])
            if([b,y] not in visited):
                queue.append([b,y]) 
       else:
        continue


p=int(input("Enter capacity of JUG A:"))
q=int(input("Enter capacity of JUG B:"))
print("1.JUG A\n2.JUG B")
tar=int(input("Select any jug(1/2):"))
capacity=int(input("Enter target capacity:"))
water_jug_problem(p,q,capacity,tar)
        