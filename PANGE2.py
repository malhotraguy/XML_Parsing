import numpy as np
import pandas as pd
from random import choice
def Paring(dict_ComponentItems,N):
    df = pd.DataFrame(columns=['q', 'rel','irr'])
    #Taking one group of components
    for i in dict_ComponentItems:
        #making the rest of dictionary keys list expect the present chosen group key
        temp_rest_dict_list=list(dict_ComponentItems)
        temp_rest_dict_list.remove(i)
        #for taking each element in the numpy array of the present chosen group
        for j in dict_ComponentItems[i]:

            #for iterating over each element except the present chosen element to make the
            for k in dict_ComponentItems[i]:
                if k!=j:

                    for l in range(N):
                        list_for_pd = [j, k]
                        random_dict_key=choice(temp_rest_dict_list)
                        list_for_pd.append(np.random.choice(dict_ComponentItems[random_dict_key], 1)[0])
                        list_for_pd=[int(x) for x in list_for_pd]
                        print(list_for_pd)
                        #print("np.random.choice(dict_ComponentItems[random_dict_key], 1)[0]=",np.random.choice(dict_ComponentItems[random_dict_key], 1)[0])
                        df = df.append(pd.Series(list_for_pd, index=['q', 'rel','irr']), ignore_index=True)

    df.to_csv('dataframe.csv', index=None, header=True)


