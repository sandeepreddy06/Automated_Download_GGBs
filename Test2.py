import requests
import pandas as pd
import sys

USG5=''
USG6='USG6.csv'
IAG5=''
IAG6=''


df = pd.read_csv(USG6)
# ROOT_LINK = "https://www.geogebra.org/material/download/format/file/id/"
Max=len(df)

for i in range(Max):
    GGB_LINK = df['GGB_LINK'][i]
    ID = GGB_LINK[-8:]
    fileName = df['Module'][i] + df['Grade'][i] + df['Class'][i] + df['Applet'][i] + "_" + ID + ".ggb"

    myfile = requests.get(GGB_LINK)
    open(fileName, 'wb').write(myfile.content)
    print(f"{fileName} successfully downloaded!")

