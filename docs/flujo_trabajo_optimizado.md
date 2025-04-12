# 🔁 Flujo de trabajo narrativo optimizado (CrewAI)

Este es el flujo definitivo para el sistema narrativo multiagente, orientado a estabilidad, escalabilidad y máxima calidad literaria.

---

## 📘 INICIO ÚNICO (1 vez por novela)

### 0. Planificación general
- Agentes: Arquitecto, Científico, Personajes, Temático, Coherencia, Diálogo
- Acción: establecer tono, universo, estilo narrativo, arcos temáticos
- Resultado: `plan_novela.json`

---

## 🔄 CICLO COMPLETO POR CAPÍTULO

### 1. Planificación del capítulo (Arquitecto)
- Acción: estructura, secciones, progresión emocional
- Resultado: `plan_cap_xx.json`

---

### 2. Redacción por bloques (Estilista)
- Acción: escribe secciones divididas en sub-bloques (~750+750 si necesario)
- Resultado: `story/chapters/cap_xx/sec_yy.md`

---

### 3. Validación rápida por Coherencia
- Acción: detecta quiebres narrativos tras cada sección
- Resultado: observaciones inmediatas antes de continuar

---

### 4. Redacción continúa hasta completar capítulo
- Acción: se repite paso 2 y 3 hasta completar todas las secciones

---

### 5. Revisión integral por agentes secundarios
- Agentes: Personajes, Diálogo, Científico, Temático, Coherencia
- Acción: cada uno evalúa el capítulo completo

---

### 6. Informe global (Supervisor)
- Acción: síntesis de observaciones de todos los agentes
- Formato sugerido:

| Sección | Personajes | Coherencia | Diálogo | Científico | Temático |
|---------|------------|------------|---------|------------|----------|
| sec_01  | ✅          | ⚠️ detalle | ✅       | ✅          | ✅        |

---

### 7. Aprobación inicial
- Agente: Supervisor o usuario
- Acción: determina si se pasa a reescritura

---

### 8. Reescritura dirigida por sección (Estilista)
- Acción: reescribe solo donde hay observaciones
- Input: `plan_reescritura.json` generado desde el informe

---

### 9. Aprobación final
- Acción: validación definitiva del capítulo (usuario o Supervisor)

---

### 10. Actualización de memoria narrativa
- Archivos:
  - `story/summaries/cap_xx.md`
  - `story/global_state.json`

---

### (11). Activación de LangGraph (opcional)
- Uso: ramificación narrativa, decisiones estructurales
- Acción: si se requiere bifurcación o historia no lineal

---

## 🧠 Nota final
Este flujo mantiene la calidad literaria, permite colaboración entre agentes IA especializados y deja el control final al autor humano.
