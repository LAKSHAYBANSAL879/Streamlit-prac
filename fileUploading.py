import streamlit as st 
import pandas as pd
from PIL import Image
st.title("Uploading a image")
img_file=st.file_uploader('Upload a image',type=["jpeg","png","jpg"])
if img_file is not None:
    st.write(type(img_file))
    file_details={'file_name':img_file.name,'file_type':img_file.type,'file_size':img_file.size}
    st.write(file_details)
    st.image(Image.open(img_file))