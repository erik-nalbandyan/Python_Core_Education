s = input("Enter ticket number:")
while len(str(s)) != 6 or s.isdigit() == False:
    s = input("You wrote something wrong try again:")
sum1, sum2 = 0, 0
n= s[:3]
m = s[3:]
for i in n:
    sum1 += int(i)
for i in m:
    sum2 += int(i)
if sum1 == sum2:
    print("Congrats!! Your ticket is lucky")
else:
    print("Sorry, you are not lucky")
