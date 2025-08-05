import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter as cnt
import addcopyfighandler as cp


#------import data----------
df= pd.read_csv("Students.csv")
# print(df.shape)
# p=(df.isnull().sum()).sum()
# print(p)
# print(df.dtypes.to_clipboard())


# p=df.groupby("Stream")['AI_Tools_Used'].count()
# n=p.index
# v=p.values
# plt.bar(n,p,color="olive")
# plt.title("use AI tools in each stream by Student",fontweight='bold')
# plt.xlabel("Name of stream",fontweight="bold",labelpad=20)
# plt.ylabel("count of use of Ai in Stream",fontweight='bold',labelpad=20)
# plt.xticks(rotation=45)
# for i in range(10):
#      plt.annotate(f"({v[i]})",(n[i],v[i]),textcoords=("offset points"),xytext=(0,8),ha='center')
# plt.show()

# p=df.groupby('Internet_Access')['Device_Used'].value_counts()
# p=p.reset_index(name='Count')
# p=sns.barplot(x='Internet_Access',y='Count',hue='Device_Used',data=p)
# for container in p.containers:
#     p.bar_label(container)
# plt.title("Device Usage by Internet Access")
# plt.xlabel("types of speed ",labelpad=20)
# plt.ylabel("count of speed of each device",labelpad=20,)
# plt.show()

# p=df.groupby('Do_Professors_Allow_Use')['Preferred_AI_Tool'].value_counts()
# n=p.reset_index(name='Count of AI tools that is allow or not allow by professors')
# l=sns.barplot(x='Do_Professors_Allow_Use',y='Count of AI tools that is allow or not allow by professors',hue='Preferred_AI_Tool',data=n)
# l.set_xlabel('Do_Professors_Allow_Use',fontweight='bold')
# l.set_ylabel("Count of tools AI that is allow or not allow by professors",fontweight='bold')
# plt.title("Preferred AI Tools by Professor Approval")
# for i in l.containers:
#     l.bar_label(i)
# plt.show()



# p=df['AI_Tools_Used'].tolist()
# m=cnt(p)
# key=m.keys()

# pr=df['Willing_to_Pay_for_Access'].value_counts()
# m=pr.index
# l=pr.values
# plt.pie(l,labels=m,colors=['teal','blue'],autopct='%1.1f%%')
# plt.title("Willing to Pay for Access of AI pro version")
# plt.show()


# custom_palette = {
#     5: '#e74c3c',      # Bright red for grade 5
#     4: '#3498db',      # Blue
#     3: '#2ecc71',      # Green
#     2: '#f1c40f',      # Yellow
#     1: '#9b59b6',      # Purple
#     0: '#95a5a6',      # Gray
#     -1: '#34495e',     # Dark Blue
#     -2: '#d35400',     # Orange
#     -3: '#7f8c8d',     # Taupe
#     -4: '#1abc9c',     # Teal
#     -5: '#c0392b'      # Dark Red
# }
# sns.barplot(data=df,x='AI_Tools_Used',y='Daily_Usage_Hours',hue='Impact_on_Grades',palette=custom_palette,errorbar=None)
# plt.xticks(rotation=65)
# plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Impact on Grades')
# plt.tight_layout()
# plt.title('Daily use hours of AI Impact on grades')
# plt.show()

# p=df.groupby('AI_Tools_Used')['Trust_in_AI_Tools'].count()
# print(p)
# plt.pie(p.values,labels=p.index,autopct="%1.1f%%")
# plt.title("Trust level of students on AI")
# plt.show()

# p=df.groupby('AI_Tools_Used')['Awareness_Level'].count()
# plt.plot(p.index,p.values,marker='*',color='red',linestyle='--')
# plt.xticks(rotation=110)
# plt.title("Awareness level of student with AI")
# plt.xlabel('NAME of AI')
# plt.ylabel("number of students Awareness with AI")
# for i in range(9):
#     plt.annotate(f'({p.values[i]})',(p.index[i],p.values[i]),textcoords="offset points",xytext=(0,5),ha='center')

# plt.show()