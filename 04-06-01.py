#coding:utf-8

# def tashizan(a,b):
#   total = 0
#   for i in range(a,b+1):
#     total = total + i
#   return total

# c = tashizan(1,5)
# print(c)

def tashizan(a,b = 5):
  total = 0
  for i in range(a,b+1):
    total = total + total + i
  return total

c = tashizan(3)
print(c)