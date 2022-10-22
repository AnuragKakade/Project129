import pandas as pd
 
df=pd.read_csv('dwarf_stars.csv')

df=df[df['Star_name']. notna()]
df=df[df['Distance']. notna()]
df=df[df['Mass']. notna()]
df=df[df['Radius']. notna()]

df['Mass']=df['Mass'].apply(lambda x : float(x))
df['Radius']=df['Radius'].apply(lambda x : float(x))

df['Mass']=0.000954588*df['Mass']
df['Radius']=0.102763*df['Radius']

df.to_csv('cleaned.csv')
