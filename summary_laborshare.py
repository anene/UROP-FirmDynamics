import pandas as pd

df = pd.read_csv('/Users/ajinkya/Documents/UROP-FirmDynamics/Compustat-Data/LaborShares.csv')

#cost = rev + profits
#rev = revt
#profits  = gp
#wl = wage*labor supply = xlr
#<2000, 2001-2007, 2008-2015
#first two NAICS digits
#summary stats -> WL/cost, WL/rev

naics_id = df['naics'].values
rev = df['revt'].values
profit = df['gp'].values
year = df['fyear'].values
wl = df['xlr'].values

groups = []

group_data = [] #name, num, year, wl/cost, wl/rev


def put_data(gNum, yr_group, wlc, wlr):
    ind = -1
    for i in range(len(group_data)):
        if (group_data[i][0] == gNum and group_data[i][2] == yr_group):
            ind = i
            break

    group_data[ind][3] += wlc
    group_data[ind][4] += wlr
    group_data[ind][1] += 1

for i in range(len(naics_id)):

    gNum = (str(naics_id[i])[:2])

    if (gNum == 'na'):
        gNum = 0

    gNum = int(gNum)

    r = str(rev[i])
    p = str(profit[i])
    w_labor = str((wl[i]))

    yr = int(year[i])

    if (r == "nan"):
        r = 0.0 #prevent divide by 0
    if (p == "nan"):
        p = 0.0
    if (w_labor == 'nan'):
        w_labor = 0.0

    r = float(r)
    p = float(p)
    w_labor = float(w_labor)

    cost = r + p
    if cost <= 0.00001:
        wlc = 0.0
    else:
        wlc = w_labor/cost
    if r <= 0.000001:
        wlr = 0.0
    else:
        wlr = w_labor/r

    if not(gNum in groups):
        groups.append(gNum)
        group_data.append([gNum, 0, 0, 0.0, 0.0])
        group_data.append([gNum, 0, 1, 0.0, 0.0])
        group_data.append([gNum, 0, 2, 0.0, 0.0])

    if (yr < 2000):
        put_data(gNum, 0, wlc, wlr)
    elif (yr >= 2008):
        put_data(gNum, 2, wlc, wlr)
    else:
        put_data(gNum, 1, wlc, wlr)

for i in range(len(group_data)):
    if group_data[i][1] == 0:
        group_data[i][3] = 0.0
        group_data[i][4] = 0.0
    else:

        group_data[i][3] /= group_data[i][1]
        group_data[i][4] /= group_data[i][1]


df = pd.DataFrame(group_data, columns=['NAICS', 'group-size', 'group-yr', 'wlc', 'wlr'])
df.to_csv('/Users/ajinkya/Documents/UROP-FirmDynamics/Compustat-Data/Summary-Labor_Share.csv')
