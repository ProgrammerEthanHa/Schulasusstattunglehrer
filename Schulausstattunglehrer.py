import streamlit as st
import pandas as pd
import altair as alt

st.header("Schüler kritischer hinsichtlich der Schulausstattung - Lehrer")
st.subheader("Einschätzung der derzeitigen Computer- und Internetausstattung der Schule - Lehrer")

source = pd.DataFrame({
        'Anteil(%)': [21, 37, 36, 6, 0],
        'Einschätzung': ['sehr gut', 'gut', 'mittelmäßig', 'schlecht', 'sehr schlecht']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Einschätzung:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Bitkom")