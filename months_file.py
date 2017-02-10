import pandas as pd

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

start_year = 1998
end_year = 2016

new_data = []

for i in range(start_year, end_year):
    for x in range(12):
        new_data.append(months[x] + " " + str(i))
df = pd.DataFrame(new_data, columns=['month'])
df.to_csv('months.csv')