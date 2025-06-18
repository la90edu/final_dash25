import streamlit as st

def main():
    st.set_page_config(
        page_title="מערכת ניהול תלמידים",
        page_icon="📌",
        layout="wide"
    )
    
    # כותרת ראשית
    st.title("🏫 מערכת ניהול תלמידים")
    st.markdown("---")
    
    # יצירת tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🏠 בית", 
        "📊 נתונים", 
        "📈 גרפים", 
        "⚙️ הגדרות", 
        "📞 צור קשר"
    ])
    
    with tab1:
        show_home_page()
    
    with tab2:
        show_data_page()
    
    with tab3:
        show_charts_page()
    
    with tab4:
        show_settings_page()
    
    with tab5:
        show_contact_page()

def show_home_page():
    st.header("🏠 עמוד הבית")
    st.write("ברוכים הבאים למערכת ניהול התלמידים!")
    
    # תוכן ארוך לבדיקת הגלילה
    for i in range(1, 25):
        st.subheader(f"📄 סעיף {i}")
        
        if i % 4 == 0:
            st.success(f"""
            **סעיף {i} - הצלחה**
            
            זהו תוכן חשוב לדוגמה. הכותרת והתפריט למעלה נשארים גלויים?
            
            מידע נוסף:
            - פרט ראשון
            - פרט שני  
            - פרט שלישי
            """)
        elif i % 4 == 1:
            st.info(f"""
            **סעיף {i} - מידע**
            
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            """)
        elif i % 4 == 2:
            st.warning(f"""
            **סעיף {i} - אזהרה**
            
            זהו תוכן לדוגמה לבדיקת הגלילה.
            בדוק שהכותרת נשארת למעלה!
            """)
        else:
            st.error(f"""
            **סעיף {i} - שגיאה**
            
            תוכן לדוגמה נוסף.
            המטרה היא לבדוק שהכותרת נשארת קבועה.
            """)

def show_data_page():
    st.header("📊 ניתוח נתונים")
    st.write("כאן יוצגו הנתונים והסטטיסטיקות")
    
    import pandas as pd
    import numpy as np
    
    # יצירת נתונים לדוגמה
    for i in range(1, 15):
        st.subheader(f"טבלת נתונים {i}")
        
        data = {
            'שם': [f'תלמיד {j}' for j in range(1, 8)],
            'ציון': [np.random.randint(70, 100) for _ in range(7)],
            'כיתה': [f'{i}א' for _ in range(7)],
            'מקצוע': ['מתמטיקה', 'פיזיקה', 'כימיה', 'ביולוגיה', 'היסטוריה', 'ספרות', 'אנגלית']
        }
        
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        
        if i % 3 == 0:
            st.success(f"הצגת {i} טבלאות נתונים")

def show_charts_page():
    st.header("📈 גרפים ותרשימים")
    st.write("כאן יוצגו הגרפים השונים")
    
    import pandas as pd
    import numpy as np
    
    for i in range(1, 10):
        st.subheader(f"גרף {i}")
        
        # גרף קו
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=[f'סדרה {j}' for j in range(1, 4)]
        )
        st.line_chart(chart_data, use_container_width=True)
        
        # גרף עמודות
        if i % 2 == 0:
            bar_data = pd.DataFrame(
                np.random.rand(10, 2),
                columns=['A', 'B']
            )
            st.bar_chart(bar_data, use_container_width=True)

def show_settings_page():
    st.header("⚙️ הגדרות המערכת")
    st.write("כאן ניתן לשנות הגדרות שונות")
    
    # הגדרות שונות
    for i in range(1, 12):
        st.subheader(f"קטגוריית הגדרות {i}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.selectbox(f"בחירה {i}", ["אפשרות 1", "אפשרות 2", "אפשרות 3"], key=f"select_{i}")
            st.checkbox(f"הפעל תכונה {i}", key=f"check_{i}")
        
        with col2:
            st.slider(f"ערך {i}", 0, 100, 50, key=f"slider_{i}")
            st.number_input(f"מספר {i}", 0, 1000, 100, key=f"number_{i}")

def show_contact_page():
    st.header("📞 צור קשר")
    st.write("כאן ניתן ליצור קשר עם התמיכה")
    
    # טופס יצירת קשר
    with st.form("contact_form"):
        name = st.text_input("שם מלא")
        email = st.text_input("כתובת אימייל")
        subject = st.selectbox("נושא", ["תמיכה טכנית", "שאלה כללית", "דיווח על בעיה", "הצעה לשיפור"])
        message = st.text_area("הודעה", height=150)
        
        if st.form_submit_button("שלח הודעה"):
            st.success("ההודעה נשלחה בהצלחה!")
    
    # מידע נוסף
    st.markdown("---")
    st.subheader("מידע ליצירת קשר")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("📧 **אימייל:** support@school.com")
        st.write("📞 **טלפון:** 03-1234567")
    
    with col2:
        st.write("🏢 **כתובת:** רחוב הבית ספר 123, תל אביב")
        st.write("🕒 **שעות פעילות:** א'-ה' 8:00-17:00")

if __name__ == "__main__":
    main()