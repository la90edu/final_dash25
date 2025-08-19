import pandas as pd
import numpy as np

class Normalization:
    def __init__(self, df1, df2):
        # ניקוי ערכים ריקים ובחירת רק נומריים
        self.df1 = df1.dropna()
        self.df2 = df2.dropna()

    #שלב 3 
    def _normalize(self):       
        
        #חישוב הממוצע וסטיית תקן לT0 וT1 
        mean_df1 = self.df1.to_numpy().mean()
        std_df1 = self.df1.to_numpy().std()
        mean_df2 = self.df2.to_numpy().mean()
        std_df2 = self.df2.to_numpy().std()

        # עבור כל משתתף ב-T0: הערך שלו פחות הממוצע חלקי הסטיית תקן
        df1_normalized_vector = (self.df1 - mean_df1) / std_df1

        # עבור כל משתתף ב-T1: הערך שלו פחות הממוצע חלקי הסטיית תקן
        df2_normalized_vector = (self.df2 - mean_df2) / std_df2

        #ממוצע של כל הערכים שחישבנו בשלב הקודם - עבור T0 ו-T1
        df1_mean=df1_normalized_vector.to_numpy().mean()
        df2_mean=df2_normalized_vector.to_numpy().mean()

        #החזרת ההפרשת בין שתי הממוצעים משלב קודם
        return df1_mean, df2_mean


    def return_delta(self):
        """Return the delta between the two normalized means."""
        df1_mean, df2_mean = self._normalize()
        #החזרת ההפרשת בין שתי הממוצעים משלב קודם 
        return df2_mean - df1_mean


# #שלב 4 
# def mean_gorup(vector1,vector2):
#     """
#     מחשב את הממוצע של שני וקטורים
#     """
#     mean1=mean(vector1)
#     mean2=mean(vector2)
    
#     return mean1,mean2



