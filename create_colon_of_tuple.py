
#8. Write a Python program to create the colon of a tuple.

from copy import deepcopy

tx=('hello',5,[],True)
print(tx)

tx_colon=deepcopy(tx)
tx_colon[2].append(50)

print(tx_colon)
print(tx)
