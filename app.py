import numpy as np
import pickle
import streamlit as st
model=pickle.load(open('employee_Burnout_prediction.sav','rb'))

def burnout_prediction(input_data):
    data=np.array(input_data,dtype = float)
    data_reshape=data.reshape(1,-1)
    prediction=model.predict(data_reshape)
    return prediction
def main():
    st.title("Employee Burnout Rate Prediction")

    WFH_Setup_Available=st.text_input("Enter whether work from home setup avaiableor not(no:0,yes=1))")
    Designation=st.text_input("enter the designation value(from 0 to 5)")
    Resource_allocation=st.text_input('enter the resource allocation value(from 1 to 10)')
    Mental_Fatigue_Score=st.text_input('enter the mental Fatigue score')
    Gender=st.text_input("Enter the Gender(Male:0,Female:1)")
    Company_label=st.text_input("enter the company(product:0,Service:1)")
    report=''
    if st.button("Get the BurnRate of Employee"):
        report=burnout_prediction([WFH_Setup_Available,Designation,Resource_allocation,Mental_Fatigue_Score,Gender,Company_label])
    st.success(report)
if __name__=='__main__':
    main()