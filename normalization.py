import pandas as pd
import numpy as np
import streamlit as st

class Normalization:
    def __init__(self, df1, df2):
        # ניקוי ערכים ריקים ובחירת רק נומריים
        self.df1 = df1.dropna()
        self.df2 = df2.dropna()

    #שלב 3 
    def return_mean(self,df):
        answer=df.mean()
        answer= np.mean(answer)
        return answer
    
    def _normalize(self):       
        
        #חישוב הממוצע וסטיית תקן לT0 וT1 
        df1_mean=self.return_mean(self.df1)
        f_df1_mean=float(df1_mean)
        std_df1 = self.df1.to_numpy().std()
        f_std_df1=float(std_df1) 
        df2_mean=self.return_mean(self.df2)
        f_df2_mean=float(df2_mean)
        std_df2 = self.df2.to_numpy().std()
        f_std_df2=float(std_df2)

        # עבור כל משתתף ב-T0: הערך שלו פחות הממוצע חלקי הסטיית תקן
        df1_normalized_df = (self.df1 - f_df1_mean) / f_std_df1

        # עבור כל משתתף ב-T1: הערך שלו פחות הממוצע חלקי הסטיית תקן
        df2_normalized_df = (self.df2 - f_df2_mean) / f_std_df2
         # עיגול ל-3 נקודות עשרוניות
        df1_normalized_df = df1_normalized_df.round(3)
        df2_normalized_df = df2_normalized_df.round(3)
        
        # st.write("normalized vectors:")
        # st.dataframe(df1_normalized_df)
        # st.dataframe(df2_normalized_df)

        col_mean_df1=df1_normalized_df.mean(axis=0).round(3)
        
        col_mean_df2=df2_normalized_df.mean(axis=0).round(3)
        
        st.write("cols mean ")
        st.dataframe(col_mean_df1)
        st.dataframe(col_mean_df2)
        #ממוצע של כל הערכים שחישבנו בשלב הקודם - עבור T0 ו-T1
       
        f_df1_mean_final=float(col_mean_df1.mean(axis=0)).round(3)
        f_df2_mean_final=float(col_mean_df2.mean(axis=0)).round(3)

        st.write("final means:")
        st.write(f_df1_mean_final)
        st.write(f_df2_mean_final)

        #החזרת ההפרשת בין שתי הממוצעים משלב קודם
        return f_df1_mean_final, f_df2_mean_final

    def return_simple_mean(self,df):
        col_mean=df.mean(axis=0)
        mean=col_mean.mean(axis=0)
        return round(float(mean),3)

    def return_delta(self):
        #return the delta between the two means in precentage - how much there was a diffrent between the first ti the second
        df1_mean=self.return_simple_mean(self.df1)
        df2_mean=self.return_simple_mean(self.df2)
        #החזרת ההפרשת בין שתי הממוצעים משלב קודם
        answer= ((df1_mean - df2_mean)/df1_mean)*(-100)
        return answer


# #שלב 4 
# def mean_gorup(vector1,vector2):
#     """
#     מחשב את הממוצע של שני וקטורים
#     """
#     mean1=mean(vector1)
#     mean2=mean(vector2)
    
#     return mean1,mean2



