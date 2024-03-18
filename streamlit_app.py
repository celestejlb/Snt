import streamlit as st
import panda as pd
import numpy as py
voc=pd.read_csv('lien')
st.dataframe(voc)
l=voc.shape[0]
i=hp.random.choice(range(l))
word_fr=voc['Definition'].values[i]
word_chi=voc['?'].values[i]
st.write(word_fr+""+word_chi)
st.button("refresh")
