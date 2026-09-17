import math

x=int(input("Enter a Number"))
result1=math.ceil(x)
result2=math.factorial(x)
result3=math.exp(x)
result4=math.sqrt(x)2

result5=math.floor(x)
n1=int(input("Enter number1:"))
n2=int(input("Enter Number2:"))
result6=math.gcd(n1,n2)
result7=math.pow(n1,n2)
angle=int(input("Enter an angle:"))
a=math.radians(angle)
result8=math.sin(a)
result9=math.cos(a)
result10=math.tan(a)

print(f"Using math.ceil({x}):{result1}")
print(f"Using math.factorial({x}):{result2}")
print(f"Using math.exp({x}):{result3}")
print(f"Using math.sqrt({x}):{result4}")
print(f"Using math.floor({x}):{result5}")
print(f"Using math.gcd({n1},{n2}):{result6}")
print(f"Using math.pow({n1},{n2}):{result7}")
print(f"Using math.sin({angle}):{result8}")
print(f"Using math.cos({angle}):{result9}")
print(f"Using math.tan({angle}):{result10:.15f}")