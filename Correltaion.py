import plotly.express as px
import csv
import numpy as np

def getData(pathData):
    marksObtainedByStudent = []
    totalDaysPresent = []
    with open(pathData) as f:
        df = csv.DictReader(f)
        for row in df:
            marksObtainedByStudent.append(float(row["Marks In Percentage"]))
            totalDaysPresent.append(float(row["Days Present"]))
    return{'x' : marksObtainedByStudent, 'y' : totalDaysPresent}
def findCorrelatedData(dataSource):
    correltaion = np.corrcoef(dataSource['x'],dataSource['y'])
    print(correltaion[0,1])        
def setUp():
    pathData = 'Student Marks vs Days Present.csv'
    dataSource = getData(pathData)
    findCorrelatedData(dataSource)   

setUp()    