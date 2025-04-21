import streamlit as st
import pandas as pd
from utils.wqi4df import calculate_wqi_for_df

st.set_page_config(page_title="WQI Calculator", layout="centered")

st.title("💧 Water Quality Index (WQI) Calculator")
st.write("Tải dữ liệu quan trắc, tính toán chỉ số WQI và tải kết quả về.")

# Section: Download sample template
st.subheader("📄 Mẫu file dữ liệu")
with open("data/wqi_form.csv", "rb") as f:
    st.download_button(
        label="⬇️ Tải form mẫu nhập liệu (CSV)",
        data=f,
        file_name="form_input_template.csv",
        mime="text/csv"
    )

# Section: Upload and process data
uploaded_file = st.file_uploader("📂 Tải file CSV dữ liệu quan trắc", type="csv")

if uploaded_file is not None:
    try:
        # Read CSV file
        df = pd.read_csv(uploaded_file)
        df = df.drop(index=0).reset_index(drop=True)

        # Show original data
        with st.expander("🔍 Xem dữ liệu gốc"):
            st.dataframe(df.head())

        # Calculate WQI
        st.info("🔄 Đang tính toán chỉ số WQI...")
        df_result = calculate_wqi_for_df(df)

        # Show result
        st.success("✅ Tính toán hoàn tất!")
        st.dataframe(df_result.head(10))

        # Download result
        csv = df_result.to_csv(index=False)
        st.download_button(
            label="📥 Tải kết quả dưới dạng CSV",
            data=csv,
            file_name="wqi_form_result.csv",
            mime="text/csv"
        )
    except Exception as e:
        st.error(f"❌ Lỗi khi xử lý file: {e}")
else:
    st.warning("⏳ Vui lòng tải lên một file CSV để bắt đầu.")
