import streamlit as st
st.title("BMI Calculation")
st.image("bmi.png")
st.markdown("---")
sex=st.radio("เพศ",("ชาย","หญิง"),horizontal=True)
kg=st.number_input("น้ำหนัก:",value=40.0,min_value=5.0,max_value=200.0)
cm=st.number_input("ความสูง:",value=140.0,min_value=10.0,max_value=200.0)
if st.button("calculate"):
    bmi=kg/(cm/100)**2
    if sex=="หญิง":
        st.subheader(f"your bmi is {bmi:.1f}")
        if bmi< 18:
           st.info(f"ตำกว่าเกณฑ์")
           st.warning("เสี่ยงขาดสารอาหาร")
           st.image("0.png")
        elif bmi< 22.9:
           st.success(f"สมส่วน")
           st.success("โรคเเทรกซ้อนน้อย")
           st.image("1.png")
        elif bmi< 24.9:
           st.warning(f"เกินมาตรฐาน")
           st.warning("นำหนักเกิน")
           st.image("2.png")
        elif bmi< 30:
           st.warning(f"อ้วน")
           st.error("นำหนักเกินมาก ระยะอ้วนเริ่มต้น")
           st.image("3.png")
        else:
           st.error(f"อ้วนมาก")
           st.error("โรคอ้วน")
           st.image("4.png")
    else:
        if bmi< 19:
           st.info(f"ตำกว่าเกณฑ์")
           st.warning("เสี่ยงขาดสารอาหาร")
           st.image("1.1.png")
        elif bmi< 23.9:
           st.success(f"สมส่วน")
           st.success("โรคเเทรกซ้อนน้อย")
           st.image("1.2.png")
        elif bmi< 25.9:
           st.warning(f"เกินมาตรฐาน")
           st.warning("นำหนักเกิน")
           st.image("1.3.png")
        elif bmi< 29.9:
           st.warning(f"อ้วน")
           st.error("นำหนักเกินมาก ระยะอ้วนเริ่มต้น")
           st.image("1.4.png")
        else:
           st.error(f"อ้วนมาก")
           st.error("โรคอ้วน")
           st.image("1.5.png")

