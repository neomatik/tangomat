# 🧠 Sistema Narrativo Multiagente con CrewAI

Este proyecto es una infraestructura modular para desarrollar novelas mediante agentes IA colaborativos. Está construido sobre **CrewAI** y diseñado específicamente para narrativa compleja, estilo neo-noir, y control creativo por parte del autor.

---

## 📁 Estructura del proyecto

```
novela_crewai/
├── agents/                # Agentes IA especializados
├── prompts/               # Prompts personalizados por agente
├── story/                 # Capítulos, resúmenes y estado global
│   ├── chapters/
│   ├── summaries/
│   ├── global_state.json
│   └── characters.json
├── workflows/             # Flujo narrativo por capítulo
├── utils/                 # Guardado, consolidación, carga de contexto
├── scripts/               # Entrada desde terminal (consolidación, etc.)
├── context_manager/       # (Futuro) Control avanzado de memoria narrativa
├── config.yaml            # Modelos y parámetros por agente
├── requirements.txt
└── README.md
```

---

## 🚀 Cómo ejecutar

### 1. Activar entorno virtual

```bash
source venv/bin/activate
```

### 2. Ejecutar generación de secciones (loop Estilista)

```bash
python loops/loop_estilista.py
```

### 3. Consolidar capítulo desde terminal

```bash
python scripts/consolidar.py 2
```

Esto creará `capitulo_completo.md` dentro de `story/chapters/cap_02/`.

---

## 🔧 Componentes clave

### Agentes disponibles

- `Arquitecto`: diseña capítulos y estructura narrativa
- `Estilista`: redacta secciones literarias (~1500 palabras)
- `Personajes`: evalúa evolución psicológica
- `Diálogo`: refina naturalidad verbal
- `Coherencia`: asegura continuidad lógica
- `Temático`: detecta símbolos y dilemas filosóficos
- `Científico`: valida plausibilidad técnica
- `Supervisor`: coordina revisión global

### Flujos

- `flujo_capitulo.py`: ejecuta todas las tareas narrativas, en orden optimizado

### Utilidades

- `guardar_seccion()`: guarda una sección automáticamente
- `consolidar_capitulo()`: une todas las secciones en un solo `.md`
- `scripts/consolidar.py`: ejecutable desde terminal

---

## 🧠 Filosofía del sistema

Este proyecto prioriza:

- **Control autoral**: tú decides cuándo reescribir, aprobar o ramificar
- **Modularidad**: puedes ejecutar agentes por separado
- **Escalabilidad**: sistema listo para expandirse con LangGraph, memoria semántica o nuevos agentes

---

## ✅ Requisitos previos

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Requiere tener definida la variable de entorno con tu clave de OpenAI:

```bash
export OPENAI_API_KEY=tu_clave_aqui
```

---

## 🧩 Futuras mejoras (ya previstas)

- Generación automática de resúmenes
- Control de estado narrativo por sección
- Bifurcaciones narrativas con LangGraph
- Exportación para maquetación o publicación

---

Este sistema ha sido diseñado a medida para narrativa compleja. Disfrútalo, modifícalo, y siéntete en control.
