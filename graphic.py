# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 02:05:36 2020

@author: jacob
"""


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from bokeh.plotting import figure, output_file, show

df = pd.read_excel (r'C:\Users\jacob\Documents\01 Python\GroupVideo_StarterCode_v1 (1)\GroupVideo_StarterCode_v1\RBA_KYC_Accounts_ALL_Ids.xlsx')
df.head(10)
df.T



x = df['ledgerCode']
y = df['rbaValue']
radii = df['rbaValue']
colors = [
    "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*x, 30+2*y)
]

TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

p = figure(tools=TOOLS)

p.scatter(x, y, radius=radii,
          fill_color=colors, fill_alpha=0.6,
          line_color=None)


show(p)  # open a browser


#%%

x = df['age_in_year']
y = df['number_of_cash_dep_90_days']
z= df['GENDER']

# scatter plot with scatter() function
plt.scatter('X', 'Y', data=df,alpha=0.5)
plt.xlabel("age_in_year", size=10)
plt.ylabel("number_of_cash_dep_90_days", size=10)

#%%

plt.figure(figsize=(10,6))
sns.scatterplot(x=x, y=y,
                sizes=(20,500),
                alpha=0.5,
                hue="GENDER",
                 data=df)
plt.legend(bbox_to_anchor=(1.01, 1),borderaxespad=0)


plt.xlabel("number_of_cash_dep_90_days")
plt.ylabel("age_in_year")

plt.savefig("test.png",
                    format='png',dpi=150)
plt.tight_layout()

#%%

import numpy as np, pandas as pd; np.random.seed(0)
import seaborn as sns; 
sns.set(style="darkgrid", color_codes=True, palette= "Reds")

g = sns.jointplot(x="avg_of_cash_wd_90_days", y="age_in_year", data=df)
