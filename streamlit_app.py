import streamlit as st

st.title("Mucha hambre o que pirobo")
st.write("Diga a ver qué tiene pa' comer.")

recetas = {
    "Arroz con pollo": ["arroz", "pollo", "zanahoria", "cebolla"],
    "Ensalada fresca": ["lechuga", "tomate", "limon", "sal"],
    "Omelette básico": ["huevo", "sal", "aceite", "queso"],
    "Pasta rápida": ["pasta", "tomate", "ajo", "queso"]
}

ingredientes_input = st.text_input("Ingredientes que tiene (separados por comas):")

if st.button("COCINAAAAAR"):
    if ingredientes_input:
        ingredientes_usuario = [i.strip().lower() for i in ingredientes_input.split(",")]
        
        st.write("---")
        st.subheader("Resultados de la búsqueda:")
        
        for nombre_receta, ingredientes_necesarios in recetas.items():
            coincidencias = 0
            ingredientes_faltantes = []
            
            for ing in ingredientes_necesarios:
                if ing in ingredientes_usuario:
                    coincidencias += 1
                else:
                    ingredientes_faltantes.append(ing)
            
            porcentaje = int((coincidencias / len(ingredientes_necesarios)) * 100)
            
            if porcentaje == 100:
                st.success(f"¡Puede hacer **{nombre_receta}** al 100%! ¡Tienes todo!")
            elif porcentaje >= 50:
                st.info(f"Se podría hacer **{nombre_receta}** ({porcentaje}% de los ingredientes). Le falta: {', '.join(ingredientes_faltantes)}")
            else:
                pass
    else:
        st.error("Por favor escriba qué tiene pa' cocinar.")
