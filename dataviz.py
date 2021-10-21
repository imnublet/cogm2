from matplotlib import pyplot as plt
import numpy as np

results = []
# Read results and save as array
for line in open("results.txt", "r"):
    results.append(int(line))

results = np.array(results, dtype=int)
# print results
fig1, ax1 = plt.subplots()
ax1.set_title('Steps it takes to solve Tower of Hanoi')
ax1.boxplot(results)
plt.savefig('boxplot.png')

print 'average steps it takes to complete hanoi', round(results.mean())
print 'Standard Deviation = ', round(results.std())
