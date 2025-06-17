import streamlit as st

def main():
    st.set_page_config(
        page_title="פרמטרים פשוטים",
        page_icon="🏫",
        layout="wide"
    )
    
    st.title("🏫 מערכת לקליטת פרמטרים")
    
    # קליטת פרמטרים מה-URL
    query_params = st.query_params
    
    # שמירה ב-session_state
    if "class_name" in query_params:
        st.session_state.class_name = query_params["class_name"]
    
    if "school_name" in query_params:
        st.session_state.school_name = query_params["school_name"]
    
    # הצגת הפרמטרים
    st.subheader("📋 הפרמטרים שהתקבלו:")
    
    class_name = st.session_state.get('class_name', 'לא הועבר')
    school_name = st.session_state.get('school_name', 'לא הועבר')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("כיתה", class_name)
    
    with col2:
        st.metric("בית ספר", school_name)
    
    # אם יש פרמטרים - הצג תוכן
    if class_name != 'לא הועבר' and school_name != 'לא הועבר':
        st.success(f"מציג נתונים עבור כיתה {class_name} בבית ספר {school_name}")
        
        # כאן תוכל להוסיף את הלוגיקה שלך
        st.info("כאן יוצגו הנתונים של הכיתה...")
    
    else:
        st.warning("חסרים פרמטרים. אנא הוסף לכתובת:")
        st.code("?class_name=5א&school_name=אורט")

if __name__ == "__main__":
    main()