import pandas as pd
df0=pd.read_csv("brock1_cleaned.csv")
pt=pd.read_csv("brock2_cleaned_pt1.csv")


pt.drop_duplicates(inplace=True)
gr=pd.DataFrame(pt["track_id"].value_counts())
dupli=gr[gr["count"]>1].index.tolist()
df0=pd.concat([df0,pt])
df0.reset_index(inplace=True)
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
df.to_csv("batch1_ex.csv",index=False)
