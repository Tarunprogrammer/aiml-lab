import statistics

data=input("Enter data separated by comma:")
data=[int(x) for x in data.split(',')]
mean=statistics.mean(data)
median=statistics.median(data)
mode=statistics.mode(data)
std_dev=statistics.stdev(data)
variance=statistics.variance(data)
print(f"mean={mean}")
print(f"median={median}")
print(f"mode={mode}")
print(f"standard Deviation={std_dev}")
print(f"variance={variance}")