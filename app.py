import streamlit as st

# Tiêu đề app
st.set_page_config(page_title="App Truyện của Nguyên", page_icon="📚")
st.title("📚 Kho Văn Bản / Truyện")

# Ô để bạn dán nội dung văn bản
text_input = st.text_area("Nhập hoặc dán nội dung văn bản vào đây:", height=300)

if text_input:
    st.subheader("Nội dung hiển thị:")
    st.write(text_input)
    st.success("Đã hiển thị nội dung thành công!")
