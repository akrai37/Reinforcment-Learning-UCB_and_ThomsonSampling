# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset=pd.read_csv('Ads_CTR_Optimisation.csv')

# Implementing Thompson Sampling
import random
N= dataset.shape[0]
d= dataset.shape[1]
number_of_selections  = [0]*d
sum_of_rewards = [0]*d
total_rewards = 0
ad_selected= []
for n in range(0, N):
    random_beta= [random.betavariate( sum_of_rewards[i]+1, number_of_selections[i]+1)
                  for i in range(d)]
    
    ad= np.argmax(random_beta) #chooses the index of highest value in the axis(axis means row or column , 0 axis means column , 1 axis means row , not mentioning the axis means either single row or column) 
    ad_selected.append(ad)
    sum_of_rewards[ad]+= dataset.values[n,ad]
    number_of_selections[ad]+=1
    
total_rewards=sum(sum_of_rewards)   

#visualization
plt.hist(ad_selected, ec='black')
plt.title('Thomson_Sampling')
plt.xlabel('ads')
plt.ylabel('number_of_times_ad_was_selected')
plt.show()



