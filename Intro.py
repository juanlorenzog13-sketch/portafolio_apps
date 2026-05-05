import streamlit as st

st.set_page_config(
    page_title="Portafolio | Apps en Streamlit",
    page_icon="◇",
    layout="wide"
)

PROJECTS = [
    {
        "title": "OCR + Audio",
        "url": "https://ocr-audio-zkyxqh6awyp5evjsrpxzad.streamlit.app/",
        "category": "Visión",
        "ascii": r"""
  .----.
 / OCR \
|AUDIO |
 \____/
""",
        "description": "Aplicación relacionada con OCR y audio."
    },
    {
        "title": "Reconocimiento visual de texto para ayudas accesibles",
        "url": "https://junms5ttspuarlxs5ngawq.streamlit.app/",
        "category": "Visión",
        "ascii": r"""
  _____
 /TEXT \
| VIEW |
 \_____/
""",
        "description": "Reconocimiento visual de texto pensado para accesibilidad y apoyo a usuarios."
    },
    {
        "title": "IntroCopia",
        "url": "https://introcopia.streamlit.app/",
        "category": "General",
        "ascii": r"""
  _____
 /INTRO\
|COPY  |
 \_____/
""",
        "description": "Aplicación introductoria de prueba y exploración."
    },
    {
        "title": "IMM1Copia1",
        "url": "https://imm1copia1.streamlit.app/",
        "category": "General",
        "ascii": r"""
  _____
 / IMM \
|COPY  |
 \__1__/
""",
        "description": "Aplicación experimental de interfaz."
    },
    {
        "title": "Reconocimiento de Dígitos escritos a mano",
        "url": "https://rutq8isvy6xhgper5lxutc.streamlit.app/",
        "category": "Dibujo",
        "ascii": r"""
  _____
 / 123 \
| HAND |
 \_____/
""",
        "description": "Reconocimiento de números escritos a mano a partir de trazos en pantalla."
    },
    {
        "title": "Ejercicio de Dibujo",
        "url": "https://ejerciciodibujojuan-hmxcm3upmjyzhyofumilq2.streamlit.app/",
        "category": "Dibujo",
        "ascii": r"""
  /\_/\ 
 ( . . )
  > ^ <
""",
        "description": "Ejercicio interactivo de dibujo en canvas."
    },
    {
        "title": "Draw Recognition",
        "url": "https://drawrecog-ccrywsbya3cufwk95aa9zf.streamlit.app/",
        "category": "Dibujo",
        "ascii": r"""
  _____
 /DRAW \
|RECOG |
 \_____/
""",
        "description": "Reconocimiento de dibujos realizados por el usuario."
    },
    {
        "title": "Control por Voz",
        "url": "https://ctrlvoice-vxdhiu8ltvdvvqc9mwgjmr.streamlit.app/",
        "category": "Voz",
        "ascii": r"""
  .-.-.
 ( o o )
 /|___|\
""",
        "description": "Control de acciones por comandos de voz."
    },
    {
        "title": "ChatPDF",
        "url": "https://chatpdf-m6jnzuqv4fekxho2fgy9j3.streamlit.app/",
        "category": "Texto",
        "ascii": r"""
  _____
 / PDF \
|CHAT |
 \_____/
""",
        "description": "Interacción con documentos PDF mediante preguntas y respuestas."
    },
    {
        "title": "YOLOv5",
        "url": "https://yolov5-cyulvhjkn898fljo4g5fa5.streamlit.app/",
        "category": "Visión",
        "ascii": r"""
  ____
 / __ \
|YOLO|
 \____/
""",
        "description": "Aplicación basada en detección de objetos con YOLOv5."
    },
    {
        "title": "WordCloud",
        "url": "https://wordcloud-kt3xzhgqvrrlxxwmypznpz.streamlit.app/",
        "category": "Texto",
        "ascii": r"""
  .----.
 /WORD \
|CLOUD|
 \____/
""",
        "description": "Generador de nubes de palabras."
    },
    {
        "title": "Vision App",
        "url": "https://visionapp-kjq8a6m86xoputjhgvs4xq.streamlit.app/",
        "category": "Visión",
        "ascii": r"""
  .----.
 / EYE \
| APP  |
 \----/
""",
        "description": "Aplicación de visión por computador."
    },
    {
        "title": "Traductor",
        "url": "https://traductor-2c23ljlzz6vgsnpnxgo4cz.streamlit.app/",
        "category": "Texto",
        "ascii": r"""
  _____
 /A > B\
|WORDS |
 \_____/
""",
        "description": "Aplicación de traducción de texto."
    },
    {
        "title": "Reconocimiento de Imágenes autoritario",
        "url": "https://jbvappgsro9ke64u5htcr74.streamlit.app/",
        "category": "Visión",
        "ascii": r"""
  _____
 /SCAN \
|IMAGE |
 \_____/
""",
        "description": "Reconocimiento de imágenes."
    },
    {
        "title": "Proto-chat de texto",
        "url": "https://qdqpcvqzetnxr4u5wrsd63.streamlit.app/",
        "category": "Texto",
        "ascii": r"""
  _____
 /CHAT \
|PROTO |
 \_____/
""",
        "description": "Lee texto ingresado por el usuario y responde preguntas con base en ese contenido."
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
        "description": "Aplicación general de prueba."
    },
    {
        "title": "Tablero Prop",
        "url": "https://tableroprop-ab9xustaukqkavmgxaceeq.streamlit.app/",
        "category": "Dibujo",
        "ascii": r"""
  _____
 /BOARD\
| PROP |
 \_____/
""",
        "description": "Tablero interactivo para dibujo y experimentación."
    },
    {
        "title": "Sentimenta",
        "url": "https://sentimenta-uhlb3gxq4bmmlb7eytu2mq.streamlit.app/",
        "category": "Texto",
        "ascii": r"""
  _____
 /SENTI\
|MENTA |
 \_____/
""",
        "description": "Aplicación de análisis de sentimiento."
    },
    {
        "title": "Enviar MQTT",
        "url": "https://sendcmqtt-bwdhohi2yc42jhowl72jhy.streamlit.app/",
        "category": "MQTT",
        "ascii": r"""
  .----.
 /SEND \
|MQTT |
 \____/
""",
        "description": "Envía datos y comandos usando MQTT."
    },
    {
        "title": "Recibir MQTT",
        "url": "https://recepmqtt-auzq9jm9nwfcaphbl7bssb.streamlit.app/",
        "category": "MQTT",
        "ascii": r"""
  .----.
 /RECV \
|MQTT |
 \____/
""",
        "description": "Recibe y visualiza datos desde MQTT."
    },
]

CATEGORY_ORDER = ["Todas", "Visión", "Texto", "Dibujo", "Voz", "MQTT", "General"]

st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1350px;
    }

    .hero {
        padding: 2rem;
        border-radius: 24px;
        background: linear-gradient(135deg, #0f172a 0%, #111827 45%, #1e293b 100%);
        border: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 1.5rem;
        box-shadow: 0 18px 40px rgba(0,0,0,0.28);
    }

    .hero h1 {
        margin: 0;
        color: white;
        font-size: 2.5rem;
        font-weight: 800;
        letter-spacing: -0.02em;
    }

    .hero p {
        margin-top: 0.8rem;
        color: #cbd5e1;
        font-size: 1.02rem;
        max-width: 760px;
        line-height: 1.6;
    }

    .mini-stats {
        display: flex;
        gap: 0.75rem;
        flex-wrap: wrap;
        margin-top: 1rem;
    }

    .mini-stat {
        background: rgba(255,255,255,0.06);
        color: #dbeafe;
        border: 1px solid rgba(255,255,255,0.08);
        padding: 0.55rem 0.9rem;
        border-radius: 999px;
        font-size: 0.9rem;
    }

    .section-title {
        color: #0f172a;
        font-size: 1.35rem;
        font-weight: 800;
        margin: 1.8rem 0 0.8rem 0;
    }

    .card {
        background: #111827;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 1rem;
        min-height: 330px;
        box-shadow: 0 10px 28px rgba(0,0,0,0.22);
    }

    .card-title {
        color: white;
        font-size: 1.15rem;
        font-weight: 700;
        line-height: 1.35;
        margin-bottom: 0.45rem;
    }

    .card-category {
        display: inline-block;
        padding: 0.25rem 0.7rem;
        border-radius: 999px;
        background: #2563eb;
        color: white;
        font-size: 0.78rem;
        margin-bottom: 0.9rem;
        font-weight: 600;
    }

    .card-desc {
        color: #cbd5e1;
        font-size: 0.94rem;
        line-height: 1.5;
        min-height: 72px;
    }

    .ascii-box {
        background: #0b1220;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 14px;
        padding: 0.85rem;
        color: #93c5fd;
        font-family: monospace;
        font-size: 0.95rem;
        white-space: pre;
        margin: 0.9rem 0;
        min-height: 94px;
    }

    .results-note {
        color: #334155;
        font-weight: 600;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

total_projects = len(PROJECTS)
categories_used = len(set(p["category"] for p in PROJECTS))

st.markdown(f"""
<div class="hero">
    <h1>Portafolio de aplicaciones en Streamlit</h1>
    <p>
        Esta página reúne proyectos desarrollados en Streamlit enfocados en visión por computador,
        texto, dibujo, voz e integración con MQTT. El objetivo es mostrar distintas exploraciones
        interactivas en interfaces, inteligencia artificial y prototipos funcionales.
    </p>
    <div class="mini-stats">
        <div class="mini-stat">{total_projects} proyectos</div>
        <div class="mini-stat">{categories_used} categorías</div>
        <div class="mini-stat">Apps interactivas + prototipos</div>
    </div>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("Explorar")
    search = st.text_input("Buscar", "")
    selected_category = st.selectbox("Categoría", CATEGORY_ORDER)

filtered = []
for project in PROJECTS:
    text_match = (
        search.lower() in project["title"].lower()
        or search.lower() in project["description"].lower()
        or search.lower() in project["category"].lower()
    )
    category_match = selected_category == "Todas" or project["category"] == selected_category
    if text_match and category_match:
        filtered.append(project)

st.markdown(
    f"<div class='results-note'>Mostrando {len(filtered)} proyecto(s)</div>",
    unsafe_allow_html=True
)

display_categories = [c for c in CATEGORY_ORDER if c != "Todas"]

for category in display_categories:
    category_projects = [p for p in filtered if p["category"] == category]
    if not category_projects:
        continue

    st.markdown(f"<div class='section-title'>{category}</div>", unsafe_allow_html=True)

    for i in range(0, len(category_projects), 3):
        row = st.columns(3)
        for col, project in zip(row, category_projects[i:i+3]):
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
