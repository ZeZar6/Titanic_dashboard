import streamlit as st
from streamlit import session_state as state    

st.title("Welcome to the Home Page")
tab1, tab2, tab3, tab4, tab5, tab6= st.tabs([
    "Home",
    "Forum", "About us", "Contact us", "Login", "Sign up"
])




with tab1:
    st.write("This is the home page content.")
    st.write("You can navigate to other tabs for more information.")
    colmn1, column2, column3 = st.columns(3, gap="large",vertical_alignment="bottom")
    
    with colmn1:
        st.image("https://fisica.tecnico.ulisboa.pt/media/images/plasmas-lasers-e-Fusao-Nuclear.width-880.jpg", caption="Nuclear Fusion projects")
    with column2:
        st.image("https://th.bing.com/th/id/R.6c2c3e765918c6378a68da5f89439d63?rik=QJqjAas3lWVo9w&riu=http%3a%2f%2fmasteres.ugr.es%2fmtaf%2fpages%2fimagenes%2fimagen%2f!%2f&ehk=6u4GSLl%2fwtxyynZFzGd0iGcU1%2fihZktRoUXMKeqlQJ0%3d&risl=&pid=ImgRaw&r=0", caption="Fiber Optics and Lasers")
    with column3:
        st.image("https://lexica.art/prompt/54c5ca69-eaf5-4ee0-a896-ec61de38c186/opengraph-image?d26e3adb96114073", caption="Seeking new frontiers in physics")  

with tab2:
    st.write("This is the forum page.")
    st.write("Here you can discuss various topics with other users.")
    
with tab3:
    st.write("This is the about us page.")
    st.write("Learn more about our mission and team.")
    column4, column5= st.columns([1,4], gap="large", vertical_alignment="bottom")
    column4.image("https://tse2.mm.bing.net/th/id/OIP.0wnbsl4O6K-RTv0QFtlL3gHaEK?rs=1&pid=ImgDetMain&o=7&rm=3", caption="Dogs are great companions")
    column5.image("https://wallpaperaccess.com/full/527114.jpg", caption="Beautiful Landscape")

with tab4:
    st.write("This is the contact us page.")
    st.write("Get in touch with us through this page.")

with tab5:
    st.write("This is the login page.")
    st.write("Log in to your account.")
    st.sidebar.subheader("Login Form")
    tab5username = st.sidebar.text_input("Username")
    tab5password = st.sidebar.text_input("Password", type="password")


with tab6:
    st.write("This is the sign up page.")
    st.write("Create a new account.")
    

