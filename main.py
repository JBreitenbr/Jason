import pandas as pd
df0=pd.read_csv("spoti_data_cleaned.csv")
lst1=df0["album_tracks"].tolist()
lst2=[]
for i in range(len(lst1)):
  lst2.append(lst1[i][0:-1])
df0["album_tracks"]=lst2


del df0["imgUrl"]
del df0["track_id"]
del df0["album_id"]
del df0["artist_id"]

del df0["count"]
for i in range(len(df0)):
  df0.loc[i,"year"]=df0.loc[i,"album_date"][0:4]
bij=pd.read_csv("bij.csv")
df=pd.merge(df0,bij,on="artist",how="inner")
df.sort_values(by=["alphaname","album","year","album_date","indexOf"],inplace=True)
print(df.iloc[16])
df.to_csv("doubled.csv",index=False)
