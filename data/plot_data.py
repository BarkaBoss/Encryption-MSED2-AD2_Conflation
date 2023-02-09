import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_csv('crypt_data_1.csv')
data_frame1 = pd.read_csv('crypt_data_1_3-4_1.csv')
data_frame2 = pd.read_csv('crypt_data_1_5-2_6_1.csv')
data_frame3 = pd.read_csv('crypt_data_2_3-2_4_1.csv')
data_frame4 = pd.read_csv('MSED2.csv')
#print(data_frame.head(10))

fig, ax = plt.subplots()
sns.set_theme(style="darkgrid")

sns.lineplot(data=data_frame4)
ax.set_ylim(1, 303000)
plt.ylabel("Execution Time (MS)")
plt.show()

sns.lineplot(data=data_frame)
ax.set_ylim(1, 1500)
plt.ylabel("Execution Time (MS)")
plt.show()

sns.lineplot(data=data_frame1)

ax.set_ylim(1, 40000)
plt.ylabel("Execution Time (MS)")
plt.show()

sns.lineplot(data=data_frame2)

ax.set_ylim(1, 303000)
plt.ylabel("Execution Time (MS)")
plt.show()

sns.lineplot(data=data_frame3)

ax.set_ylim(1, 60000)
plt.ylabel("Execution Time (MS)")
plt.show()