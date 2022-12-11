import pickle 
import numpy as np
import streamlit as st

model = pickle.load(open('survived_titanic.sav', 'rb'))

st.title('prediksi keselamatan penumpang titanic')

col1, col2 = st.columns(2)

with col1 :
	Pclass = st.number_input('input kelas penumpang')

	sex = st.number_input('input jenis kelamin (male : 1 female : 2)')

	age = st.number_input('input umur')

	SibSp = st.number_input('input jumlah saudara')

with col2:	
	Parch = st.number_input('input jumlah orang tua')

	Fare = st.number_input('input jumlah tarif')

	Embarked = st.number_input('input keberangkatan (Southampton(S) : 1, Cherbourg(C) : 2, Queenstown(Q) : 3)')

prediksi = ''

if st.button('prediksi keselamatan penumpang'):
	survive_prediksi = model.predict([[Pclass, sex, age, SibSp, Parch, Fare, Embarked]])

	if(survive_prediksi[0]==1):
		prediksi = 'penumpang selamat'
	else :
		prediksi = 'penumpang meninggal'
st.success(prediksi)
