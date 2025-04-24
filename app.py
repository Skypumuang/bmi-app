import streamlit as st
st.title("BMI Calculation")
st.image("bmi.png")
st.markdown("---")
kg=st.number_input("your weight:",value=40.0,min_value=5.0,max_value=200.0)
cm=st.number_input("your height:",value=150.0,min_value=10.0,max_value=200.0)
if st.button("calculate"):
    bmi=kg/(cm/100)**2
    st.subheader(f"your bmi is {bmi:.1f}")
    if bmi< 18.5:
       st.info(f"{bmi}ตำกว่าเกณฑ์")
       st.warning("เสี่ยงขาดสารอาหาร")
       st.image("1.png")
    elif bmi< 23:
       st.success(f"{bmi}สมส่วน")
       st.success("โรคเเทรกซ้อนน้อย")
       st.image("2.png")
    elif bmi< 25:
       st.warning(f"{bmi}เกินมาตรฐาน")
       st.warning("นำหนักเกิน")
       st.image("3.png")
    elif bmi< 30:
       st.warning(f"{bmi}อ้วน")
       st.error("นำหนักเกินมาก ระยะอ้วนเริ่มต้น")
       st.image("4.png")
    else:
       st.error(f"{bmi}อ้วนมาก")
       st.error("โรคอ้วน")
       st.image("5.png")

