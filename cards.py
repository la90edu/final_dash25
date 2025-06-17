import streamlit as st

def main():
    st.set_page_config(
        page_title="עמוד עם כרטיסיות קבועות",
        page_icon="📂",
        layout="wide"
    )
    
    st.title("📂 עמוד עם כרטיסיות קבועות")
    
    # יצירת מיכל קבוע עבור הכרטיסיות
    tabs_container = st.container()
    
    with tabs_container:
        # יצירת כרטיסיות עם מפתחות ייחודיים
        if 'active_tab' not in st.session_state:
            st.session_state.active_tab = 0
        
        # יצירת כפתורי כרטיסיות
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("🏠 בית", key="tab1", use_container_width=True):
                st.session_state.active_tab = 0
        
        with col2:
            if st.button("📊 נתונים", key="tab2", use_container_width=True):
                st.session_state.active_tab = 1
        
        with col3:
            if st.button("📈 גרפים", key="tab3", use_container_width=True):
                st.session_state.active_tab = 2
        
        with col4:
            if st.button("⚙️ הגדרות", key="tab4", use_container_width=True):
                st.session_state.active_tab = 3
    
    st.markdown("---")
    
    # הצגת תוכן בהתאם לכרטיסיה הפעילה
    content_container = st.container()
    
    with content_container:
        if st.session_state.active_tab == 0:
            show_home_tab()
        elif st.session_state.active_tab == 1:
            show_data_tab()
        elif st.session_state.active_tab == 2:
            show_charts_tab()
        elif st.session_state.active_tab == 3:
            show_settings_tab()

def show_home_tab():
    st.header("🏠 עמוד הבית")
    st.write("ברוכים הבאים לעמוד הבית!")
    
    # הוספת תוכן ארוך לבדיקת הגלילה
    for i in range(1, 21):
        st.subheader(f"סעיף {i}")
        st.write(f"""
        זהו תוכן של סעיף {i}. כאן יכול להיות מידע חשוב על המערכת.
        המטרה היא לבדוק שהכרטיסיות נשארות למעלה גם כשגוללים למטה.
        
        תוכן נוסף: Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """)
        
        if i % 5 == 0:
            st.info(f"הגעת לסעיף {i}! הכרטיסיות עדיין נמצאות למעלה?")

def show_data_tab():
    st.header("📊 ניתוח נתונים")
    st.write("כאן יוצגו הנתונים והסטטיסטיקות")
    
    # תוכן לדוגמה
    for i in range(1, 16):
        st.subheader(f"טבלת נתונים {i}")
        st.write(f"זוהי טבלת נתונים מספר {i}")
        
        # טבלה לדוגמה
        data = {
            'שם': [f'תלמיד {j}' for j in range(1, 6)],
            'ציון': [85 + (i * j) % 20 for j in range(1, 6)],
            'כיתה': [f'{i}א' for _ in range(5)]
        }
        
        st.table(data)
        
        if i % 3 == 0:
            st.success(f"סיימת לצפות ב-{i} טבלאות! הכרטיסיות עדיין למעלה?")

def show_charts_tab():
    st.header("📈 גרפים ותרשימים")
    st.write("כאן יוצגו הגרפים השונים")
    
    import pandas as pd
    import numpy as np
    
    # תוכן לדוגמה
    for i in range(1, 12):
        st.subheader(f"גרף {i}")
        st.write(f"זהו גרף מספר {i}")
        
        # גרף לדוגמה
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['A', 'B', 'C']
        )
        
        st.line_chart(chart_data)
        
        if i % 4 == 0:
            st.warning(f"צפית ב-{i} גרפים! בדוק שהכרטיסיות עדיין נמצאות למעלה")

def show_settings_tab():
    st.header("⚙️ הגדרות המערכת")
    st.write("כאן ניתן לשנות הגדרות שונות")
    
    # הגדרות לדוגמה
    st.subheader("הגדרות כלליות")
    theme = st.selectbox("בחר ערכת צבעים", ["בהיר", "כהה", "אוטומטי"])
    language = st.selectbox("בחר שפה", ["עברית", "אנגלית", "ערבית"])
    
    st.subheader("הגדרות תצוגה")
    show_sidebar = st.checkbox("הצג סרגל צד", value=True)
    show_footer = st.checkbox("הצג כותרת תחתונה", value=False)
    
    st.subheader("הגדרות נתונים")
    auto_refresh = st.slider("רענון אוטומטי (דקות)", 1, 60, 15)
    max_rows = st.number_input("מספר שורות מקסימלי", 10, 1000, 100)
    
    # תוכן נוסף ארוך
    st.subheader("מידע נוסף")
    for i in range(1, 11):
        st.write(f"הגדרה {i}: זוהי הגדרה חשובה במערכת")
    
    # כפתורי פעולה
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("💾 שמור הגדרות", key="save_settings"):
            st.success("ההגדרות נשמרו בהצלחה!")
    
    with col2:
        if st.button("🔄 איפוס", key="reset_settings"):
            st.info("ההגדרות אופסו לברירת המחדל")
    
    with col3:
        if st.button("📤 ייצא הגדרות", key="export_settings"):
            st.info("ההגדרות יוצאו לקובץ")

if __name__ == "__main__":
    main()