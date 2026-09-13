import streamlit as st
import pandas as pd
st.write ("My Stremlit application..")

st.markdown('Text Elements')
st.text('1.2 Displaying basic text')
st.title('This is the title')
st.header('This is the Header')
st.subheader('This is the subheader')
st.text('This is a text')
st.caption('This is a caption ')
st.divider()
st.write('This is a write')
df = pd.DataFrame({'col1':[1,2,3,4], 'col2':[10,20,30,40]})
st.write('Display a data frame using a st.write', df)

st.text('1.6. Displaying formatting and Display Tools')
st.code('x = 134')
st.latex(r'''a + ar +a r^2 ''')

st.image('https://images.pexels.com/photos/37685036/pexels-photo-37685036.jpeg', caption='Data Analysis')

st.video('https://www.pexels.com/download/video/32829410/')
