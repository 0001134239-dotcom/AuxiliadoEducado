import streamlit as st
import numpy as np
import math
import matplotlib.pyplot as plt

st.title('Trabalhando com Abas')

aba1, aba2, aba3, aba4 = st.tabs(['Sequence of Fibonacci', 'Geral Relativity', 'Probality','Black Holes'])

with aba1:
    st.title('Sequence of Fibonacci')
    st.text('Função onde a partir do 3° termo o próximo é a soma dos dois anteriores')
    
    n = st.number_input('Número de termos', min_value=1, step=1)

    def fibonacci_sequence(qtd):
        a, b = 0, 1
        seq = []
        for _ in range(qtd):
            seq.append(a)
            a, b = b, a + b
        return seq
    if n:
        seq = fibonacci_sequence(int(n))
        st.write(f'Sequência de Fibonacci com {int(n)} termos:')
        st.write(seq)
        st.subheader('Gráfico da Sequência de Fibonacci')
        fig, ax = plt.subplots()
        ax.plot(range(len(seq)), seq, marker='o', linestyle='-', color='blue')
        ax.set_xlabel('Índice')
        ax.set_ylabel('Valor')
        ax.set_title('Sequência de Fibonacci')
        st.pyplot(fig)
with aba2:
    st.title('Geral Relativity')
    st.text('Compreensão da gravidade ao descrevê-la como uma manifestação da curvatura do espaço-tempo causada por objetos massivos')
    
    raio = st.number_input('Raio do planeta escolhido:',min_value= 1)
    massa = st.number_input('Massa do planeta:', min_value= 1)
    tempo = st.number_input('Tempo de medição:', min_value = 1)
    r = raio
    m = massa 
    t0 = tempo
    g = 6.67430e-11
    c = 2.99792458e8
    t = t0 / math.sqrt(1 - (2 * g * m) / (r * c**2))
    st.text(f'Tempo visto por um observador estacionário é de aproximadamente: {t}')
with aba3:
    st.title('Probability')
    st.text('Cálculo de três eventos de acontecerem.(Considerando que em todos os casos tenham apenas 1 evento caracterizado como sucesso.)')
    
    A = st.number_input('Número de casos do evento A',min_value = 1)
    B = st.number_input('Número de casos do evento B',min_value = 1)
    C = st.number_input('Número de casos do evento C',min_value = 1)
    
    AeB = (1/A)*(1/B)
    AeC = (1/A)*(1/B)
    BeC = (1/B)*(1/C)
    AeBeC = (1/A)*(1/B)*(1/C)
    ABC = (1/A)+(1/B)+(1/C)-(AeB)-(AeC)-(BeC)-(AeBeC)
    
    st.text(f'Probabilidade de acontecer A e B: {AeB}')
    st.text(f'Probabilidade de acontecer A e C: {AeC}')
    st.text(f'Probabilidade de acontecer B e C: {BeC}')
    st.text(f'Probabilidade de acontecer A e B e C: {AeBeC}')
    st.text(f'Probabilidade de acontecer A ou B ou C: {ABC}')
with aba4:
    st.title('Black Holes Temperature')
    st.text('Cálculo da temperatura de um buraco negro')
    massa = st.number_input('Massa do buraco negro')
    
    c = 2.99792458e8
    h = 1.055e-34
    G = 6.67430e-11
    k = 1.381e-23
    m = massa
    pi = math.pi
    
    t = ((c**3)*h) / 8*pi*G*k*m
    apr = round(massa,2)
    st.text(f'A temperatura do buraco negro de massa {apr} é de aproximadamente {t}')
    fig, ax = plt.subplots()
    massas = np.logspace(20, 35, 200)
    temp = ((c**3)*h) / 8*pi*G*k*massas
    ax.plot(massas, temp)
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Massa do buraco negro (kg)')
    ax.set_ylabel('Temperatura (K)')
    ax.set_title('Temperatura vs Massa do Buraco Negro')
    ax.grid(True, which="both", ls="--", linewidth=0.5)
    
    st.pyplot(fig)