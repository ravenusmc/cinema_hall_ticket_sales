#Main file to examine all the CSV data. 

# importing supporting libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


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
  
  #Stacked Bar Chart: Seat Type Preference by Genre – Compare how many VIP vs. Standard seats were sold per genre.
  def seat_preference_by_genre(self):
    genres = self.data['Movie_Genre'].unique()
    seat_types = self.data['Seat_Type'].unique()
    seat_preferences = [] 
    columns = ['Genre', 'Standard', 'VIP','Premium']
    seat_preferences.append(columns)
    for genre in genres:
      rows = [] 
      filtered_df = self.data[self.data['Movie_Genre'] == genre]
      rows.append(genre)
      for seat in seat_types:
        df = filtered_df
        seat_type_df = df[df['Seat_Type'] == seat]
        seat_type_counts = seat_type_df['Seat_Type'].value_counts()
        count = int(seat_type_counts.iloc[0])
        rows.append(count)
      seat_preferences.append(rows)
    print(seat_preferences)
  
  #Boxplot: Ticket Price by Seat Type – Compare prices for different seat types.
  def ticket_price_by_seat_type(self):
    grouped = self.data.groupby("Seat_Type")["Ticket_Price"]
    box_data = []

    for seat_type, prices in grouped:
        summary = {
            "seat_type": seat_type,
            "min": float(prices.min()),
            "q1": float(prices.quantile(0.25)),
            "median": float(prices.median()),
            "q3": float(prices.quantile(0.75)),
            "max": float(prices.max())
        }
        box_data.append(summary)
    print(box_data)
  
  def linear_regression(self):
    # Prepare the data
    X = self.data[["Age"]].values  # Feature matrix
    y = self.data["Ticket_Price"].values  # Target variable
    # Fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    # Predict and display the regression results
    slope = model.coef_[0]
    intercept = model.intercept_
    r_squared = model.score(X, y)
    print(slope)
  
  def build_age_ticket_price_graph(self):
    # Drop rows with missing values in Age or Ticket_Price
    df = self.data[["Age", "Ticket_Price"]].dropna()
    # Reshape data for sklearn
    X = df["Age"].values.reshape(-1, 1)
    y = df["Ticket_Price"].values
    # Fit linear regression model
    model = LinearRegression()
    model.fit(X, y)
    # Create a sorted range of ages for plotting the regression line
    age_range = np.linspace(df["Age"].min(), df["Age"].max(), 100).reshape(-1, 1)
    predicted_prices = model.predict(age_range)
    # Combine into a DataFrame for export to the frontend
    regression_data = pd.DataFrame({
        "Age": age_range.flatten(),
        "Predicted_Ticket_Price": predicted_prices
    })
    # If you want to output as JSON for use in Vue.js
    regression_json = regression_data.to_dict(orient="records")
    print(regression_json)
          

obj = ExamineData()
obj.build_age_ticket_price_graph()
      