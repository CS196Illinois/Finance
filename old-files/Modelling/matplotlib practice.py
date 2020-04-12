import matplotlib;import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt




# First, I want to create a bar chart
objects = ('Diana', 'Patina', 'Jesus', 'Vishnue', 'Kresna', 'Budda')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]

# bar means vertical bars,
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('genius level')
plt.title('some talented people in world history')
plt.show()

#while barh means horitontal ones
#But we have to change the positions of objects and performances, otherwise,
#it's ugly
plt.barh(objects, y_pos, align='center', alpha=0.5)
plt.xticks(y_pos, performance)
plt.ylabel('genius level')
plt.title('some talented people in uiuc')

plt.show()





# Second, I want to create a scatterplot
x = np.linspace(0, 10, 30) # we specify its range and points
y = np.cos(x)

plt.plot(x, y, 'o', color='black')
plt.show()

plt.plot(x, y, '-ok') # now we link all the points together
plt.show()






# Last, I want to know how to create pie chart,
# To do this, I asked professor google and it gives me the following response.
# I modified some of it.
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [24, 30, 45, 1]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow= True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
