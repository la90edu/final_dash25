import init 
import pandas as pd
from urllib.parse import quote

df = init.init()

def make_urls(df):
    # יצירת טבלה של בתי ספר וכיתות
    schools_classes = df[['school', 'class']].drop_duplicates().sort_values(['school', 'class'])
    
    print("טבלת בתי ספר וכיתות:")
    print("-" * 50)
    print(schools_classes.to_string(index=False))
    
    # אפשרות לקבל את הטבלה כ-DataFrame
    return schools_classes

def get_schools_summary(df):
    """פונקציה נוספת לקבלת סיכום מפורט"""
    
    # קבלת רשימה ייחודית של בתי ספר וכיתות
    unique_combinations = df.groupby('school')['class'].unique().reset_index()
    
    print("\nסיכום מפורט:")
    print("=" * 60)
    
    for index, row in unique_combinations.iterrows():
        school = row['school']
        classes = ', '.join(sorted(row['class']))
        print(f"🏫 {school}")
        print(f"   כיתות: {classes}")
        print("-" * 40)
    
    return unique_combinations

def create_urls_table(df):
    """יצירת טבלה עם URLs לכל בית ספר וכיתה - פורט 8504"""
    
    schools_classes = df[['school', 'class']].drop_duplicates()
    
    # יצירת URLs עם קידוד נכון ופורט 8504
    urls = []
    for index, row in schools_classes.iterrows():
        school_encoded = quote(str(row['school']))
        class_encoded = quote(str(row['class']))
        url = f"http://localhost:8504?school_name={school_encoded}&class_name={class_encoded}"
        urls.append(url)
    
    # הוספת עמודת URLs לטבלה
    schools_classes['url'] = urls
    
    return schools_classes

def create_direct_links(df):
    """יצירת קישורים ישירים מוכנים לשימוש - פורט 8504"""
    
    schools_classes = df[['school', 'class']].drop_duplicates().sort_values(['school', 'class'])
    
    print("\n🔗 קישורים ישירים לפורט 8504:")
    print("=" * 80)
    
    for index, row in schools_classes.iterrows():
        school = row['school']
        class_name = row['class']
        school_encoded = quote(str(school))
        class_encoded = quote(str(class_name))
        
        url = f"http://localhost:8504?school_name={school_encoded}&class_name={class_encoded}"
        print(f"🏫 {school} - {class_name}")
        print(f"   {url}")
        print("-" * 50)

# הרצת הפונקציות
if __name__ == "__main__":
    print("🔗 מחולל URLs עבור פורט 8504")
    print("="*60)
    
    # הצגת הטבלה הבסיסית
    schools_table = make_urls(df)
    
    # הצגת סיכום מפורט
    summary = get_schools_summary(df)
    
    # יצירת טבלה עם URLs
    urls_table = create_urls_table(df)
    
    print("\nטבלה עם URLs לפורט 8504:")
    print("=" * 80)
    print(urls_table.to_string(index=False))
    
    # הצגת קישורים ישירים
    create_direct_links(df)
    
    # שמירה לקובץ CSV
    urls_table.to_csv('schools_urls_8504.csv', index=False, encoding='utf-8-sig')
    print(f"\n✅ הטבלה נשמרה בקובץ: schools_urls_8504.csv")
    
    print(f"\n📝 הוראות שימוש:")
    print("1. הרץ את stayup.py על פורט 8504:")
    print("   streamlit run stayup.py --server.port 8504")
    print("2. העתק אחד מהקישורים למעלה")
    print("3. הדבק בדפדפן")
    print("4. האפליקציה תציג את הפרמטרים שנשלחו")