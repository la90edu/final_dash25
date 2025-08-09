
import pandas as pd
import streamlit as st
import anigmas


colors = {
    "current_color": "#FF5733",
    "global_color": "#33FF57",
    "research_color": "#5733FF"
}

def round_number(number):
        return round(number,1)
  
# research_average={
#     "ici":3.71,
#     "risc":3.22,
#     "future_negetive_past":2.47,
#     "future_positive_past":3.2,
#     "future_fatalic_present":2.7,
#     "future_hedonistic_present":2.84,
#     "future_future":3.68
    
# }

research_average={
    "ici":3.7,
    "risc":3.2,
    "future_negetive_past":2.4,
    "future_positive_past":3.2,
    "future_fatalic_present":2.7,
    "future_hedonistic_present":2.84,
    "future_future":3.68
    
}

colors = {
    "current_color": "#FF5733",
    "global_color": "#33FF57",
    "research_color": "#5733FF"
}

def round_number(number):
        return round(number,1)
  
# research_average={
#     "ici":3.71,
#     "risc":3.22,
#     "future_negetive_past":2.47,
#     "future_positive_past":3.2,
#     "future_fatalic_present":2.7,
#     "future_hedonistic_present":2.84,
#     "future_future":3.68
    
# }

research_average={
    "ici":3.7,
    "risc":3.2,
    "future_negetive_past":2.4,
    "future_positive_past":3.2,
    "future_fatalic_present":2.7,
    "future_hedonistic_present":2.84,
    "future_future":3.68
    
}

def return_research_average():
    return research_average 

def return_global_average(global_df,anigmas):
    # יצירת מילון global_average ישירות מהפונקציות של anigmas במקום שימוש ב-SchoolInfo
    global_average = {
        "ici": round_number(float(anigmas.ici_result(global_df))),
        "risc": round_number(float(anigmas.risc_result(global_df))),
        "future_negetive_past": round_number(float(anigmas.future_negetive_past_result(global_df))),
        "future_positive_past": round_number(float(anigmas.future_positive_past_result(global_df))),
        "future_fatalic_present": round_number(float(anigmas.future_fatalic_present_result(global_df))),
        "future_hedonistic_present": round_number(float(anigmas.future_hedonistic_present_result(global_df))),
        "future_future": round_number(float(anigmas.future_future_result(global_df)))
    }
    # אתחול המשתנים ב-session_state
    st.session_state.research_average = research_average
    
    return global_average
    
    

# def return_global_average(df,anigmas): 
#     global_average={
#         "ici":float(anigmas.ici_result(df)),
#         "risc":float(anigmas.risc_result(df))
#     }
    
#     return global_average

def init_heg_avg(df,anigmas):
    heg_avg=anigmas.get_global_heg_avg_as_dict(df)
    st.session_state.heg_avg=heg_avg
    return heg_avg