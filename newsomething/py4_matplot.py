import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1,2,3,4], [1,7,3,5]) #draw on current figure
# plt.show()

# plt.figure(1)
# plt.plot([1,2,3,4], [1,2,3,4])
# plt.savefig("new-fig")

principal = 10000
interest = 0.05

values = []
years = 10

for i in range(years + 1):
    values.append(principal)
    principal = principal + principal*interest


plt.figure(1)

plt.title("comp interest 5%")
plt.xlabel("Years")
plt.ylabel("Cash")
plt.plot(values)
plt.show()