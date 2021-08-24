import math
import csv
with open("data.csv",newline="") as f:
  df=csv.reader(f)
  data=list(df)
dataSet=data[0]
total=0
for i in dataSet:
  total=total+int(i)

mean=total/len(dataSet)
print(mean)

squaredList=[]
for i in dataSet:
  a=int(i)-mean
  a=a**2
  squaredList.append(a)

sum=0
for i in squaredList:
  sum=sum+i

std=math.sqrt(sum/(len(dataSet)-1))
print(std)
print(dataSet)

