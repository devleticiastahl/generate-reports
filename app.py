import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Título do app
st.title("Meu App de Análise")

# Exemplo de criação de dataframe
data = {
    'Categoria': ['A', 'B', 'C', 'D'],
    'Valor': [10, 20, 15, 30]
}
df = pd.DataFrame(data)

st.write("Exemplo de DataFrame:")
st.dataframe(df)

# Gráfico de barras
st.write("Gráfico de Barras:")
fig, ax = plt.subplots()
sns.barplot(x='Categoria', y='Valor', data=df, ax=ax)
st.pyplot(fig)

# Exemplo de cálculo NumPy
array = np.array([1, 2, 3, 4, 5])
st.write("Soma do array:", np.sum(array))
