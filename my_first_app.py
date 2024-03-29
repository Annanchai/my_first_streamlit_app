import streamlit as st 
import numpy as np
import altair as alt
import pandas as pd 


st.header('st.write')

st.write('Hello, *World!* :sunglasses:')

st.write(1234)

df = pd.DataFrame({
    'first_coloumn':[1,2,3,4],
    'second_coloumn':[10,20,30,40]
})

st.write(df)

st.write('Below is a :red[Dataframe]:', df, 'Above is a Dataframe')

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', tooltip=['a', 'b', 'c']
)
st.write(c)
st.write(df2)