import numpy as np
import plotly.express as px
import csv 

def plotfigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x = "Days Present",y = "Marks In Percentage")

        fig . show()

def getdataSource(data_path):
    marks_in_percentage = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return{"x":marks_in_percentage,"y":days_present}

def findcorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation = ",correlation[0,1])

def setup():
    data_path = "data1.csv"
    dataSource = getdataSource(data_path)
    findcorrelation(dataSource)
    plotfigure(data_path)

setup()