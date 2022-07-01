from time import time
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title("This is a Title")
st.text("Das ist der Text") 
st.markdown("Streamlit is ***really cool*** :+1:")
st.header("Haydi Header")
st.subheader("This a sub")

st.success("This a success")
st.info("bu bir info")
st.error("bu bir error")
st.spinner("sadsw3e")
st.write('Hello",*World* :sunglasses:')
img=Image.open("images.jpeg")
st.image(img,caption="cattie",width=500)
st.help(st.image)

my_video=open("ml.mov","rb")
st.video(my_video)
st.video("https://www.youtube.com/watch?v=uHKfrz65KSU")

cbox=st.checkbox("Hide and seek")

if cbox:
    st.write("Hide")
else: 
    st.video("https://www.youtube.com/watch?v=uHKfrz65KSU")
    
    
    
st.radio("Select a color",("blue","orange","yellow"))

status=st.radio("Select a color",("Blue","Orange","Yellow"))
st.write(status)

st.button("Button")
if st.button("Press Me"):
    st.success("Analyse result are..")
else:
    ("Hadi Bas")
    
occupation=st.selectbox("My occupation",["Police","Doctor"])


#multi_select
multi_select = st.multiselect("Select multiple numbers",[1,2,3,4,5])
sn = st.selectbox("Select a number",[1,2,3,4,5])

option1=st.slider("Select a number",min_value=50,max_value=300,value=100,step=5)
option2 = st.slider("Select a number",20,200,100,7)
option3 = st.slider("Select a number",20,200,100)
option1*option2




age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

name=st.text_input("Enter your Name",placeholder="Your name here")
if st.button("Submit"):
    st.success(name.title())
    st.snow()
    st.balloons()
    st.balloons()
    st.balloons()
    st.balloons()
    st.snow()
    
    
with st.spinner("wait wait"):
    
    st.success("Done!")
    
    st.code("import pandas as pd")
st.code("import pandas as pd\nimport numpy as np")
with st.echo():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({"a":[1,2,3], "b":[4,5,6]})
    df
    

import datetime
today=st.date_input("Today is",datetime.datetime.now())
d=st.date_input("My Birthday",datetime.date(1982,5,30))

#st.help(st.date_input)
the_time=st.time_input("The time is",datetime.time(8,45))
the_timem=st.time_input("The time is")
#st.sidebar.title("sewred")
st.title("sedede")
st.title(955555555)
a=st.sidebar.slider("input",0,5,2,1)
x=st.sidebar.slider("input2")
st.success(a*x)


df=pd.read_csv("Advertising (1).csv", nrows=(100))
df
st.table(df.head())
st.write(df.head())
st.dataframe(df.head())

import pickle
filename = "finalized_model.sav"
model = pickle.load(open(filename, "rb"))
a = st.sidebar.number_input("TV:",value=230, step=10)
b = st.sidebar.number_input("radio:",value=37, step=10)
c = st.sidebar.number_input("newspaper:",value=69, step=10)
if st.button("Predict"): 
    pred = model.predict([[a,b,c]])
    st.write(pred)
    
html_temp = """
<div style="background-color:tomato;padding:1.5px">
<h1 style="color:white;text-align:center;">Single Customer </h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)

tenure=st.sidebar.slider("Number of months the customer has stayed with the company (tenure)", 1, 72, step=1)
MonthlyCharges=st.sidebar.slider("The amount charged to the customer monthly", 0,100, step=5)
TotalCharges=st.sidebar.slider("The total amount charged to the customer", 0,5000, step=10)
Contract=st.sidebar.selectbox("The contract term of the customer", ('Month-to-month', 'One year', 'Two year'))
OnlineSecurity=st.sidebar.selectbox("Whether the customer has online security or not", ('No', 'Yes', 'No internet service'))
InternetService=st.sidebar.selectbox("Customer’s internet service provider", ('DSL', 'Fiber optic', 'No'))
TechSupport=st.sidebar.selectbox("Whether the customer has tech support or not", ('No', 'Yes', 'No internet service'))
def single_customer():
    my_dict = {"tenure" :tenure,
        "OnlineSecurity":OnlineSecurity,
        "Contract": Contract,
        "TotalCharges": TotalCharges ,
        "InternetService": InternetService,
        "TechSupport": TechSupport,
        "MonthlyCharges":MonthlyCharges}
    df_sample = pd.DataFrame.from_dict([my_dict])
    return df_sample
df = single_customer()
st.table(df)