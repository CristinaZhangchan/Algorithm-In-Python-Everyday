# %% [第一块：导入]
import pandas as pd
from io import StringIO

# %% [第二块：数据处理]
csv_data = """A,B,C,D
1.0,2.0,3.0,4.0
5.0,6.0,,8.0
10.0,11.0,12.0,"""

df = pd.read_csv(StringIO(csv_data))
df  # 这里的 df 会直接在右侧触发表格显示

# %%
type(df)

#%%
df.values
# %%
#统计每一列确实数据个数
df.isnull().sum(axis=1)

# %% 删除确实的行
df2=df.dropna(axis=0)
df2
# %%
df2.dropna(subset=['C'])


# %%
# Source - https://stackoverflow.com/a/59439287
# Posted by deramko, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-11, License - CC BY-SA 4.0

from sklearn.impute import SimpleImputer
import numpy as np

imr = SimpleImputer(missing_values=np.nan, strategy='mean')
imr = imr.fit(df.values)
imputed_data = imr.transform(df.values)
imputed_data
# %%

import pandas as pd
df = pd.DataFrame([['green', 'M', 10.1, 'class1'],
                   ['red', 'L', 13.5, 'class2'],
                   ['blue', 'XL', 15.3, 'class1']])
df.columns = ['color', 'size', 'price', 'classlabel']

df_original = df
df
# %%
size_mapping ={'XL':3,'L':2,'M':1}
df['size'] =df['size'].map(size_mapping)
df

# %%
import numpy as np
class_mapping = {label: idx for idx, label in enumerate(np.unique(df['classlabel']))}
class_mapping

# %%
df['classlabel'] = df['classlabel'].map(class_mapping)
X = df[['color', 'size', 'price', 'classlabel']].values
X
#说明了.value()可以表示而为参数
# %%
from sklearn.preprocessing import LabelEncoder
color_le = LabelEncoder()
X[:, 0] = color_le.fit_transform(X[:, 0])
X
# %%
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer([('encoder', OneHotEncoder(),[0])], remainder = 'passthrough')
ct.fit_transform(X)
# %%
import os
os.getcwd()
# %%
 