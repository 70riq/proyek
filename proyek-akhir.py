import streamlit as st 

st.title("Proyek Analisis Data")

st.header("Thoriq Rizky Dwiputra\n700riq")

st.image("payment.png", caption="Penggunaan tiap jenis pembayaran")

with st.expander("See Explanation"):
    st.write(
        """Pada bar chart diatas dapat disimpulkan credit card adalah jenis pembayaran yang paling sering digunakan."""
    )

st.image("product.png", caption="Top 10 Produk Terlaris")
with st.expander("See Explanation"):
    st.write(
        """Pada bar chart diatas terdapat 10 produk yang paling laris. Bed Bath Table adalah produk paling laris diantara yang lain."""
    )
 
 

