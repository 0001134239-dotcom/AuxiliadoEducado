import streamlit as st

st.title('Aceita jogar jogo da velha aceitando os termos e condições?')
col1, col2 = st.columns(2)
with col1:
    b1 = st.button('Sim')

with col2:
    b2 = st.button('Não')

if b2:
    st.warning('Resposta inválida')
elif b1:
    st.text('Obrigado por aceitar os termos e condições.')
    st.text('--'*30)
    st.write('Termos e Condições')
    st.text('Não roubar igual da última vez pq foi mt feio, aceitar q vai perder todas e se perder me deve a kiss (se ganhar tu se fode pq é impossivel)')
