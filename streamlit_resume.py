import streamlit as st

# resume title
st.title('Aditya Kadrekar')
st.markdown('[github.com/adityakadrekar16](https://github.com/adityakadrekar16)')

# choose filter
st.sidebar.title('Choose ...')
check_button = st.sidebar.radio("What's your favorite movie genre", ('Comedy', 'Drama', 'Documentary'))

if check_button == 'Comedy':
  st.write('It works')


# https://github.com/streamlit/streamlit/issues/1088
# base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
# pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">' 
# st.markdown(pdf_display, unsafe_allow_html=True)
