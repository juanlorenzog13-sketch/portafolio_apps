import streamlit as st

st.set_page_config(
    page_title="Mi Portafolio de Apps",
    page_icon="<>",
    layout="wide"
)

PROJECTS = [
    {
        "title": "OCR + Audio",
        "url": "https://ocr-audio-zkyxqh6awyp5evjsrpxzad.streamlit.app/",
        "category": "IA / Visión",
        "ascii": r"""
  .----.
 / OCR \
| AUDIO |
 \____/
""",
        "description": "Aplicación relacionada con OCR y audio."
    },
    {
        "title": "Proyecto 02",
        "url": "https://junms5ttspuarlxs5ngawq.streamlit.app/",
        "category": "General",
        "ascii": r"""
  .----.
 / app \
|  02  |
 \____/
""",
        "description": "Proyecto Streamlit general."
    },
    {
        "title": "IntroCopia",
        "url": "https://introcopia.streamlit.app/",
        "category": "General",
        "ascii": r"""
  ______
 / intro\
| copia |
 \______/
""",
        "description": "Aplicación IntroCopia."
    },
    {
        "title": "IMM1Copia1",
        "url": "https://imm1copia1.streamlit.app/",
        "category": "General",
        "ascii": r"""
  ______
 / imm1 \
| copia |
 \__1___/
""",
        "description": "Aplicación IMM1Copia1."
    },
    {
        "title": "Proyecto 05",
        "url": "https://rutq8isvy6xhgper5lxutc.streamlit.app/",
        "category": "General",
        "ascii": r"""
  .----.
 / app \
|  05  |
 \____/
""",
        "description": "Proyecto Streamlit general."
    },
    {
        "title": "Ejercicio de Dibujo",
        "url": "https://ejerciciodibujojuan-hmxcm3upmjyzhyofumilq2.streamlit.app/",
        "category": "Dibujo",
        "ascii": r"""
  /\_/\
 ( o.o )
  > ^ <
""",
        "description": "Ejercicio de dibujo interactivo."
    },
    {
        "title": "Draw Recognition",
        "url": "https://drawrecog-ccrywsbya3cufwk95aa9zf.streamlit.app/",
        "category": "Dibujo / IA",
        "ascii": r"""
  _____
 /draw \
| recog |
 \_____/
""",
        "description": "Reconocimiento de dibujos."
    },
    {
        "title": "Control por Voz",
        "url": "https://ctrlvoice-vxdhiu8ltvdvvqc9mwgjmr.streamlit.app/",
        "category": "Voz / MQTT",
        "ascii": r"""
  .-.-.
 (  o  )
 /|___|\
""",
        "description": "Aplicación de control por voz."
    },
    {
        "title": "ChatPDF",
        "url": "https://chatpdf-m6jnzuqv4fekxho2fgy9j3.streamlit.app/",
        "category": "IA / Documentos",
        "ascii": r"""
  ______
 / PDF  \
| CHAT  |
 \______/
""",
        "description": "Chat con documentos PDF."
    },
    {
        "title": "YOLOv5",
        "url": "https://yolov5-cyulvhjkn898fljo4g5fa5.streamlit.app/",
        "category": "IA / Visión",
        "ascii": r"""
  ____
 / __ \
| YOLO |
 \____/
""",
        "description": "Aplicación basada en YOLOv5."
    },
    {
        "title": "WordCloud",
        "url": "https://wordcloud-kt3xzhgqvrrlxxwmypznpz.streamlit.app/",
        "category": "Texto / Visualización",
        "ascii": r"""
  .-~~-.
 ( text )
( cloud )
 `-__-'
""",
        "description": "Generación de nubes de palabras."
    },
    {
        "title": "Vision App",
        "url": "https://visionapp-kjq8a6m86xoputjhgvs4xq.streamlit.app/",
        "category": "IA / Visión",
        "ascii": r"""
  .----.
 / eye  \
| app   |
 \------/
""",
        "description": "Aplicación de visión por computador."
    },
    {
        "title": "Traductor",
        "url": "https://traductor-2c23ljlzz6vgsnpnxgo4cz.streamlit.app/",
        "category": "Lenguaje",
        "ascii": r"""
  _____
 / A>B \
| words |
 \_____/
""",
        "description": "Aplicación de traducción."
    },
    {
        "title": "Proyecto 14",
        "url": "https://jbvappgsro9ke64u5htcr74.streamlit.app/",
        "category": "General",
        "ascii": r"""
  .----.
 / app \
|  14  |
 \____/
""",
        "description": "Proyecto Streamlit general."
    },
    {
        "title": "Proyecto 15",
        "url": "https://qdqpcvqzetnxr4u5wrsd63.streamlit.app/",
        "category": "General",
        "ascii": r"""
  .----.
 / app \
|  15  |
 \____/
""",
        "description": "Proyecto Streamlit general."
    },
    {
        "title": "TDF ESP",
        "url": "https://tdfesp-aroqdtmk5wnrthrktq36eq.streamlit.app/",
        "category": "General",
        "ascii": r"""
  _____
 / TDF \
| ESP  |
 \_____/
""",
        "description": "Aplicación TDF ESP."
    },
    {
        "title": "Tablero Prop",
        "url": "https://tableroprop-ab9xustaukqkavmgxaceeq.streamlit.app/",
        "category": "Dibujo",
        "ascii": r"""
  _____
 /board\
| prop |
 \_____/
""",
        "description": "Tablero interactivo."
    },
    {
        "title": "Sentimenta",
        "url": "https://sentimenta-uhlb3gxq4bmmlb7eytu2mq.streamlit.app/",
        "category": "IA / Texto",
        "ascii": r"""
  _____
 / senti\
| menta |
 \_____/
""",
        "description": "Aplicación de análisis de sentimiento."
    },
    {
        "title": "Enviar MQTT",
        "url": "https://sendcmqtt-bwdhohi2yc42jhowl72jhy.streamlit.app/",
        "category": "MQTT / IoT",
        "ascii": r"""
  .----.
 / send \
| MQTT  |
 \____/
""",
        "description": "Aplicación para enviar datos por MQTT."
    },
    {
        "title": "Recibir MQTT",
        "url": "https://recepmqtt-auzq9jm9nwfcaphbl7bssb.streamlit.app/",
        "category": "MQTT / IoT",
        "ascii": r"""
  .----.
 / recv \
| MQTT  |
 \____/
""",
        "description": "Aplicación para recibir datos por MQTT."
    },
]

st.markdown("""
<style>
    .main {
        background-color: #0f172a;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .hero {
        padding: 1.5rem 1.5rem 1rem 1.5rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #111827 0%, #1f2937 100%);
        border: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 1.2rem;
    }
    .hero h1 {
        margin: 0;
        color: white;
        font-size: 2.2rem;
    }
    .hero p {
        margin-top: 0.6rem;
        color: #cbd5e1;
        font-size: 1rem;
    }
    .card {
        background: #111827;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 18px;
        padding: 1rem;
        min-height: 320px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.25);
    }
    .card-title {
        color: white;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 0.35rem;
    }
    .card-category {
        display: inline-block;
        padding: 0.25rem 0.6rem;
        border-radius: 999px;
        background: #1d4ed8;
        color: white;
        font-size: 0.8rem;
        margin-bottom: 0.8rem;
    }
    .card-desc {
        color: #cbd5e1;
        font-size: 0.95rem;
        min-height: 52px;
    }
    .ascii-box {
        background: #0b1220;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 0.75rem;
        color: #93c5fd;
        font-family: monospace;
        font-size: 0.95rem;
        white-space: pre;
        margin: 0.8rem 0;
    }
    .counter {
        color: #93c5fd;
        font-weight: 600;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>Mi Portafolio de Apps en Streamlit</h1>
    <p>
        Esta página reúne las aplicaciones web que he desarrollado con Streamlit.
        Puedes explorarlas por categoría o buscarlas por nombre.
    </p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("Filtros")
    search = st.text_input("Buscar proyecto", "")
    categories = sorted(set(p["category"] for p in PROJECTS))
    selected_category = st.selectbox("Categoría", ["Todas"] + categories)

filtered = []
for project in PROJECTS:
    matches_search = search.lower() in project["title"].lower() or search.lower() in project["description"].lower()
    matches_category = selected_category == "Todas" or project["category"] == selected_category
    if matches_search and matches_category:
        filtered.append(project)

st.markdown(f'<div class="counter">Proyectos mostrados: {len(filtered)}</div>', unsafe_allow_html=True)

cols_per_row = 3
for i in range(0, len(filtered), cols_per_row):
    row = st.columns(cols_per_row)
    for col, project in zip(row, filtered[i:i + cols_per_row]):
        with col:
            st.markdown(
                f"""
                <div class="card">
                    <div class="card-title">{project['title']}</div>
                    <div class="card-category">{project['category']}</div>
                    <div class="card-desc">{project['description']}</div>
                    <div class="ascii-box">{project['ascii']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.link_button("Abrir app", project["url"], use_container_width=True)

if not filtered:
    st.warning("No se encontraron proyectos con esos filtros.")
