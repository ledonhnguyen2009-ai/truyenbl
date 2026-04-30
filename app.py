import streamlit as st

st.set_page_config(page_title="App Truyện của Nguyên", page_icon="📚")

st.title("📚 Đang đọc: Truyện BL")

# Lệnh để app tự đọc file truyện bạn vừa tải lên
try:
    with open("truyện bl.txt", "r", encoding="utf-8") as f:
        noi_dung = f.read()
    
    # Hiển thị nội dung ra màn hình
    st.markdown("---")
    st.write(noi_dung)
    
except FileNotFoundError:
    st.error("Không tìm thấy file truyện bl.txt trên GitHub!")
