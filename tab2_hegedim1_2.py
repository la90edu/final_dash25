import plotly.graph_objects as go
import streamlit as st
import class_school_info
import anigmas

def show(df1,global_dict1,df2,global_dict2):
    """
    This function creates a line graph using the provided dictionaries and name.
    
    Parameters:
    - df1: The first DataFrame containing data for the first line.
    - global_dict1: The global dictionary for the first line.
    - df2: The second DataFrame containing data for the second line.
    - global_dict2: The global dictionary for the second line.
    
    Returns:
    - fig: A Plotly figure object representing the line graph.
    """
    
    school_info1=class_school_info.SchoolInfo(df1,anigmas.Anigmas1,global_dict1)
    school_info2=class_school_info.SchoolInfo(df2,anigmas.Anigmas2,global_dict2)

    school_info1_dict=school_info1.return_anigmas_result_as_dict()
    school_info2_dict=school_info2.return_anigmas_result_as_dict()
    
    fig = go.Figure()
    
    # Add first line (local data)
    fig.add_trace(go.Scatter(
        x=list(school_info1_dict.keys()),
        y=list(school_info1_dict.values()),
        mode='lines+markers',
        name="סבב 1 ",
        line=dict(color='gray', width=3),
        marker=dict(size=8)
    ))
    
    # Add second line (local data)
    fig.add_trace(go.Scatter(
        x=list(school_info2_dict.keys()),
        y=list(school_info2_dict.values()),
        mode='lines+markers',
        name="סבב 2 ",
        line=dict(color='green', width=3),
        marker=dict(size=8)
    ))
    
    # Add global average line 1
    fig.add_trace(go.Scatter(
        x=list(global_dict1.keys()),
        y=list(global_dict1.values()),
        mode='lines+markers',
        name="סבב 1 - ממוצע ארצי",
        line=dict(color='darkgray', width=1 ),
        marker=dict(size=2)
    ))
    
    # Add global average line 2
    fig.add_trace(go.Scatter(
        x=list(global_dict2.keys()),
        y=list(global_dict2.values()),
        mode='lines+markers',
        name="סבב 2 - ממוצע ארצי",
        line=dict(color='darkgreen', width=1),
        marker=dict(size=2)
    ))
    
    # Set layout with Hebrew support
    fig.update_layout(
        title="השוואת תוצאות בין סבבים - הכיתה מול הממוצע הארצי",
        xaxis_title='אניגמות',
        yaxis_title='ערכים',
        font=dict(size=14),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        hovermode='x unified',
        width=800,
        height=500
    )
    
    # Update x-axis for better readability
    fig.update_xaxes(
        tickangle=45,
        showgrid=True,
        gridwidth=1,
        gridcolor='lightgray'
    )
    
    # Update y-axis
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='lightgray'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # הוספת טבלה להשוואה
    st.subheader("📊 טבלת השוואה מפורטת")
    
    import pandas as pd
    
    comparison_df = pd.DataFrame({
        'אניגמה': list(school_info1_dict.keys()),
        'סבב 1 - כיתה': list(school_info1_dict.values()),
        'סבב 1 - ארצי': list(global_dict1.values()),
        'סבב 2 - כיתה': list(school_info2_dict.values()),
        'סבב 2 - ארצי': list(global_dict2.values())
    })
    
    # חישוב הפרשים
    comparison_df['הפרש סבב 1 (כיתה-ארצי)'] = comparison_df['סבב 1 - כיתה'] - comparison_df['סבב 1 - ארצי']
    comparison_df['הפרש סבב 2 (כיתה-ארצי)'] = comparison_df['סבב 2 - כיתה'] - comparison_df['סבב 2 - ארצי']
    comparison_df['שיפור בין סבבים'] = comparison_df['סבב 2 - כיתה'] - comparison_df['סבב 1 - כיתה']
    
    st.dataframe(comparison_df, use_container_width=True)
    
    # תובנות
    st.subheader("💡 תובנות מהגרף")
    
    # חיפוש השיפור הגדול ביותר
    max_improvement_idx = comparison_df['שיפור בין סבבים'].idxmax()
    max_improvement_anigma = comparison_df.loc[max_improvement_idx, 'אניגמה']
    max_improvement_value = comparison_df.loc[max_improvement_idx, 'שיפור בין סבבים']
    
    if max_improvement_value > 0:
        st.success(f"✅ השיפור הגדול ביותר: **{max_improvement_anigma}** עם שיפור של {max_improvement_value:.2f} נקודות")
    
    # חיפוש הירידה הגדולה ביותר
    min_improvement_idx = comparison_df['שיפור בין סבבים'].idxmin()
    min_improvement_anigma = comparison_df.loc[min_improvement_idx, 'אניגמה']
    min_improvement_value = comparison_df.loc[min_improvement_idx, 'שיפור בין סבבים']
    
    if min_improvement_value < 0:
        st.warning(f"⚠️ הירידה הגדולה ביותר: **{min_improvement_anigma}** עם ירידה של {abs(min_improvement_value):.2f} נקודות")
