import pandas as pd
tracksObj={}
tracksObj["none"]=[{"artist":"none"}]
df=pd.read_csv("batch1.csv")
del df["indexOf"]
artists=df["artist"].unique().tolist()[0:2]
for i in range(len(artists)):
  tracksObj[artists[i]]=[]
for artist in artists:
  sub=df[df["artist"]==artist]
  
  for j in range(len(sub)):
    tracksObj[artist].append(sub.iloc[j].to_dict())
import json
tracks=json.dumps(tracksObj,indent=0)
#tracksLib={}
#tracksLib["tracksLib"]=tracksObj
print(tracks)
