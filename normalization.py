import pandas as pd
import numpy as np

class Normalization:
    def __init__(self, df1, df2):
        self.df1 = df1.select_dtypes(include=[np.number])
        self.df2 = df2.select_dtypes(include=[np.number])

    #שלב 3 
    def _normalize(self):        
            # חישוב סטטיסטיקות - Calculate statistics
        mean_df1 = self.df1.mean()
        std_df1 = self.df1.std()
            
        mean_df2 = self.df2.mean()
        std_df2 = self.df2.std()
            
            # יישום טרנספורמציה - Apply transformation
            # for each participant in T0:
        # if std_df1 > 0:
        df1_normalized_vector = (self.df1 - mean_df1) / std_df1

            # for each participant in T1:
        # if std_df2 > 0:
        df2_normalized_vector = (self.df2 - mean_df2) / std_df2

        df1_mean=df1_normalized_vector.mean()
        df2_mean=df2_normalized_vector.mean()

        return df1_mean, df2_mean


    def return_delta(self):
        """Return the delta between the two normalized means."""
        df1_mean, df2_mean = self._normalize()
        return df2_mean - df1_mean


# #שלב 4 
# def mean_gorup(vector1,vector2):
#     """
#     מחשב את הממוצע של שני וקטורים
#     """
#     mean1=mean(vector1)
#     mean2=mean(vector2)
    
#     return mean1,mean2



