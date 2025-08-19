import streamlit as st
import init
import pandas as pd
from PIL import Image
import os
import tabs

def main():
    st.set_page_config(
        page_title="מערכת ניהול תלמידים",
        page_icon="📌",
        layout="wide"
    )
    
    # הוספת לוגו לסיידבר
    try:
        # חיפוש לוגו בתקיית img
        img_path = "img"
        if os.path.exists(img_path):
            image_files = [f for f in os.listdir(img_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            if image_files and len(image_files) > 1:
                # בחירת הלוגו השני (אינדקס 1)
                logo_file = image_files[1]
                logo_path = os.path.join(img_path, logo_file)
                logo_image = Image.open(logo_path)
                st.logo(logo_image, size="large")
    except Exception as e:
        # אם יש שגיאה, פשוט נמשיך בלי לוגו
        pass

    # הוספת תמונה קטנה של hi_tech
    display_hitech_image()

    # כותרת ראשית
    st.title("🏫 מערכת ניהול תלמידים")
    st.markdown("---")

    # קליטת פרמטרים מה-URL
    
    # הצגת הפרמטרים
 
    
        # טעינת הנתונים
    df_all_1= init.return_df_1()
    df_all_2 = init.return_df_2()
    if df_all_1.empty:
        df_all_1=None
    if df_all_2.empty:
        df_all_2=None


   


    if not df_all_1.empty and 'school' in df_all_1.columns:
        unique_schools = df_all_1["school"].unique().tolist()
        selected_school = st.selectbox("בחר בית ספר:", unique_schools, key="school_selector")
        filtered_df1 = df_all_1[df_all_1['school'] == selected_school]
        st.session_state.filtered_df1 = filtered_df1
       
    if not df_all_2.empty:
            # unique_schools = df2["school"].unique().tolist()
            # selected_school = st.selectbox("בחר בית ספר:", unique_schools, key="school_selector")
            filtered_df2 = df_all_2[df_all_2['school'] == selected_school] #if selected_school else df2

            if  filtered_df2.empty:
                st.warning(" לא נמצאו נתוני שאלון שני")
                

    st.dataframe(filtered_df1, use_container_width=True)
    st.dataframe(filtered_df2, use_container_width=True)
    
    show_tabs(filtered_df1, filtered_df2)
    # יצירת tabs עם סטיילינג

def show_tabs(df1,df2):
        setup_tabs_styling()
        
        
        tab1, tab2 = st.tabs([
                "📈היגדים ", 
                "👥 רפלקציה", 
                 
            ])
    
        with tab1:
                # tab1_hegedim2.show(st.session_state.filtered_df2)
                tabs.Tab1(df1,df2).return_text()

        with tab2:
                tabs.Tab2(df1,df2).return_text()

        # show_charts_page()

def display_school_class_selector():
    """הצגת בורר בית ספר וכיתה"""
    st.subheader("🏫 בחירת בית ספר וכיתה")
    
    
        # טעינת הנתונים
    df1= init.return_df_1()
    df2 = init.return_df_2()
    if df1.empty:
        df1=None
    if df2.empty:
        df2=None
        
    st.session_state.df1 = df1
    st.session_state.df2 = df2
    
        
    if not df2.empty and 'school' in df2.columns:
            unique_schools = df2["school"].unique().tolist()
            selected_school = st.selectbox("בחר בית ספר:", unique_schools, key="school_selector")
            filtered_df = df2[df2['school'] == selected_school] #if selected_school else df2
            st.session_state.filtered_df2 = filtered_df 
            return True               
    else:
            st.warning("לא נמצאו נתונים לסינון")
            filtered_df = df2
            return False

    
    
def setup_tabs_styling():
    """הגדרת עיצוב הטאבים"""
    st.markdown("""
    <style>
    /* יצמדת טאבים למרכז */
    .stTabs [data-baseweb="tab-list"] {
        direction: rtl;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        direction: rtl;
    }
    
    /* הגדלת גודל הטאבים */
    .stTabs [data-baseweb="tab"] > div {
        font-size: 28px !important;
        font-weight: bold !important;
    }
    
    /* ריווח בין הטאבים */
    .stTabs [data-baseweb="tab"] {
        font-size: 20px !important;
        padding: 15px 25px !important;
        font-weight: bold !important;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

def display_hitech_image():
    """הצגת תמונה קטנה של hi_tech"""
    img_path = "img"
    hitech_files = ["hi_tech.png", "hi_tech.jpg", "hi_tech.jpeg", "hi_tech.gif", "hi_tech.bmp"]
    
    for hitech_file in hitech_files:
        hitech_path = os.path.join(img_path, hitech_file)
        if os.path.exists(hitech_path):
            try:
                hitech_image = Image.open(hitech_path)
                
                # הצגת התמונה במרכז העמוד בחצי גודל
                col1, col2, col3 = st.columns([2, 1, 2])
                with col2:
                    st.image(hitech_image, use_container_width=True, caption=" ")
                break
            except Exception as e:
                st.error(f"שגיאה בטעינת תמונת hi_tech: {str(e)}")

def show_home_page():
    """הצגת עמוד הבית עם הנתונים המסוננים"""
    
    # קבלת הפרמטרים מ-session_state
    school_name = st.session_state.get('school_name', None)
    class_name = st.session_state.get('class_name', None)
    
    # בדיקה אם יש פרמטרים
    if school_name and class_name:
        st.subheader(f"📊 נתונים עבור {school_name} - {class_name}")
        
        try:
            # ייבוא ה-DataFrame
            import init
            df = init.init()
            
            # סינון הנתונים לפי בית ספר וכיתה
            filtered_df = df[
                (df['school'] == school_name) & 
                (df['class'] == class_name)
            ]
            
            if not filtered_df.empty:
                st.success(f"נמצאו {len(filtered_df)} רשומות")
                
                # הצגת הטבלה
                st.dataframe(filtered_df, use_container_width=True)
                
                # סטטיסטיקות נוספות
                st.markdown("---")
                st.subheader("📈 סיכום סטטיסטי")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("סה״כ תלמידים", len(filtered_df))
                
                with col2:
                    # חיפוש עמודת ציון (יכולה להיות בשמות שונים)
                    score_columns = [col for col in filtered_df.columns if 'score' in col.lower() or 'ציון' in col]
                    if score_columns:
                        avg_score = filtered_df[score_columns[0]].mean()
                        st.metric("ציון ממוצע", f"{avg_score:.1f}")
                    else:
                        st.metric("עמודות", len(filtered_df.columns))
                
                with col3:
                    st.metric("בית ספר", school_name)
                
                # הצגת עמודות זמינות
                st.subheader("📋 עמודות זמינות בנתונים")
                st.write(", ".join(filtered_df.columns.tolist()))
                
                # אפשרות להורדה
                csv = filtered_df.to_csv(index=False)
                st.download_button(
                    label="💾 הורד נתונים כ-CSV",
                    data=csv,
                    file_name=f"{school_name}_{class_name}_data.csv",
                    mime="text/csv"
                )
                
            else:
                st.warning(f"לא נמצאו נתונים עבור {school_name} - {class_name}")
                st.info("ייתכן ושילוב בית הספר והכיתה לא קיים במערכת")
                
        except Exception as e:
            st.error(f"שגיאה בטעינת הנתונים: {str(e)}")
            st.info("וודא שקובץ init.py קיים ומכיל את הפונקציה init()")
    
    else:
        st.info("🔍 בחר בית ספר וכיתה כדי להציג נתונים")
        
        # הצגת סקירה כללית אם אין בחירה
        try:
            import init
            df = init.init()
            
            st.subheader("📊 סקירה כללית של המערכת")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                total_students = len(df)
                st.metric("סה״כ תלמידים במערכת", total_students)
            
            with col2:
                total_schools = df['school'].nunique()
                st.metric("מספר בתי ספר", total_schools)
            
            with col3:
                total_classes = df['class'].nunique()
                st.metric("מספר כיתות", total_classes)
            
            # הצגת בתי ספר וכיתות זמינים
            st.markdown("---")
            st.subheader("🏫 בתי ספר וכיתות במערכת")
            summary_df = df.groupby(['school', 'class']).size().reset_index(name='מספר תלמידים')
            st.dataframe(summary_df, use_container_width=True)
            
        except Exception as e:
            st.error(f"שגיאה בטעינת הנתונים: {str(e)}")

# def show_data_page():
#     pass

# def show_charts_page():
#     pass

if __name__ == "__main__":
    main()


# init.init()


