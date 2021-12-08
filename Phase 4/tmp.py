import numpy as np
import pandas as pd
def temp():
    df = pd.read_excel('Records.xlsx')
    #print(df.head() )
    #blank_row_bool = df.iloc[:,1].isna()
    #print(blank_row_bool)
    opt = 1
    
    data = [[1,2,3,4,5,6,7,7,8,7,6,5]]
    colname = ["Optimization","Chassis Type","Motor Type",	"Battery Type",	"# of Battery",	"Parachute diam",	"Wheel Radius",	"Chassis mass",	"Gear Diameter",	"Fuel Mass",	"Overall time",	"Cost"]
    #print()

    df2 = pd.DataFrame(data, columns=colname)
    D = df.append(df2)
    print(len(data))
    print(D)

    D.to_excel("Records.xlsx")  

    print(df)

    return
temp()
# initial guess

