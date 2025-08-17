import streamlit as st
import pandas as pd
import consts
import connect_to_google_sheet
import anigmas


def init():
    # st.set_page_config(
    #     layout="wide",
    #     page_title="דאשבורד ניתוח נתונים",
    #     page_icon="📊",
    #     initial_sidebar_state="expanded",
    #     menu_items={
    #         'About': "אפליקציה לניתוח נתונים פסיכולוגיים של תלמידים"
    #     }
    #)
    st.session_state.research_average = consts.return_research_average()

    st.markdown(
    """
    <style>
    h1, h2, h3, h4, h5, h6 {
        text-align: right;
        direction: rtl;
    }

    .css-1d391kg { 
        text-align: right; 
    }
    p {
        text-align: right;
        direction: rtl;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def return_df_1():
    data=connect_to_google_sheet.return_data_first()
    df=pd.DataFrame(data)

    # השתמש במחלקה הסטטית ישירות, ללא יצירת instance
    # global_avg=consts.return_global_average(df, anigmas.Anigmas1)
    # st.session_state.global_average1=global_avg
    # heg_avg=consts.init_heg_avg(df, anigmas.Anigmas1)
    # st.session_state.heg_avg1=heg_avg

    return df

def return_df_2():
    data=connect_to_google_sheet.return_data_last()
    df=pd.DataFrame(data)
    
    # השתמש במחלקה הסטטית ישירות, ללא יצירת instance
    # global_avg=consts.return_global_average(df, anigmas.Anigmas2)
    # st.session_state.global_average2=global_avg
    # heg_avg=consts.init_heg_avg(df, anigmas.Anigmas2)
    # st.session_state.heg_avg2=heg_avg
    return df

#for selectbox 
# st.markdown(
#         """
#         <style>
#         div[data-testid="stSelectbox"] {
#                 text-align: right;
#                 direction: rtl;
#                 width: 150px; /* Reduced width from 200px to 150px */
#                 margin-left: auto;
#                 margin-right: 0;
#         }
#         div[data-testid="stSelectbox"] > label > p {
#                 text-align: right;
#                 direction: rtl;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
# )