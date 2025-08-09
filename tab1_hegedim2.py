import streamlit as st
import class_school_info
from anigmas import Anigmas2
import plotly.graph_objects as go

def show(filter_df2):
    """
    This function displays the second tab of the dashboard, which includes
    a comparison of the user's results with others in the system.
    """
    
    # Check if the filtered DataFrame is available in session state
    if 'filtered_df2' not in st.session_state:
        st.error("🔍 אין נתונים זמינים להצגה. אנא בחר בית ספר וכיתה.")
        return
    
    # Set the title for the tab
    st.title("📊 השוואה עם אחרים במערכת")
    
    # Display the header for the comparison section
    st.header("👥 אני ואחרים")
    
    # Display a message about comparing with others
    st.write("השוואה עם אחרים במערכת")
    
    # Get the filtered DataFrame from session state
    
    # Create an instance of SchoolInfo with the filtered DataFrame and Anigmas2
    

    

    class_info=class_school_info.SchoolInfo(filter_df2, Anigmas2,st.session_state.global_average2)
    fig_ici=class_info.get_fig_ici("ici")
    fig_risc=class_info.get_fig_risc("risc")
    fig_spider=class_info.get_fig_spider(mobile=False)
    st.plotly_chart(fig_ici, use_container_width=True)
    st.plotly_chart(fig_risc, use_container_width=True)
    st.plotly_chart(fig_spider, use_container_width=True)
