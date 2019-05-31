import matplotlib.pyplot as plot 

Year = [2010,2011,2012,2013]
Rice = [10,30,45,30]

plot.xlabel("Year")
plot.ylabel("Rice")
plot.title("Rice Havested Per Annum")
plot.plot(Year,Rice)
plot.show()