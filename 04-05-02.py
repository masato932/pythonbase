#coding:utf-8

# for a in range(1,10+1):
#   print(a)
#   if a % 2 == 0:
#     print("〇")
#   if a % 3 == 0:
#     print("×")
#   if (a % 2 == 0) and (a % 3 == 0):
#     print("▲")

# for a in range(1,20+1):
#   print(a)
#   if (a % 12 == 0):
#     print("〇")
#   elif (a % 4 == 0):
#     print("△")
#   elif (a % 2 == 0):
#     print("×")
#   else:
#     print("☆")

total = 0
a = 1
while True:
  total = total + a
  a = a + 1
  if total > 50:
    break
print(total)