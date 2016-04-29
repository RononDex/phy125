# ---------------------------------------------------------------------------
# Mind the gap assignement
#
# Modul:   PHY125
# Author:  Tino Heuberger
# Email:   tino.heuberger@uzh.ch
# ---------------------------------------------------------------------------
import csv
import numpy as np
import matplotlib.pyplot as plt

# This class represents a WorlBand CSV file
class WBCsvFile:
    
    CsvReader = None
    FileName = ""
    HEADER_ROW = 4

    def __init__(self, fileName):
        self.FileName = fileName
        self.ReadCsvFile()
    
    def ReadCsvFile(self):
        fileStream = open(self.FileName, encoding='UTF-8')
        self.CsvReader = csv.reader(fileStream)
        data = self.CsvReader
        return data

    def GetHeaderRow(self):
        curRow = 0
        for row in self.CsvReader:
            if curRow == self.HEADER_ROW:
                return row
            curRow += 1

    def GetNewestValues(self):
        values = []
        curRow = 0
        for row in self.CsvReader:
            if curRow <= self.HEADER_ROW:
                curRow += 1
                continue
            
            if (len(row) > 10 and row[-7] != ""):
                values.append(float(row[-7]))
            else:
                 values.append(0)
            curRow += 1
        return values

    def GetRowForCountry(self,country):
        curRow=0
        for row in self.CsvReader:
            if country in row[0]:
                return row
            curRow += 1            

# THe code for the first task, plottin expected life (From the murder rate) vs population
def Task1():
    # Open the csv files
    populationFile = WBCsvFile('data/wb-popul.csv')
    murderRateFile = WBCsvFile('data/wb-rate.csv')

    # Get the newest values for the population
    population = populationFile.GetNewestValues()
    for x in range(0, len(population)):
        population[x] = float(1E-6)*population[x]

    # Get the newest values for the murder rate per 100'000 inhabitants
    murderRate = murderRateFile.GetNewestValues()
    years = []
    deleteCount = 0

    # Calculate the estimated life expectancy for the different murder rates and population
    for x in range(0, len(murderRate)):
        if (murderRate[x] != 0):
            years.append((1E5) / murderRate[x])
        else:
            del population[x - deleteCount]
            deleteCount += 1

    # Plotting
    logYears = np.log10(years)
    lmin = np.min(logYears)
    lmax = np.max(logYears)
    bins = np.linspace(lmin, lmax, 21)
    bins = 10**bins

    plt.hist(years, bins, weights=population)
    plt.gca().set_xscale('log')

    plt.ylabel("Popultion in millions")
    plt.xlabel("Life expectancy (years)")
    plt.show()

def Task2():
    # Open the csv files
    populationFile = WBCsvFile('data/wb-popul.csv')
    agrarPercentageFile = WBCsvFile('data/wb_agrar.csv')

    population = populationFile.GetNewestValues()
    agrarPercentage = agrarPercentageFile.GetNewestValues()


    plt.plot(population, agrarPercentage, marker='o', ls='')
    plt.xlabel("Population")
    plt.ylabel("Agrar % of GNP")
    plt.show()


Task2()

