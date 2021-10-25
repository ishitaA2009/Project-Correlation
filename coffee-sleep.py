import plotly.express as px
import csv
import numpy as np
import pandas as pd

def getDataSource(data_path):
    coffee_in_ml = []
    sleep_in_hours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep in hours"]))

    return {"x" : coffee_in_ml, "y": sleep_in_hours}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Coffee in ml and sleep in hours :-  \n--->",correlation[0,1])

def plot_figure():
    with open("cups of coffee vs hours of sleep.csv") as csv_file:
      df = pd.read_csv(csv_file)
      fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours" , color="week")
      fig.show()

def setup():
    data_path  = "cups of coffee vs hours of sleep.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()    
plot_figure()