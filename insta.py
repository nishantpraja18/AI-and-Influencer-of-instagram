import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from collections import Counter as cn


p=pd.read_csv('instagram.csv')

# l=p['viral_video'].value_counts()
# plt.figure(figsize=(2,5))
# plt.bar(l.index,l.values)
# plt.title('HOW MANY VIDEOS ARE VIRAL ')
# plt.xlabel('number of videos are viral',labelpad=20,fontweight=20)
# plt.ylabel('number of user that have viral video',labelpad=20,fontweight=20)
# for i in range(8):
#     plt.annotate(f'({l.index[i]},{l.values[i]})',(l.index[i],l.values[i]),textcoords='offset points',xytext=(0,8),ha='center')
# plt.show()



# def convert_views(Views):
#     Views = Views.strip().lower()
#     if 'k' in Views:
#         return float(Views.replace('k', '')) * 1000
#     elif 'm' in Views:
#         return float(Views.replace('m', '')) * 1000000
#     else:
#         return float(Views)
    
# p['Views'] = p['Views'].apply(convert_views)
# print(p['Views'].min())
# def convert_Followers(Followers):
#     Followers = Followers.strip().lower()
#     if 'k' in Followers:
#         return float(Followers.replace('k', '')) * 1000
#     elif 'm' in Followers:
#         return float(Followers.replace('m', '')) * 1000000
#     else:
#         return float(Followers)
    
# p['Followers']=p['Followers'].apply(convert_Followers)    

# g=p.groupby('key_services')['Followers'].max()
# plt.bar(g.index,g.values)
# plt.title('maximum follower in each categogy',fontweight='bold')
# plt.xlabel('name of category',labelpad=20,fontweight=25)
# plt.ylabel('Maximum follower',labelpad=20,fontweight=25)
# plt.xticks(rotation=90)
# plt.show()

