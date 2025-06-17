import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.set_page_config(
        page_title="עמוד עם כרטיסיות",
        page_icon="📂",
        layout="wide"
    )
    
    st.title("📂 עמוד עם כרטיסיות")
    
    # יצירת כרטיסיות עם st.tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🏠 בית", "📊 נתונים", "📈 גרפים", "⚙️ הגדרות"])
    
    with tab1:
        show_home_tab()
    
    with tab2:
        show_data_tab()
    
    with tab3:
        show_charts_tab()
    
    with tab4:
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
        
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        
        if i % 3 == 0:
            st.success(f"סיימת לצפות ב-{i} טבלאות!")

def show_charts_tab():
    st.header("📈 גרפים ותרשימים")
    st.write("כאן יוצגו הגרפים השונים")
    
    # תוכן לדוגמה
    for i in range(1, 12):
        st.subheader(f"גרף {i}")
        st.write(f"זהו גרף מספר {i}")
        
        # גרף לדוגמה
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['A', 'B', 'C']
        )
        
        st.line_chart(chart_data, use_container_width=True)
        
        if i % 4 == 0:
            st.warning(f"צפית ב-{i} גרפים!")

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