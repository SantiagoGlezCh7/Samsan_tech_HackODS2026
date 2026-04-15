
# Uso de Inteligencia Artificial

# AI Log - Equipo SamsanTech

## Herramientas utilizadas
- Google Gemini
- Claude

## Filosofía de uso
Como equipo, utilizamos la IA generativa como un **acelerador de sintaxis y maquetación visual**, no como un motor de decisiones. La IA sugiere cómo escribir el código, pero el equipo dicta la narrativa, filtra los datos geográficamente e impone el rigor técnico. Si una gráfica no aportaba a nuestra historia en el Golfo de México, la salida de la IA era rechazada o reestructurada.

---

## Registro de uso

### 2026-04-12 | Síntesis visual de fuentes documentales
- **Tarea:** Traducir datos cualitativos de literatura científica (SEMARNAT, INEGI) en métricas visuales para la introducción del análisis.
- **Resultado:** Gráficas de dona para representar biodiversidad en arrecifes (25%) y amenazas de origen humano (>70%).
- **Decisión del equipo:** La selección de las dos variables críticas, el cruce de fuentes y la validación fueron procesos del equipo; la IA generó la sintaxis de visualización.

### 2026-04-13 | Filtro geográfico y diseño de información
- **Tarea:** Visualizar la fuerza laboral pesquera nacional resaltando la zona de impacto del derrame.
- **Resultado:** Gráfica interactiva que destaca estados del Golfo y neutraliza visualmente los estados no afectados.
- **Decisión del equipo:** La acotación geográfica (excluir Sinaloa y Guerrero a pesar de su volumen pesquero) fue una decisión editorial del equipo basada en contexto geográfico.

### 2026-04-13 | Configuración de repositorio y despliegue
- **Tarea:** Configurar GitHub Actions y GitHub Pages para publicación automática del sitio Quarto.
- **Resultado:** Script de construcción y workflow de CI que exporta los notebooks a HTML y publica en `docs/`.
- **Decisión del equipo:** La estructura de carpetas y la selección de notebooks en el dashboard fueron definidas por el equipo.

### 2026-04-13 | Homogenización visual de notebooks
- **Tarea:** Unificar paleta de colores, tipografía, librería de gráficas y estructura narrativa entre todos los notebooks.
- **Resultado:** Paleta ODS (amarillo/guinda/azul), migración a Plotly, numeración consistente y hallazgos clave por sección.
- **Decisión del equipo:** Los colores oficiales ODS, los indicadores a visualizar y la arquitectura narrativa fueron definidos por el equipo.

### 2026-04-13 | Corrección de visualización de gráficas
- **Tarea:** Resolver problema de visibilidad de gráficas Plotly en Jupyter.
- **Resultado:** Configuración del renderer para embeber Plotly directamente en el notebook, haciéndolo autocontenido.
- **Decisión del equipo:** El equipo evaluó las alternativas y eligió la que garantizaba visualización sin dependencia de internet.

### 2026-04-14 | Validación de datos y auditoría de código
- **Tarea:** Unificar diseño de gráfica de ocupaciones con datos reales de DataMéxico, reemplazando datos provisionales.
- **Resultado:** Gráfica conectada al CSV oficial; la visualización conserva el diseño original con datos reales.
- **Decisión del equipo:** La detección del error y la delimitación al sector pesquero como universo de análisis fue una decisión metodológica del equipo.

### 2026-04-14 | Depuración de notebook corrupto
- **Tarea:** Reparar error de sintaxis en JSON del notebook tras edición directa en GitHub.
- **Resultado:** Identificación y corrección de errores estructurales que impedían abrir el archivo.
- **Decisión del equipo:** Uso puntual como herramienta de diagnóstico; el equipo validó la corrección antes de aceptarla.

### 2026-04-14 | Mapa interactivo de zonas afectadas
- **Tarea:** Crear mapa de sitios con y sin atención institucional tras el derrame.
- **Resultado:** Mapa interactivo que diferencia zonas atendidas por instituciones de las atendidas solo por la comunidad.
- **Decisión del equipo:** No se realizaron modificaciones al resultado generado.

### 2026-04-14 | Integración de datos reales y corrección de interpretación
- **Tarea:** Conectar gráficas de fuerza laboral a CSVs de DataMéxico; corregir municipio con mayor tasa de desempleo.
- **Resultado:** Secciones 2.1 y 2.2 con datos reales por ocupación y estado; gráfica 3.1 corregida para señalar Minatitlán.
- **Decisión del equipo:** La detección del error de interpretación y la validación de los datos ENOE fueron realizadas por el equipo.

---

## Lo que deliberadamente NO delegamos a la IA
- **Selección de indicadores:** Qué medir y por qué provino de discusiones del equipo y revisión de literatura.
- **Validación del universo de datos:** Acotar el análisis a la rama industrial de la pesca fue una decisión metodológica propia.
- **Arquitectura narrativa:** El orden expositivo (ecosistema → crisis pesquera → desempleo → soberanía energética) fue estructurado por el equipo para generar empatía progresiva antes de la propuesta de solución.
