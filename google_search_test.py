from google import search
import pandas as pd


df = pd.read_csv('/Users/ajinkya/Documents/UROP-FirmDynamics/links.csv')

company_names = df['conml'].values
company_links = df['weburl'].values

new_data = []


for a in range(len(company_names)):
     name = company_names[a]
     if (company_links[a] == "not-found'"):
          i = 0
          list_names = []
          print (name + "\n")
          for url in search(name, stop=5):
               print("[" + str(i) + "]: " + url)
               list_names.append(url)
               i += 1

          user_input = input("Enter link number:")
          if (user_input == 'n'):
               #company_links[a] = "not_found'"
               new_data.append([name, "not_found"])
          elif(user_input == 'q'):
               #company_links[a] = "not-found"
               for x in range(a, len(company_names)):
                    new_data.append([company_names[x], "not_found"])
               break
          else:
               new_data.append([name, list_names[int(user_input)]])
               #company_links[a] = list_names[int(user_input)]
     else:
          new_data.append([name, company_links[a]])

df = pd.DataFrame(new_data, columns=['conml', 'weburl'])
df.to_csv('links.csv')