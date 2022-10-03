import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_csv('crypt_data.csv')
#print(data_frame.head(10))

fig, ax = plt.subplots()
sns.set_theme(style="darkgrid")
sns.lineplot(data=data_frame)

ax.set_ylim(1, 500)
plt.show()