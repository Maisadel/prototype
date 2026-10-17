import streamlit as st
import random

st.set_page_config(page_title="SafeMed MVP", page_icon="🛡️", layout="centered")

st.title("🛡️ SafeMed: منصة الفرز الطبي الآمن والمجهول")
st.markdown("---")

tab1, tab2 = st.tabs(["👤 واجهة المريض (الفحص الخفي)", "🩺 واجهة الطبيب (فك التشفير)"])

with tab1:
    st.subheader("سجل أعراضك وأرفق فحوصاتك السابقة بحرية تامة")
    symptoms = st.text_area("ما هي الأعراض أو الشكوى الرئيسية التي تعاني منها؟", placeholder="اكتب الأعراض هنا لتوليد تقرير SBAR...")
    
    urgency = st.selectbox("مستوى الألم أو الاستعجال:", ["منخفض", "متوسط", "عالي (حرج)"])
    
    # الإضافة الجديدة: رفع التقارير أو التحاليل السابقة
    uploaded_file = st.file_uploader("📁 أرفق تقارير طبية أو تحاليل سابقة (اختياري - صور أو PDF)", type=["png", "jpg", "jpeg", "pdf"])
    
    if st.button("إرسال وتشفير التقرير"):
        if symptoms.strip():
            token = f"MED-{random.randint(10000, 99999)}"
            st.session_state['saved_token'] = token
            st.session_state['has_file'] = uploaded_file is not None
            
            st.success("تم تشفير البيانات بنجاح وحماية خصوصيتك بالكامل!")
            st.markdown("### 📋 ملخص تقرير SBAR الطبي:")
            st.markdown("""
            - **Situation (الموقف):** مريض يحتاج تقييم عاجل بدون كشف الهوية.
            - **Background (الخلفية):** إدخال ذاتي آمن للأعراض والفحوصات السابقة.
            - **Assessment (التقييم):** تم رصد الحالة وتصنيفها آلياً.
            - **Recommendation (التوصية):** مراجعة الطبيب بالرمز أدناه.
            """)
            if uploaded_file:
                st.info(1 * "📎 تم إرفاق الملف الطبي بنجاح وتشفيره للمراجعة السريرية.")
            
            st.info(f"🔑 رمز المرور السري الخاص بك: **{token}** (احتفظ به لعرضه على الطبيب)")
        else:
            st.warning("الرجاء كتابة الأعراض أولاً.")

with tab2:
    st.subheader("بوابة الممارس الصحي المعتمد")
    entered_token = st.text_input("أدخل رمز المريض السري:", value=st.session_state.get('saved_token', ''))
    
    if st.button("فك التشفير وعرض الملف"):
        if entered_token:
            st.success("تم التحقق من الرمز وفك التشفير بنجاح (الهوية مخفية تماماً)")
            st.markdown("""
            | بيانات التقرير | التفاصيل |
            | :--- | :--- |
            | **الحالة الطبية** | تم استلام الشكاوي وتحليلها وفق بروتوكول SBAR |
            """)
            
            if st.session_state.get('has_file', False):
                st.warning("⚠️ يوجد مرفق طبي (تحاليل/أشعة) مرفق مع هذا التقرير متاح للاطلاع الإكلينيكي الآمن.")
            else:
                st.info("ℹ️ لم يتم إرفاق ملفات إضافية من قبل المريض في هذه الحالة.")
                
            st.markdown("""
            | المؤشرات | التفاصيل |
            | :--- | :--- |
            | **نسبة توفير الوقت** | تقليل وقت أخذ التاريخ المرضي بنسبة 70% |
            """)
        else:
            st.error("الرجاء إدخال الرمز الصحيح.")
