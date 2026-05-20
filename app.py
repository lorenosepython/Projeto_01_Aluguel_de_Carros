import streamlit as st
st.title('Rosy Maple Moth Carros')
st.subheader('Carros inspirados na mariposa Dyrocampa Rubicunda')
st.sidebar.title('Escolha um modelo de carro🦋')
st.sidebar.image('logo.png')
carros = ["BMW", 'Mustang', 'AstonMartin', 'Koenigsegg', 'Corvette', 'Koenigsegg', 'McLaren']
opcao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)


st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo {opcao}')
st.markdown('---')