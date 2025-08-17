import pandas as pd
import streamlit as st
from abc import ABC, abstractmethod
import return_delta

class Tabs_abstract:
    def __init__(self, df1, df2):
        self.df1 = df1
        self.df2 = df2

    @abstractmethod
    def return_text(self):
        pass
    
    @abstractmethod
    def calculate_delta(self):
        pass

class Tab1(Tabs_abstract):
    def __init__(self, df1, df2):
        super().__init__(df1, df2)

    def return_text(self):
        st.write("This is Tab 1")

    def calculate_delta(self):
        st.write("Calculating delta for Tab 1")
 
 #ref       
class Tab2(Tabs_abstract):
    def __init__(self, df1, df2):
        super().__init__(df1, df2)
        
    def _calculate_delta(self):
        answer = return_delta.Delta_Returned(self.df1, self.df2).return_delta_ref()
        return answer

    def return_text(self):
        answer= self._calculate_delta()
        st.write(f"Delta for Tab 2: {answer}")
        

    