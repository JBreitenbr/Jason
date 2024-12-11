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
    sub.to_json("{perf}.json".format(perf=artist),orient="records")
    #txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
    #tracksObj[artist].append(sub.iloc[j].to_dict())
#import json
#tracks=json.dumps(tracksObj,indent=1)
#tracksLib={}
#tracksLib["tracksLib"]=tracksObj
print(tracks)
