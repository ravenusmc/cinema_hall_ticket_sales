#Main file to examine all the CSV data. 

# importing supporting libraries
import numpy as np
import pandas as pd

class ExamineData():

  def __init__(self):
    self.data = pd.read_csv('./data/cinema_hall_ticket_sales.csv')
  
  #Ticket Sales by Movie Genre – Show how many tickets were sold per genre.
  def ticket_sales(self):
    #group by Movie_Genre then get count. 
    genre_counts = self.data['Movie_Genre'].value_counts()
    print(genre_counts)
    #return genre_counts

  def second_graph(self):

          

obj = ExamineData()
obj.ticket_sales()
      