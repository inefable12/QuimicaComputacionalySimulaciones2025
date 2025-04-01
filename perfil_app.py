import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_energy_diagram(reactant, transition, product):
    states = ['Reactante', 'Estado de Transición', 'Producto']
    energies = [reactant, transition, product]
    positions = [0, 1, 2]
    
    fig, ax = plt.subplots(figsize=(6, 4))

    for pos, energy in zip(positions, energies):
        ax.hlines(y=energy, xmin=pos - 0.2, xmax=pos + 0.2, colors='b', linewidth=4)
        ax.text(pos, energy - 5, f"{energy} kJ/mol", ha='center', fontsize=12)
    
    ax.plot(positions, energies, linestyle='--', color='gray', linewidth=1)
    ax.set_xticks(positions)
    ax.set_xticklabels(states)
    ax.set_ylabel('Energía (kJ/mol)')
    ax.set_title('Diagrama de Perfil de Energía')
    ax.grid(True, linestyle='--', alpha=0.6)
    
    st.pyplot(fig)

    # Cálculo de parámetros cinéticos y termodinámicos
    cinetica = transition - reactant
    termodinamica = product - reactant
    
    st.write(f"Cinética (E_activación): {cinetica} kJ/mol")
    st.write(f"Termodinámica (ΔH): {termodinamica} kJ/mol")
    
    if termodinamica > 0:
        st.write("La reacción es endotérmica")
    else:
        st.write("La reacción es exotérmica")

st.title('Generador de Diagramas de Perfil de Energía')

reactant_energy = st.number_input('Energía del Reactante (kJ/mol)', value=0.0)
transition_energy = st.number_input('Energía del Estado de Transición (kJ/mol)', value=50.0)
product_energy = st.number_input('Energía del Producto (kJ/mol)', value=-20.0)

if st.button('Generar Diagrama'):
    plot_energy_diagram(reactant_energy, transition_energy, product_energy)
