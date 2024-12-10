from sqlalchemy import create_engine
import pandas as pd
import pymysql

engine = create_engine("mysql+pymysql://root:12345@localhost:3306/member_addr?charset=utf8mb4")
engine.connect()

data = {'hakbun':[2000,2001,2002,2003,2004,2005], 'score':[70,60,50,75,100,85]}
df = pd.DataFrame(data=data, columns=['hakbun', 'score'])

print(df)
df.to_sql(con=engine, name='score_table', index=False, if_exists='replace')
# if_exists= 속성 옵션 -> fail, append, replace -> 두번쨰 fail 있어서 오류남. append 뒤에 붙음(2배). replace 원 df 로 입력