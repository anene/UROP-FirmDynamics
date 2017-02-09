from google import search
import pandas as pd


df = pd.read_csv('/Users/ajinkya/Documents/UROP-FirmDynamics/links.csv')

company_names = df['conml'].values
company_links = df['weburl'].values

new_data = []

found = 0

for a in range(len(company_names)):
     if not(company_links[a] == "not_found" or company_links[a] == "not_found-1" or company_links[a] == "not-needed"):
         found += 1


print(found)