import pandas as pd
import numpy as np

def changeLine (lines):
    lines = [line.replace("http://", "") for line in lines]
    lines = [line.replace("www.", "") for line in lines]  # May replace some false positives ('www.com')
    #urls = [url.split('/')[0] for url in lines.split()]
    return lines


df = pd.read_csv('/Users/ajinkya/Desktop/HG_urlcheck.csv')

clientUrl = changeLine(df['Client URL'].values)
checkUrl = changeLine(df['URL'].values)

count = 0

ind = []

for i in range (len (checkUrl)):
    if (not(clientUrl[i] == checkUrl[i])):
        count += 1
        ind.append(i)

print(count)

dataWrong = []

for i in range (count):
    print ('cl: ' + clientUrl[ind[i]] + ' : ' + 'ch:' + checkUrl[ind[i]])
    dataWrong.append([clientUrl[ind[i]], checkUrl[ind[i]]])



df = pd.DataFrame(dataWrong, columns=['Client URL', 'Check URL'])

df.to_csv('wrong.csv')