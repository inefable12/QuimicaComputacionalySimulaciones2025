import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_energy_diagram(reactant, transition, product):
    states = ['Reactante', 'Estado de Transición', 'Producto']
    energies = [reactant, transition, product]
    
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot([0, 1, 2], energies, marker='o', linestyle='-', color='b')
    
    for i, txt in enumerate(energies):
        ax.text(i, energies[i] + 1, f"{txt} kJ/mol", ha='center', fontsize=12)
    
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(states)
    ax.set_ylabel('Energía (kJ/mol)')
    ax.set_title('Diagrama de Perfil de Energía')
    ax.grid(True, linestyle='--', alpha=0.6)
    
    st.pyplot(fig)

st.title('Generador de Diagramas de Perfil de Energía')

reactant_energy = st.number_input('Energía del Reactante (kJ/mol)', value=0.0)
transition_energy = st.number_input('Energía del Estado de Transición (kJ/mol)', value=50.0)
product_energy = st.number_input('Energía del Producto (kJ/mol)', value=-20.0)

if st.button('Generar Diagrama'):
    plot_energy_diagram(reactant_energy, transition_energy, product_energy)
