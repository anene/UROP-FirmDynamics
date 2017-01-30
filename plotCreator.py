from matplotlib import pyplot as plt
import numpy as np


def createXY(x, y, a, b, nHouse):
    z = np.polyfit(x, y, 2)
    f = np.poly1d(z)

    x_new = np.linspace(x[0], x[-1], b-a)
    y_new = f(x_new)

    zz = sum(nHouse[a:b])
    z = np.polyfit(x_new, y_new, 2, w=[nHouse[i] / zz for i in range(a, b)])

    y_2 = f(x_new)

    return [x_new, y_2]

nHouse = []

file = open('age-distribution.txt', 'r')

for line in file:
    nHouse.append(float(line))


tot = sum(nHouse[:])

for i in range (len(nHouse)):
    nHouse[i] = nHouse[i]/tot

a = [x for x in range(21,91)]
b_o = []

b_o.append([46.7 for x in range(35,45)])
b_o.append([105.3 for x in range(45,55)])
b_o.append([165.9 for x in range(55,65)])
b_o.append([232.1 for x in range(65,75)])

hSize_o = []
hSize_o.append([0.4376003950226 for x in range(21, 25)])
hSize_o.append([0.66845929900893 for x in range(25,35)])
hSize_o.append([0.78612895011823 for x in range(35,45)])
hSize_o.append([0.72484034139346 for x in range(45,55)])
hSize_o.append([0.65684854802189 for x in range(55,65)])
hSize_o.append([0.53870656710713 for x in range(65,91)])

b = []
for i in range(len(b_o)):
    for x in range(len(b_o[i])):
        b.append(b_o[i][x])

hSize = []
for i in range(len(hSize_o)):
    for x in range(len(hSize_o[i])):
        hSize.append(hSize_o[i][x])


vals = []
currentInt = 0

x = [21, 34]
y = [0, 37.6]

xy = createXY(x, y, 21, 35, nHouse)

for i in range(len(xy[1])):
    vals.append(xy[1][i]/(hSize[currentInt]+1))
    currentInt += 1

plt.plot(x,y,'o', xy[0], xy[1])

x = np.linspace(35, 74, num=40)
xy = createXY(x, b, 35, 75, nHouse)


for i in range(len(b)):
    vals.append(b[i]/(hSize[currentInt]+1))
    currentInt += 1


plt.plot(x, b, 'o', xy[0], xy[1])

x = [75, 90]
y = [194.8, 0]

xy = createXY(x, y, 75, 91, nHouse)

for i in range(len(xy[1])):
    vals.append(xy[1][i]/(hSize[currentInt]+1))
    currentInt += 1

plt.plot(x, y, 'o', xy[0], xy[1])


print (vals)

target = open("results.txt", 'w')

x_write = np.linspace(21, 90, num=70)

for i in range(len(vals)):
    target.write(str(x_write[i]) + " | " + str(vals[i]))
    target.write("\n")

target.close()

plt.show()