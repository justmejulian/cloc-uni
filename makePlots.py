import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("./count.csv")

df = df.sort_values('code',ascending=False)

df.plot(kind='bar',x='language',y='code', color="blue")

# so labels are not cut off
plt.gcf().subplots_adjust(bottom=0.20)

plt.savefig('plot.png')
