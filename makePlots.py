import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("./count.csv")

df = df.sort_values('code',ascending=False)

df.plot(kind='bar',x='language',y='code',label='Lines of Code', color="blue")
plt.xlabel('Language')
# so labels are not cut off
plt.gcf().subplots_adjust(bottom=0.30)


#plt.show()
plt.savefig('plot.png')
