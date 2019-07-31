import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 

dataset= pd.read_csv('Ads_CTR_Optimisation.csv')

import math
#ucb_algorithm
N= dataset.shape[0]
d= dataset.shape[1]
number_of_selection= [0]*d
sum_of_rewards= [0]*d
avg_reward= [0]*d
ucb=[0]*d
ad_selected=[]
ad= 0
total_reward= 0
for n in range(0,N):
    if n<d:
        ad=n
    else:
        ad= ucb.index(max(ucb))
    ad_selected.append(ad)
    sum_of_rewards[ad] += dataset.values[n,ad]
    number_of_selection[ad] += 1
    avg_reward[ad]= sum_of_rewards[ad] /number_of_selection[ad]
    delta=math.sqrt(3/2*math.log(n+1)/number_of_selection[ad])
    ucb[ad]=avg_reward[ad]+delta
total_reward= sum(sum_of_rewards)    
#visualization
plt.hist(ad_selected, ec='black')
plt.title('Upper_Confidence_Bound')
plt.xlabel('ads')
plt.ylabel('Number off times the ad was selected')
plt.show()










    
