#I imported the required third-party libraries
import streamlit as st
import pandas as pd

#set the size of the webpage
st.set_page_config("wide")

#placed a header and introduce the company
st.header("The Best Company")
content1 = """This organisation has a formidable track
            record of over 10 years in the AI industry as a front run. We
            have in last 2 years developed advanced research and application
            patent that are being used by the top fortune companies from Europe
            to Africa
            """
st.write(content1)

#introduce the team
st.subheader("Our Team")
st.write("Meet the team")

#spilted this part of the webpage into columns for ease of placement
col1, col2, col3 = st.columns(3)

#imported the csv file into structured frame for ease of usage
df = pd.read_csv("new_data.csv")

#coded on per column bases to add details of each team member
with col1:
    for index, row in df[0:4].iterrows():
        name = row["last name"] + row["first name"]
        st.subheader(name)
        st.write(row["role"])
        st.image(["Images/" + row["image"]])

with col2:
    for index, row in df[4:8].iterrows():
        name = row["last name"] + row["first name"]
        st.subheader(name)
        st.write(row["role"])
        st.image(["Images/" + row["image"]])


with col3:
    for index, row in df[8:13].iterrows():
        name = row["last name"] + row["first name"]
        st.subheader(name)
        st.write(row["role"])
        st.image(["Images/" + row["image"]])

