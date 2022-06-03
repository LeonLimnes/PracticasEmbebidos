# ## ###############################################
#
# program: plot.py
# Reads a file with temperature records and plots it
# Autor: César Martínez
#        Lisset Noriega Domínguez
# License: MIT
#
# ## ###############################################

import matplotlib.pyplot as plt
#Load temperature data from afile
def loadTemperatureDataFromFile(fileName):
    try:
        with open(fileName,"r") as file:
            data = file.readlines()
            return data
    except Exception as e:
        print(e)

#Extract temp data into a list
def dateTempToList(data):
    dataHour= []
    dataTemp = []
    for line in data:
        arrayData = line.split(" ")
        hour = arrayData[4]
        temp = float(arrayData[6][5:-2])
        dataHour.append(hour)
        dataTemp.append(temp)
    return [dataHour,dataTemp]

def main():
    loadedData = loadTemperatureDataFromFile("temp.log")
    dataArrays = dateTempToList(loadedData)
    
    plt.xticks(rotation = 60)
    plt.plot(dataArrays[0],dataArrays[1])
    plt.show()
main()
