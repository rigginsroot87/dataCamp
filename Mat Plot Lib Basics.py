#MATPLOTLIB BASICS

#import statement and alias, define two sample lists
import matplotlib.pyplot as plt
import random as rand
list1 = [1,2,3,4,5]
list2 = [4.0,6.0,8.0,6.0,7.5]
#you can do a line plot with the code below, don't forget the show call
plt.plot(list1,list2)
plt.show()
# clears the plot so you can 
plt.clf()
#you can also do a scatter plot with the following code (doesn't make much sense for the data set we are looking at)
plt.scatter(list1,list2)
plt.show()
plt.clf()
#you can also do a histogram
hist_plot = []
for i in range(600):
  hist_plot.append(rand.weibullvariate(1, 5))
plt.hist(hist_plot)
plt.show()

#OPTIONS FOR PLOTS - Labels & Whatnot
plt.plot(list1,list2)
# set scales on axis: plt.xscale("log")
plt.xlabel("labelx - made up datas")
plt.ylabel("labely - made up datas")
plt.title("THIS CHART SUX")
plt.yticks([2,4,6,8,10],["TWO","FOUR","SIX","EIGHT","TEN"])
plt.xticks([1,2,3,4,5],["T1","T2","T3","T4","T5"])
plt.show()


