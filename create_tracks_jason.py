import pandas as pd
tracksObj={}
tracksObj["none"]=[{"artist":"none"}]
df=pd.read_csv("batch1.csv")
del df["indexOf"]
del df["album"]
del df["year"]
del df["alphaname"]
artists=df["artist"].unique().tolist()
for i in range(len(artists)):
  tracksObj[artists[i]]=[]
for artist in artists:
  sub=df[df["artist"]==artist]
  
  for j in range(len(sub)):
    tracksObj[artist].append(sub.iloc[j].to_dict())
import json
tracks=json.dumps(tracksObj,indent=1)
#tracksLib={}
#tracksLib["tracksLib"]=tracksObj
print(tracks)
