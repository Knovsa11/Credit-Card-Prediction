import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json


with open('model_scaler.pkl', 'rb') as file_1:
  model_scaler = pickle.load(file_1)

with open('model_svm_random.pkl', 'rb') as file_2:
  model_svm = pickle.load(file_2)

def run():
  # buat form inputan
    with st.form('form-credit-card'):
       limit_balance = st.number_input('limit_balance', min_value=100, max_value=1000000, help='(range 100 until 1000000)')
       gender = st.number_input('Gender', min_value=1, max_value=2, help='(1 = Male, 2 = Female)')
       education = st.number_input('Education', min_value=1, max_value=4, help='(1=graduate school, 2=university, 3=high school, 4=others)')
       marriage = st.number_input('Marital Status', min_value=1, max_value=3, help='(1=graduate school, 2=university, 3=high school, 4=others)')
       education = st.number_input('Education', min_value=1, max_value=4, help='(1=married, 2=single, 3=others)')
       age = st.number_input('Age', min_value=1, max_value=100, help='(range number 1 - 100)')
       st.markdown('---')



       pay_0 = st.number_input('Pay_0', min_value=-2, max_value=8, help='(-2=no consumption, -1=pay duly, 0=the use of revolving credit, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months)')
       pay_2 = st.number_input('Pay_2', min_value=-2, max_value=8, help='(-2=no consumption, -1=pay duly, 0=the use of revolving credit, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months)')
       pay_3 = st.number_input('Pay_3', min_value=-2, max_value=8, help='(-2=no consumption, -1=pay duly, 0=the use of revolving credit, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months)')
       pay_4 = st.number_input('Pay_4', min_value=-2, max_value=8, help='(-2=no consumption, -1=pay duly, 0=the use of revolving credit, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months)')
       pay_5 = st.number_input('Pay_5', min_value=-2, max_value=8, help='(-2=no consumption, -1=pay duly, 0=the use of revolving credit, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months)')
       pay_6 = st.number_input('Pay_6', min_value=-2, max_value=8, help='(-2=no consumption, -1=pay duly, 0=the use of revolving credit, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months)')
       st.markdown('---')


       bill_amt_1 = st.number_input('bill_amt_1', min_value=-11545, max_value=613860, help='(range -11545 until 613860)')
       bill_amt_2 = st.number_input('bill_amt_2', min_value=-67526, max_value=512650, help='(range -67526 until 512650)')
       bill_amt_3 = st.number_input('bill_amt_3', min_value=-25433, max_value=578971, help='(range -25433 until 578971)')
       bill_amt_4 = st.number_input('bill_amt_4', min_value=-46627, max_value=488808, help='(range -46627 until 488808)')
       bill_amt_5 = st.number_input('bill_amt_5', min_value=-46627, max_value=441981, help='(range -46627 until 441981)')
       bill_amt_6 = st.number_input('bill_amt_6', min_value=-73895, max_value=436172, help='(range -73895 until 436172)')
       st.markdown('---')


       pay_amt_1 = st.number_input('pay_amt_1', min_value=0, max_value=493358, help='(range 0 until 493358)')
       pay_amt_2 = st.number_input('pay_amt_2', min_value=0, max_value=1227082, help='(range 0 until 1227082)')
       pay_amt_3 = st.number_input('pay_amt_3', min_value=0, max_value=199209, help='(range 0 until 199209)')
       pay_amt_4 = st.number_input('pay_amt_4', min_value=0, max_value=202076, help='(range 0 until 202076)')
       pay_amt_5 = st.number_input('pay_amt_5', min_value=0, max_value=388071, help='(range 0 until 388071)')
       pay_amt_6 = st.number_input('pay_amt_6', min_value=0, max_value=403500, help='(range 0 until 403500)')

       # submit button
       submitted = st.form_submit_button('Predict')

    data_inf = {
        'limit_balance': limit_balance,
        'sex':gender,
        'education_level':education,
        'marital_status':marriage,
        'age':age,
        'pay_0':pay_0,
        'pay_2':pay_2,
        'pay_3':pay_3,
        'pay_4':pay_4,
        'pay_5':pay_5,
        'pay_6':pay_6,
        'bill_amt_1':bill_amt_1,
        'bill_amt_2':bill_amt_2,
        'bill_amt_3':bill_amt_3,
        'bill_amt_4':bill_amt_4,
        'bill_amt_5':bill_amt_5,
        'bill_amt_6':bill_amt_6,
        'pay_amt_1':pay_amt_1,
        'pay_amt_2':pay_amt_2,
        'pay_amt_3':pay_amt_3,
        'pay_amt_4':pay_amt_4,
        'pay_amt_5':pay_amt_5,
        'pay_amt_6':pay_amt_6,
        }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        # split between numerik and categorical
        data_inf_num = data_inf[['limit_balance']]
        data_inf_cat = data_inf[['pay_0','pay_2', 'pay_3', 'pay_4', 'pay_5', 'pay_6']]
        #feature scaling 
        data_inf_num_scaled = model_scaler.transform(data_inf_num)
        data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat], axis = 1)
        #predict using linear reg model
        y_pred_inf = model_svm.predict(data_inf_final)

        st.write('##Default Payment Next Month: ', str(int(y_pred_inf)), '(0 = Tidak gagal bayar, 1 = Gagal bayar)')

if __name__ == '__main__':
    run()









