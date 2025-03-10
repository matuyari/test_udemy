from PIL import Image
import streamlit as st
import time


if st.checkbox("Show image"):
  img = Image.open(r"C:\Users\yuto2\Downloads\20230910_175446403.jpg")
  st.image(img, caption="sample image", use_container_width=True)

expander1 = st.expander("問い合わせ")
expander1.write("内容")


st.write("プログレスバー")
"Start"
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(0, 100):
  latest_iteration.text(f"iteration: {i+1}")
  bar.progress(i+1)
  time.sleep(0.01)
"Done"
