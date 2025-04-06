#Main file to examine all the CSV data. 

# importing supporting libraries
import numpy as np
import pandas as pd

class ExamineData():

  def __init__(self):
    self.data = pd.read_csv('./data/cinema_hall_ticket_sales.csv')
  
  def test(self):
    print(self.data.head())
          

obj = ExamineData()
obj.test()
      