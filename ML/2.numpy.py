import numpy as np
rows=int(input("Enter number of rows:"))
cols=int(input("Enter number of columns:"))
elements=list(map(float,input(f"Enter{rows*cols} elements separated by spaces:").split()))

user_array=np.array(elements).reshape(rows,cols)
ones_array=np.ones((rows,cols))
zeros_array=np.zeros((rows,cols))
transposed_array=np.transpose(user_array)

reshaped_array=user_array.reshape(rows*cols)
min_value=np.min(elements)
max_value=np.max(elements)

print("User Array:\n",user_array)
print("Ones Array:\n",ones_array)
print("Zeros Array:\n",zeros_array)
print("Transposed Array:\n",transposed_array)
print("Reshaped Array (flattened):\n",reshaped_array)
print("Minimum Value:",min_value)
print("Maximum Value:",max_value)
