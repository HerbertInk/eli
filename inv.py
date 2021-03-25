c = float(input("Enter C: "))
t = float(input("Enter time(t): "))
r = float(input("Enter rate(r): "))
n = float(input("Enter n: "))
a = (1 + (r/n))
b = t * n
d = a ** b
p = c * d
print("%.2f"%(p))