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

  #Histogram: Age Distribution – Visualize the age groups of customers.
  def age_graph(self):
    bins = [10, 20, 30, 40, 50, 60]
    labels = ['10-20', '20-30', '31-40', '41-50', '51-60']
    # Create an age group column
    self.data['Age_Group'] = pd.cut(self.data['Age'], bins=bins, labels=labels, right=True, include_lowest=True)
    # Get the age group distribution
    age_group_distribution = self.data['Age_Group'].value_counts().sort_index()
    print(age_group_distribution)
  
  #Proportion of Repeat Customers – Show how many customers purchased again.
  def repeat_customers(self):
    data_list =[]
    value_list = ['Yes', 'No']
    for value in value_list:
      rows = []
      filtered_df = self.data[self.data['Purchase_Again'] == value]
      count_df = filtered_df['Purchase_Again'].value_counts()
      count = int(count_df.iloc[0])
      rows.append(value)
      rows.append(count)
      data_list.append(rows)
    print(data_list)
          

obj = ExamineData()
obj.repeat_customers()
      