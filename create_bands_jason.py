import pandas as pd
s=pd.read_csv("batch1_ex.csv")
del s["index"]
for i in range(len(s)):
  s.loc[i,"maiuscule"]=s.loc[i,"alphaname"].upper()[0]

mlst=s["maiuscule"].unique().tolist()
wlst=[]
for i in range(len(mlst)):
  wlst.append({})
for i in range(len(mlst)):
  wlst[i]["name"]=mlst[i]
  wlst[i]["bands"]=[]
blst=[]
for i in range(len(mlst)):
  hlp=s[s["maiuscule"]==mlst[i]]["artist"].unique().tolist()
  blst.append(hlp)
slst=[[] for i in range(len(mlst))]
for i in range(len(blst)):
  for j in range(len(blst[i])):
    slst[i].append({"name":blst[i][j]})
for i in range(len(wlst)):
  wlst[i]["bands"]=slst[i]
bands=pd.DataFrame(wlst)
#import json
#bands=json.dumps(wlst,indent=2)
#print(bands.iloc[0])
bands.to_json("bandsObj.json",orient="records")

  