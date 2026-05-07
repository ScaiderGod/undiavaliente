import streamlit as st

# =========================
# Un Dia Valiente - V1
# Juego interactivo para ninos de 3 a 5 anos
# =========================

st.set_page_config(
    page_title="Un Dia Valiente",
    page_icon="🌟",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# -------------------------
# Estilos visuales
# -------------------------
st.markdown(
    """
    <style>
        .main {
            background: #fff8ef;
        }

        .block-container {
            max-width: 900px;
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        .title-box {
            background: linear-gradient(135deg, #ffe6b3, #ffd1dc);
            border-radius: 28px;
            padding: 28px;
            text-align: center;
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
            margin-bottom: 22px;
        }

        .game-title {
            font-size: 52px;
            font-weight: 900;
            color: #3a2c2c;
            line-height: 1.05;
            margin-bottom: 8px;
        }

        .game-subtitle {
            font-size: 26px;
            font-weight: 700;
            color: #5b4a4a;
        }

        .scene-card {
            background: #ffffff;
            border-radius: 30px;
            padding: 28px;
            box-shadow: 0 10px 26px rgba(0,0,0,0.10);
            border: 4px solid #ffe1a8;
            margin-bottom: 20px;
        }

        .scene-image {
            min-height: 260px;
            border-radius: 28px;
            background: linear-gradient(135deg, #dff3ff, #fff2c7);
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            margin-bottom: 24px;
            padding: 24px;
            border: 4px solid #ffffff;
            box-shadow: inset 0 0 0 3px rgba(255,255,255,0.8);
        }

        .scene-image-text {
            font-size: 42px;
            font-weight: 900;
            color: #443333;
            line-height: 1.1;
        }

        .scene-title {
            font-size: 44px;
            font-weight: 900;
            color: #302323;
            text-align: center;
            line-height: 1.08;
            margin-bottom: 16px;
        }

        .scene-text {
            font-size: 32px;
            font-weight: 800;
            color: #463838;
            text-align: center;
            line-height: 1.18;
            margin-bottom: 18px;
        }

        .question-text {
            font-size: 34px;
            font-weight: 900;
            color: #232323;
            text-align: center;
            margin-top: 12px;
            margin-bottom: 16px;
        }

        .feedback-good {
            background: #e8ffe8;
            border: 4px solid #8bd68b;
            color: #244624;
            border-radius: 26px;
            padding: 24px;
            font-size: 30px;
            font-weight: 900;
            text-align: center;
            line-height: 1.2;
            margin-bottom: 16px;
        }

        .feedback-learn {
            background: #fff3cf;
            border: 4px solid #ffc65c;
            color: #4c3510;
            border-radius: 26px;
            padding: 24px;
            font-size: 30px;
            font-weight: 900;
            text-align: center;
            line-height: 1.2;
            margin-bottom: 16px;
        }

        .small-note {
            font-size: 24px;
            font-weight: 800;
            color: #665555;
            text-align: center;
            line-height: 1.25;
        }

        .progress-box {
            background: #ffffff;
            border-radius: 20px;
            padding: 14px 18px;
            border: 3px solid #f0d49c;
            font-size: 22px;
            font-weight: 800;
            color: #4b3b3b;
            text-align: center;
            margin-bottom: 18px;
        }

        .badge-box {
            background: #f3f0ff;
            border: 3px solid #c6b8ff;
            border-radius: 20px;
            padding: 16px;
            font-size: 24px;
            font-weight: 900;
            text-align: center;
            color: #332a66;
            margin-bottom: 16px;
        }

        .final-card {
            background: linear-gradient(135deg, #e6e0ff, #fff4c9);
            border-radius: 32px;
            padding: 34px;
            text-align: center;
            border: 4px solid #ffffff;
            box-shadow: 0 10px 26px rgba(0,0,0,0.10);
        }

        .final-title {
            font-size: 54px;
            font-weight: 900;
            color: #2d2340;
            line-height: 1.05;
            margin-bottom: 16px;
        }

        .final-text {
            font-size: 32px;
            font-weight: 850;
            color: #44344d;
            line-height: 1.25;
        }

        div.stButton > button {
            font-size: 30px;
            font-weight: 900;
            min-height: 88px;
            border-radius: 26px;
            border: 4px solid #ffffff;
            background: linear-gradient(135deg, #ffffff, #fff3d6);
            color: #2b2424;
            box-shadow: 0 6px 14px rgba(0,0,0,0.12);
            white-space: normal;
            line-height: 1.15;
        }

        div.stButton > button:hover {
            border: 4px solid #f5b84b;
            background: linear-gradient(135deg, #fff7df, #ffe5a6);
            color: #2b2424;
        }

        .stTextInput input {
            font-size: 30px;
            font-weight: 800;
            border-radius: 18px;
            min-height: 64px;
            text-align: center;
        }

        @media (max-width: 700px) {
            .game-title { font-size: 40px; }
            .game-subtitle { font-size: 22px; }
            .scene-title { font-size: 34px; }
            .scene-text { font-size: 26px; }
            .question-text { font-size: 28px; }
            .scene-image-text { font-size: 34px; }
            .feedback-good, .feedback-learn { font-size: 24px; }
            div.stButton > button { font-size: 24px; min-height: 78px; }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# Datos del juego
# -------------------------
SCENES = [
    {
        "place": "Habitacion",
        "title": "Hora de despertar",
        "visual": "Una cama calientita y un nuevo dia",
        "text": "{name} abre los ojos. Todavia tiene sueno.",
        "question": "Que puede hacer?",
        "choices": [
            {
                "label": "Levantarme poquito a poquito",
                "good": True,
                "badge": "Rutina",
                "feedback": "Muy bien, {name}. Empezar con calma ayuda a tener un buen dia.",
                "suggestion": "",
            },
            {
                "label": "Taparme y no salir",
                "good": False,
                "badge": "Calma",
                "feedback": "A veces da sueno. Esta bien sentirlo.",
                "suggestion": "Mejor puedes levantarte despacito y pedir un abrazo.",
            },
            {
                "label": "Llorar porque no quiero levantarme",
                "good": False,
                "badge": "Palabras",
                "feedback": "Llorar puede pasar cuando algo cuesta.",
                "suggestion": "Mejor puedes decir: tengo sueno, ayudame por favor.",
            },
        ],
    },
    {
        "place": "Bano",
        "title": "Dientes limpios",
        "visual": "Cepillo, pasta y una sonrisa grande",
        "text": "Es momento de lavar los dientes.",
        "question": "Que elige {name}?",
        "choices": [
            {
                "label": "Cepillar mis dientes",
                "good": True,
                "badge": "Cuidado",
                "feedback": "Muy bien. Tus dientes quedan limpios y felices.",
                "suggestion": "",
            },
            {
                "label": "No quiero",
                "good": False,
                "badge": "Rutina",
                "feedback": "A veces no dan ganas.",
                "suggestion": "Mejor puedes intentarlo poquito a poquito. Tu boca necesita cuidado.",
            },
            {
                "label": "Pedir ayuda",
                "good": True,
                "badge": "Ayuda",
                "feedback": "Muy bien. Pedir ayuda tambien es una buena decision.",
                "suggestion": "",
            },
        ],
    },
    {
        "place": "Cocina",
        "title": "Desayuno",
        "visual": "Mesa, desayuno y familia cerca",
        "text": "Hay desayuno en la mesa. {name} quiere jugar, pero tambien necesita comer.",
        "question": "Que hace {name}?",
        "choices": [
            {
                "label": "Comer un poco",
                "good": True,
                "badge": "Cuidado",
                "feedback": "Muy bien. Comer ayuda a tener energia para jugar y aprender.",
                "suggestion": "",
            },
            {
                "label": "Salir corriendo a jugar",
                "good": False,
                "badge": "Rutina",
                "feedback": "Jugar es divertido.",
                "suggestion": "Mejor come un poco primero. Asi tu cuerpo tiene fuerza.",
            },
            {
                "label": "Decir no me gusta",
                "good": False,
                "badge": "Palabras",
                "feedback": "Puede haber comida que no se antoja.",
                "suggestion": "Mejor puedes decir: puedo probar poquito o comer otra cosa sana?",
            },
        ],
    },
    {
        "place": "Entrada de la escuela",
        "title": "Despedida",
        "visual": "La escuela, una mochila y un abrazo",
        "text": "Papa o mama deja a {name} en la escuela.",
        "question": "Como se despide?",
        "choices": [
            {
                "label": "Dar abrazo y decir adios",
                "good": True,
                "badge": "Carino",
                "feedback": "Que bonito. Un abrazo ayuda a empezar el dia con amor.",
                "suggestion": "",
            },
            {
                "label": "No soltar a mama o papa",
                "good": False,
                "badge": "Valentia",
                "feedback": "A veces separarse cuesta.",
                "suggestion": "Mejor puedes dar un abrazo fuerte y recordar: vuelven por mi despues.",
            },
            {
                "label": "Entrar triste sin decir nada",
                "good": False,
                "badge": "Palabras",
                "feedback": "Sentirse triste esta bien.",
                "suggestion": "Mejor puedes decir: te voy a extranar, nos vemos al rato.",
            },
        ],
    },
    {
        "place": "Salon",
        "title": "En clase",
        "visual": "Mesa, colores y una maestra sonriendo",
        "text": "La maestra pregunta algo. {name} no esta seguro de la respuesta.",
        "question": "Que puede hacer?",
        "choices": [
            {
                "label": "Intentar responder",
                "good": True,
                "badge": "Valentia",
                "feedback": "Muy bien. Intentar es valiente, aunque la respuesta no sea perfecta.",
                "suggestion": "",
            },
            {
                "label": "Quedarme callado todo el dia",
                "good": False,
                "badge": "Valentia",
                "feedback": "Da pena equivocarse a veces.",
                "suggestion": "Mejor puedes intentar o pedir ayuda. Aprender toma practica.",
            },
            {
                "label": "Pedir ayuda a la maestra",
                "good": True,
                "badge": "Ayuda",
                "feedback": "Muy bien. Pedir ayuda tambien es aprender.",
                "suggestion": "",
            },
        ],
    },
    {
        "place": "Recreo",
        "title": "No me deja pasar",
        "visual": "Juegos del parque y un camino bloqueado",
        "text": "Un nino se pone enfrente y no deja pasar a {name}.",
        "question": "Que hace {name}?",
        "choices": [
            {
                "label": "Decir quiero pasar, por favor",
                "good": True,
                "badge": "Palabras",
                "feedback": "Excelente. Usaste tus palabras con calma.",
                "suggestion": "",
            },
            {
                "label": "Empujar para pasar",
                "good": False,
                "badge": "Calma",
                "feedback": "Empujar puede lastimar.",
                "suggestion": "Mejor usa tu voz: quiero pasar, por favor. Si no funciona, pide ayuda.",
            },
            {
                "label": "Buscar a la maestra",
                "good": True,
                "badge": "Ayuda",
                "feedback": "Muy bien. Si alguien no respeta tu espacio, pedir ayuda es seguro.",
                "suggestion": "",
            },
        ],
    },
    {
        "place": "Recreo",
        "title": "Eso dolio",
        "visual": "Un momento dificil y una decision importante",
        "text": "Un nino muerde o golpea a {name}. Eso duele.",
        "question": "Que debe hacer?",
        "choices": [
            {
                "label": "Alejarme y decir no me pegues",
                "good": True,
                "badge": "Valentia",
                "feedback": "Muy bien. Tu cuerpo merece respeto.",
                "suggestion": "",
            },
            {
                "label": "Pegar tambien",
                "good": False,
                "badge": "Calma",
                "feedback": "Pegar tambien puede lastimar mas.",
                "suggestion": "Mejor alejate, usa voz fuerte y pide ayuda a un adulto.",
            },
            {
                "label": "Avisar a un adulto",
                "good": True,
                "badge": "Ayuda",
                "feedback": "Muy bien. Cuando alguien te lastima, un adulto debe saberlo.",
                "suggestion": "",
            },
        ],
    },
    {
        "place": "Salida de la escuela",
        "title": "Regreso a casa",
        "visual": "Mochila, camino a casa y descanso",
        "text": "Termina la escuela. {name} ve a mama o papa llegar.",
        "question": "Que puede hacer?",
        "choices": [
            {
                "label": "Contar como me fue",
                "good": True,
                "badge": "Palabras",
                "feedback": "Muy bien. Contar tu dia ayuda a que tu familia te entienda.",
                "suggestion": "",
            },
            {
                "label": "No decir nada si paso algo feo",
                "good": False,
                "badge": "Ayuda",
                "feedback": "A veces cuesta contar algo triste.",
                "suggestion": "Mejor puedes decir: necesito contarte algo. Los adultos te pueden cuidar.",
            },
            {
                "label": "Pedir un abrazo",
                "good": True,
                "badge": "Carino",
                "feedback": "Muy bien. Un abrazo tambien ayuda cuando el dia fue largo.",
                "suggestion": "",
            },
        ],
    },
    {
        "place": "Casa",
        "title": "Juguete compartido",
        "visual": "Juguetes en el piso y dos ninos jugando",
        "text": "Un hermano o hermana toma el juguete que {name} estaba usando.",
        "question": "Que hace {name}?",
        "choices": [
            {
                "label": "Decir lo estaba usando",
                "good": True,
                "badge": "Palabras",
                "feedback": "Muy bien. Dijiste lo que paso sin lastimar.",
                "suggestion": "",
            },
            {
                "label": "Arrebatarlo fuerte",
                "good": False,
                "badge": "Calma",
                "feedback": "Arrebatar puede empezar una pelea.",
                "suggestion": "Mejor di: lo estoy usando, te lo presto cuando termine.",
            },
            {
                "label": "Pedir ayuda si no escucha",
                "good": True,
                "badge": "Ayuda",
                "feedback": "Muy bien. Pedir ayuda es buena idea cuando no te escuchan.",
                "suggestion": "",
            },
        ],
    },
    {
        "place": "Casa",
        "title": "Mama pide ordenar",
        "visual": "Caja de juguetes y un cuarto mas limpio",
        "text": "Mama pide guardar los juguetes.",
        "question": "Que puede hacer {name}?",
        "choices": [
            {
                "label": "Guardar poquito a poquito",
                "good": True,
                "badge": "Rutina",
                "feedback": "Muy bien. Ordenar poquito a poquito hace que sea mas facil.",
                "suggestion": "",
            },
            {
                "label": "Gritar no quiero",
                "good": False,
                "badge": "Calma",
                "feedback": "A veces ordenar no se siente divertido.",
                "suggestion": "Mejor puedes decir: me ayudas a empezar?",
            },
            {
                "label": "Pedir cinco minutos",
                "good": True,
                "badge": "Palabras",
                "feedback": "Buena idea. Pediste tiempo con palabras.",
                "suggestion": "",
            },
        ],
    },
    {
        "place": "Casa",
        "title": "Papa llega cansado",
        "visual": "La puerta se abre y papa llega a casa",
        "text": "Papa llega cansado. {name} quiere jugar con el.",
        "question": "Que puede decir?",
        "choices": [
            {
                "label": "Jugamos cuando descanses?",
                "good": True,
                "badge": "Carino",
                "feedback": "Muy bien. Pediste jugar con paciencia y carino.",
                "suggestion": "",
            },
            {
                "label": "Enojarme si no juega ya",
                "good": False,
                "badge": "Calma",
                "feedback": "Querer jugar con papa es normal.",
                "suggestion": "Mejor puedes decir: quiero jugar contigo cuando puedas.",
            },
            {
                "label": "Irme triste sin hablar",
                "good": False,
                "badge": "Palabras",
                "feedback": "A veces guardarse lo que sientes te pone mas triste.",
                "suggestion": "Mejor di: papa, quiero estar contigo.",
            },
        ],
    },
    {
        "place": "Noche",
        "title": "Hora de dormir",
        "visual": "Pijama, luna y cama tranquila",
        "text": "Ya es de noche. El cuerpo de {name} necesita descansar.",
        "question": "Que hace {name}?",
        "choices": [
            {
                "label": "Ponerme pijama y descansar",
                "good": True,
                "badge": "Rutina",
                "feedback": "Muy bien. Dormir ayuda a crecer y tener energia manana.",
                "suggestion": "",
            },
            {
                "label": "Seguir jugando mucho mas",
                "good": False,
                "badge": "Rutina",
                "feedback": "Jugar es divertido, pero el cuerpo se cansa.",
                "suggestion": "Mejor guarda el juego y descansa para manana.",
            },
            {
                "label": "Pedir cuento o abrazo",
                "good": True,
                "badge": "Carino",
                "feedback": "Muy bien. Un cuento o abrazo ayuda a dormir con calma.",
                "suggestion": "",
            },
        ],
    },
]

BADGE_DESCRIPTIONS = {
    "Rutina": "Hacer una parte del dia con calma.",
    "Cuidado": "Cuidar el cuerpo.",
    "Carino": "Dar o pedir amor de forma bonita.",
    "Calma": "No lastimar cuando hay enojo.",
    "Palabras": "Decir lo que siento o necesito.",
    "Valentia": "Hacer algo aunque cueste.",
    "Ayuda": "Buscar a un adulto cuando hace falta.",
}

# -------------------------
# Estado inicial
# -------------------------
def init_state():
    defaults = {
        "started": False,
        "gender": None,
        "child_name": "",
        "scene_index": 0,
        "selected_choice": None,
        "badges": [],
        "history": [],
        "finished": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_game():
    for key in [
        "started",
        "gender",
        "child_name",
        "scene_index",
        "selected_choice",
        "badges",
        "history",
        "finished",
    ]:
        if key in st.session_state:
            del st.session_state[key]
    init_state()
    st.rerun()


init_state()

# -------------------------
# Helpers visuales
# -------------------------
def render_header():
    st.markdown(
        """
        <div class="title-box">
            <div class="game-title">Un Dia Valiente</div>
            <div class="game-subtitle">Un cuento para practicar buenas decisiones</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def clean_name():
    name = st.session_state.child_name.strip()
    return name if name else "Tu peque"


def format_text(text):
    return text.format(name=clean_name())


def add_badge(badge):
    if badge:
        st.session_state.badges.append(badge)


def render_badges():
    if not st.session_state.badges:
        return
    unique_badges = []
    for badge in st.session_state.badges:
        if badge not in unique_badges:
            unique_badges.append(badge)

    badge_text = " | ".join(unique_badges)
    st.markdown(
        f"<div class='badge-box'>Aprendizajes de hoy: {badge_text}</div>",
        unsafe_allow_html=True,
    )


def render_progress():
    total = len(SCENES)
    current = min(st.session_state.scene_index + 1, total)
    st.markdown(
        f"<div class='progress-box'>Parte {current} de {total}</div>",
        unsafe_allow_html=True,
    )
    st.progress(current / total)


# -------------------------
# Pantalla de inicio
# -------------------------
def start_screen():
    render_header()

    st.markdown(
        """
        <div class="scene-card">
            <div class="scene-image">
                <div class="scene-image-text">Elige tu personaje</div>
            </div>
            <div class="scene-title">Quien juega hoy?</div>
            <div class="scene-text">Selecciona una opcion y escribe su nombre.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Nina", use_container_width=True):
            st.session_state.gender = "nina"
    with col2:
        if st.button("Nino", use_container_width=True):
            st.session_state.gender = "nino"

    st.session_state.child_name = st.text_input(
        "Nombre",
        value=st.session_state.child_name,
        placeholder="Escribe el nombre aqui",
        label_visibility="collapsed",
    )

    selected_label = ""
    if st.session_state.gender == "nina":
        selected_label = "Personaje seleccionado: Nina"
    elif st.session_state.gender == "nino":
        selected_label = "Personaje seleccionado: Nino"

    if selected_label:
        st.markdown(
            f"<div class='small-note'>{selected_label}</div>",
            unsafe_allow_html=True,
        )

    ready = bool(st.session_state.gender) and bool(st.session_state.child_name.strip())
    if st.button("Empezar mi dia", use_container_width=True, disabled=not ready):
        st.session_state.started = True
        st.rerun()

    st.markdown(
        "<div class='small-note'>V1 sin imagenes reales. Los cuadros visuales se pueden reemplazar despues por ilustraciones.</div>",
        unsafe_allow_html=True,
    )


# -------------------------
# Pantalla de escena
# -------------------------
def scene_screen():
    render_header()
    render_progress()
    render_badges()

    scene = SCENES[st.session_state.scene_index]

    st.markdown(
        f"""
        <div class="scene-card">
            <div class="scene-image">
                <div class="scene-image-text">{scene['visual']}</div>
            </div>
            <div class="scene-title">{scene['title']}</div>
            <div class="scene-text">{format_text(scene['text'])}</div>
            <div class="question-text">{format_text(scene['question'])}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.session_state.selected_choice is None:
        for index, choice in enumerate(scene["choices"]):
            if st.button(choice["label"], use_container_width=True, key=f"choice_{st.session_state.scene_index}_{index}"):
                st.session_state.selected_choice = index
                add_badge(choice["badge"])
                st.session_state.history.append(
                    {
                        "scene": scene["title"],
                        "choice": choice["label"],
                        "good": choice["good"],
                        "badge": choice["badge"],
                    }
                )
                st.rerun()
    else:
        choice = scene["choices"][st.session_state.selected_choice]
        feedback_class = "feedback-good" if choice["good"] else "feedback-learn"
        feedback = format_text(choice["feedback"])
        suggestion = format_text(choice["suggestion"])

        message = feedback
        if suggestion:
            message = f"{feedback}<br><br>{suggestion}"

        st.markdown(
            f"<div class='{feedback_class}'>{message}</div>",
            unsafe_allow_html=True,
        )

        badge = choice.get("badge")
        if badge:
            explanation = BADGE_DESCRIPTIONS.get(badge, "")
            st.markdown(
                f"<div class='small-note'>Aprendizaje: {badge}. {explanation}</div>",
                unsafe_allow_html=True,
            )

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Probar otra opcion", use_container_width=True):
                st.session_state.selected_choice = None
                st.rerun()
        with col2:
            if st.button("Siguiente", use_container_width=True):
                st.session_state.selected_choice = None
                if st.session_state.scene_index >= len(SCENES) - 1:
                    st.session_state.finished = True
                else:
                    st.session_state.scene_index += 1
                st.rerun()


# -------------------------
# Pantalla final
# -------------------------
def final_screen():
    render_header()

    name = clean_name()
    unique_badges = []
    for badge in st.session_state.badges:
        if badge not in unique_badges:
            unique_badges.append(badge)

    if unique_badges:
        badge_summary = ", ".join(unique_badges)
    else:
        badge_summary = "buenas decisiones"

    good_choices = sum(1 for item in st.session_state.history if item["good"])
    total_choices = len(st.session_state.history)

    st.markdown(
        f"""
        <div class="final-card">
            <div class="scene-image">
                <div class="scene-image-text">Noche tranquila y un dia terminado</div>
            </div>
            <div class="final-title">Felicidades, {name}</div>
            <div class="final-text">
                Llegaste al final del dia.<br><br>
                Hoy practicaste: <b>{badge_summary}</b>.<br><br>
                Tomaste {total_choices} decisiones y aprendiste en cada una.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Resumen para mama o papa")
    st.write(f"Decisiones ideales elegidas: {good_choices} de {total_choices}")

    if st.session_state.history:
        with st.expander("Ver camino del dia"):
            for idx, item in enumerate(st.session_state.history, start=1):
                result = "Decision ideal" if item["good"] else "Decision para practicar"
                st.write(f"{idx}. {item['scene']} - {item['choice']} - {result}")

    if st.button("Jugar otra vez", use_container_width=True):
        reset_game()


# -------------------------
# Router principal
# -------------------------
if not st.session_state.started:
    start_screen()
elif st.session_state.finished:
    final_screen()
else:
    scene_screen()
