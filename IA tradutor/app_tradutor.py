import streamlit as st
import requests

list_linguas = {
    "Português (pt)": "pt-br",
    "Inglês (en)": "en",
    "Espanhol (es)": "es",
    "Francês (fr)": "fr",
    "Alemão (de)": "de",
    "Italiano (it)": "it",
    "Japonês (ja)": "ja",
    "Coreano (ko)": "ko",
    "Chinês (zh-CN)": "zh-CN"

}

#convertendo tipo dict_keys em lista
idiomas = list(list_linguas.keys())

#trabalhando com a API 
def traduzir(texto , idioma_origem , idioma_destino):
    url = "https://api.mymemory.translated.net/get"

    

    params = {"q": texto,
              "langpair": f"{list_linguas[idioma_origem]}|{list_linguas[idioma_destino]}",
              "de": "rayssa@app.com"
                
                }
    
    response = requests.get(url , params=params, timeout=10)
    
    response.raise_for_status()

    return response.json()["responseData"]["translatedText"]

#Interface
st.markdown("<h1 style='text-align: center;'>Tradutor com IA 🧠🈳</h1>", unsafe_allow_html=True)
st.divider()

texto = st.text_area("Insira o texto a ser traduzido:")

idioma_origem = st.selectbox("Idioma de origem", idiomas)

idioma_destino = st.selectbox("Idioma de Destino", idiomas)

if st.button("Traduzir  🤖"):
    if texto.strip() and idioma_origem!= idioma_destino:
        try:
            traducao = traduzir(texto , idioma_origem , idioma_destino)

            st.success("Tradução: ")
            st.write(traducao)

            #opção de download da tradução
            st.divider()
            st.write("Faça o Download da tradução em arquivo .txt ")
            st.download_button(label="Download 📂",
                           data=traducao,
                           file_name="tradução.txt",
                           mime="text/plain")

        #caso de erro com a API
        except Exception as e:
            st.error(f"Erro ao traduzir com MyMemory: {str(e)}")
    
    #erro do usuario
    else:
        st.warning("⚠️ Verifique as informações inseridas ou selecionadas ")


