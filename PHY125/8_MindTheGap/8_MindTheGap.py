# ---------------------------------------------------------------------------
# Mind the gap assignement
#
# Modul:   PHY125
# Author:  Tino Heuberger
# Email:   tino.heuberger@uzh.ch
# ---------------------------------------------------------------------------
import csv

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

    def GetRowForCountry(self,country):
        curRow=0
        for row in self.CsvReader:
            if country in row[0]:
                return row
            curRow += 1            

populationFile = WBCsvFile('data/wb-popul.csv')
print(populationFile.GetHeaderRow())
print(populationFile.GetRowForCountry("Azerbaijan"))
