num = float(input("Enter amount to change: "))
# 100 dollar notes
num1 = num//100
# remainder after 100d
num2 = num%100
#50 dollar note
num3 = num//50
# remainder after 50
num4 = num2%50
# 20 dollar notes
num5 = num4//20
#remainder after 20
num6 = num4%20
#notes by 10
num7 = num6//10
#remainder after 10
num8 = num6%10
#notes by 5dollar
num9 = num8//5
#remainder after 5 dollar
num10 = num8%5
#notes by 1 dollar
num11 = num10//1
#remiander by 1 dollar
num12 = num10%1
#cents section
#cents by .25 dollar
num13 = num12//0.25
#remaninder after quarter
num14 = num12%0.25
#dimes
num15= num14//0.1
#remainder after dimes
num16 = num14%0.1
#nickels
num17 = num16//0.05
#remainder
num18 = num16%0.05
#bronzes
num19 = num18//0.01
#remainder
num20 = num18%0.01
print(int(num1), "hundreds")
print(int(num3), "fifties")
print(int(num5), "twenties")
print(int(num7), "tens")
print(int(num9), "five")
print(int(num11), "one")
print(int(num13), "quarter")
print(int(num15), "dimes")
print(int(num17), "nickles")
print(int(num19), "pennies")