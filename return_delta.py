from abc import ABC, abstractmethod
import pandas as pd
from normalization import Normalization
import streamlit as st

class Delta_Returned:

    def __init__(self, df1, df2):
        self._df1 = df1
        self._df2 = df2
        self._cut1 = Cut1(self._df1)
        self._cut2 = Cut2(self._df2)

    def return_delta_ref(self):
        cut1 = self._cut1.cut_ref()
        cut2 = self._cut2.cut_ref()
        
        st.dataframe(cut1)
        st.dataframe(cut2)
        normalization_instance = Normalization(cut1, cut2).return_delta()
        return normalization_instance
    
    def return_delta_ici(self):
        cut1 = self._cut1.cut_ici()
        cut2 = self._cut2.cut_ici()

        normalization_instance = Normalization(cut1, cut2).return_delta()
        return normalization_instance

    def return_delta_risc(self):
        cut1 = self._cut1.cut_risc()
        cut2 = self._cut2.cut_risc()

        normalization_instance = Normalization(cut1, cut2).return_delta()
        return normalization_instance

    def return_delta_future_negetive_past(self):
        cut1 = self._cut1.cut_future_negetive_past()
        cut2 = self._cut2.cut_future_negetive_past()

        normalization_instance = Normalization(cut1, cut2).return_delta()
        return normalization_instance

    def return_delta_future_positive_past(self):
        cut1 = self._cut1.cut_future_positive_past()
        cut2 = self._cut2.cut_future_positive_past()

        normalization_instance = Normalization(cut1, cut2).return_delta()
        return normalization_instance

    def return_delta_future_fatalic_present(self):
        cut1 = self._cut1.cut_future_fatalic_present()
        cut2 = self._cut2.cut_future_fatalic_present()

        normalization_instance = Normalization(cut1, cut2).return_delta()
        return normalization_instance

    def return_delta_future_hedonistic_present(self):
        cut1 = self._cut1.cut_future_hedonistic_present()
        cut2 = self._cut2.cut_future_hedonistic_present()

        normalization_instance = Normalization(cut1, cut2).return_delta()
        return normalization_instance

    def return_delta_future_future(self):
        cut1 = self._cut1.cut_future_future()
        cut2 = self._cut2.cut_future_future()

        normalization_instance = Normalization(cut1, cut2).return_delta()
        return normalization_instance
    
    

class Cut_abstract (ABC):

    def __init__(self,df):
        self.df = df
            
    @abstractmethod
    def cut_ref(self):
        pass
        
    @abstractmethod
    def cut_ici(self):
        pass
        
    @abstractmethod
    def cut_risc(self):
        pass
        
    @abstractmethod
    def cut_future_negetive_past(self):
        pass

    @abstractmethod
    def cut_future_positive_past(self):
        pass
        
    @abstractmethod
    def cut_future_fatalic_present(self):
        pass

    @abstractmethod
    def cut_future_hedonistic_present(self):
        pass

    @abstractmethod
    def cut_future_future(self):
        pass
    
    def remove_empty_lines(self):
        # Replace empty strings with NaN
        self.df = self.df.replace(['', ' ', 'NA', 'N/A', 'null', None], pd.NA)
        # Drop rows with NaN values
        self.df = self.df.dropna()
        return self.df
        
class Cut1(Cut_abstract):
        
    def __init__(self, df):
        super().__init__(df)    
            
    def cut_ref(self):
        self.df = self.df[['ref_2', 'ref_3', 'ref_4', 'ref_5', 'ref_6', 'ref_7']]
        super().remove_empty_lines()
        return self.df

    def cut_ici(self):
        return self.df[['heg_1','heg_5','heg_10','heg_12','heg_24','heg_26']]

    def cut_risc(self):
        return self.df[['heg_4','"heg_14','heg_18','heg_19']]

    def cut_future_negetive_past(self):
        return self.df[['heg_2','heg_13','heg_23']]

    def cut_future_positive_past(self):
        return self.df[['heg_6','heg_16','heg_21']]

    def cut_future_fatalic_present(self):
        return self.df[['heg_3','heg_15','heg_22']]

    def cut_future_hedonistic_present(self):
        return self.df[['heg_11','heg_17','heg_25']]
    
    def cut_future_future(self):
        return self.df[['heg_7','heg_8','heg_9','heg_27']]
        
class Cut2(Cut_abstract):
        
    def __init__(self, df):
        super().__init__(df)    
            
    def cut_ref(self):
        self.df=self.df[['ref_1', 'ref_2', 'ref_3']]
        super().remove_empty_lines()
        return self.df

    def cut_ici(self):
        return self.df[['heg_3', 'heg_7', 'heg_10', 'heg_12', 'heg_20']]

    def cut_risc(self):
        return self.df[['heg_1', 'heg_5', 'heg_13', 'heg_16', 'heg_19']]

    def cut_future_negetive_past(self):
        return self.df[['heg_6','heg_15']]

    def cut_future_positive_past(self):
        return self.df[['heg_11','heg_17']]

    def cut_future_fatalic_present(self):
        return self.df[['heg_8', 'heg_18']]

    def cut_future_hedonistic_present(self):
        return self.df[['heg_2', 'heg_9']]
    
    def cut_future_future(self):
        return self.df[['heg_4', 'heg_14']]