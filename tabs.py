import pandas as pd
import streamlit as st
from abc import ABC, abstractmethod
import return_delta
from landchain_folder.write_answer import Write_LLM_Answer

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
    def __init__(self, df1, df2, school_name):
        super().__init__(df1, df2)
        self.ref_value=return_delta.Delta_Returned(self.df1, self.df2).return_delta_ref()
        self.ici_value= return_delta.Delta_Returned(self.df1, self.df2).return_delta_ici()
        self.risc_value = return_delta.Delta_Returned(self.df1, self.df2).return_delta_risc()
        self.future_negetive_past_value = return_delta.Delta_Returned(self.df1, self.df2).return_delta_future_negetive_past()
        self.future_positive_past_value = return_delta.Delta_Returned(self.df1, self.df2).return_delta_future_positive_past()
        self.future_fatalic_present_value = return_delta.Delta_Returned(self.df1, self.df2).return_delta_future_fatalic_present()
        self.future_hedonistic_present_value = return_delta.Delta_Returned(self.df1, self.df2).return_delta_future_hedonistic_present()
        self.future_future_value = return_delta.Delta_Returned(self.df1, self.df2).return_delta_future_future()
        self.school_name = school_name 
        
    def return_text(self):
        answer = Write_LLM_Answer(
            self.ref_value,
            self.ici_value,
            self.risc_value,
            self.future_negetive_past_value,
            self.future_positive_past_value,
            self.future_fatalic_present_value,
            self.future_hedonistic_present_value,
            self.future_future_value,
        )
        # Stream the report live in the UI
        # Add school name if available from df1
        school_name = self.school_name
        st.session_state["selected_school_name_for_llm"] = school_name
        answer.stream_all()


 
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
        

    