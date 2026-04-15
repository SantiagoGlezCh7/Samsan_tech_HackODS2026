
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
- **Tarea:** Traducir datos cualitativos de informes de SEMARNAT e INEGI en métricas visuales para la sección introductoria del análisis ("El Aliento del Planeta").
- **Resultado:** Gráficas de dona que representan la proporción de biodiversidad en arrecifes de coral (25% del total marino) y el origen humano de las amenazas costeras (>70%). El código generado fue en Matplotlib; el equipo lo migró posteriormente a Plotly para homogeneizar con el resto del proyecto.
- **Decisión del equipo:** La selección de solo dos variables críticas, el cruce de fuentes y la validación de los porcentajes fueron decisiones editoriales del equipo. La IA generó la sintaxis de visualización a partir de los datos ya procesados.

### 2026-04-13 | Filtro geográfico y diseño de información
- **Tarea:** Visualizar la fuerza laboral pesquera nacional destacando la zona de impacto del derrame, usando datos de DataMéxico.
- **Resultado:** Gráfica interactiva en Plotly que resalta los estados del Golfo (Veracruz, Tabasco, Campeche, Tamaulipas) y neutraliza visualmente los estados fuera de la zona de impacto.
- **Decisión del equipo:** La acotación geográfica —excluir visualmente a Sinaloa y Guerrero a pesar de tener mayor volumen pesquero— fue una decisión editorial del equipo basada en que el análisis se centra en el Golfo, no en el ranking nacional.

### 2026-04-13 | Configuración de repositorio y despliegue automático
- **Tarea:** Configurar el flujo de publicación del proyecto: GitHub Actions para CI, GitHub Pages para el sitio público, y Quarto para renderizar los notebooks como dashboard.
- **Resultado:** Script `build_site.sh` que exporta notebooks a HTML y los embebe en un dashboard Quarto; workflow `.github/workflows/quarto-ci.yml` que automatiza el proceso en cada push a `main`.
- **Decisión del equipo:** La estructura de carpetas, la selección de qué notebooks incluir en cada pestaña del dashboard y los nombres de salida fueron definidos por el equipo.

### 2026-04-13 | Homogenización visual entre notebooks
- **Tarea:** Unificar criterios visuales entre los notebooks del equipo: paleta de colores, tipografía, librería de gráficas, numeración de secciones y hallazgos clave.
- **Resultado:** Paleta oficial ODS (amarillo `#FDB713`, guinda `#A21942`, azul `#0A97D9`), migración completa a Plotly, función `base_layout()` reutilizable, numeración `1.1, 1.2, 2.1...` y celdas de hallazgos clave con borde de color por sección.
- **Decisión del equipo:** Los colores oficiales de las ODS 7, 8 y 14, los indicadores a visualizar y la arquitectura narrativa (ecosistema → crisis pesquera → desempleo → soberanía energética) fueron definidos por el equipo.

### 2026-04-13 | Diagnóstico y corrección de visualización de gráficas
- **Tarea:** Las gráficas de Plotly no se renderizaban en el entorno local de Jupyter después de migrar desde Matplotlib.
- **Resultado:** Diagnóstico del conflicto entre el renderer `notebook_connected` (que usa ES modules incompatibles con `file://`) y la solución con `pio.renderers.default = 'notebook'`, que embebe el JS de Plotly completo (~4.8 MB) directamente en cada celda de salida, haciendo el notebook autocontenido.
- **Decisión del equipo:** El equipo evaluó las opciones de renderización (CDN, connected, embebido) y eligió el renderer embebido aceptando el mayor tamaño del archivo a cambio de garantizar visibilidad sin conexión a internet.

### 2026-04-14 | Validación de datos y unificación de código
- **Tarea:** Un borrador de la gráfica de ocupaciones usaba datos hardcodeados en lugar de leer el CSV de DataMéxico. Se necesitaba unificar el diseño visual existente con los datos reales.
- **Resultado:** Gráfica 2.1 rediseñada para leer `ocupaciones_pesca.csv` (DataMéxico 2025-Q1); gráfica 2.2 migrada a `trabajadores_pesqueros_estado.csv` con datos reales por entidad federativa.
- **Decisión del equipo:** La detección del error de datos hardcodeados y la decisión de acotar el análisis exclusivamente a la rama industrial de la pesca (excluyendo ocupaciones no relacionadas) fueron decisiones metodológicas del equipo.

### 2026-04-14 | Depuración de notebook corrupto
- **Tarea:** Un notebook quedó con JSON inválido tras una edición directa en la interfaz de GitHub, impidiendo abrirlo.
- **Resultado:** Identificación de los errores de sintaxis (caracteres de escape faltantes en celdas Markdown y comas estructurales perdidas en el JSON del notebook). El archivo fue reparado sin pérdida de contenido.
- **Decisión del equipo:** Uso puntual como herramienta de diagnóstico de JSON. El equipo validó celda por celda que el contenido recuperado era correcto antes de commitear.

### 2026-04-14 | Mapa interactivo de zonas afectadas
- **Tarea:** Crear un mapa que diferencie los sitios con chapopote que recibieron atención institucional de los que fueron atendidos solo por la comunidad, usando los datos de reportes y la ENOE.
- **Resultado:** Mapa interactivo con `px.scatter_map` sobre fondo `carto-positron`, con dos categorías de color (guinda = sin respuesta institucional, azul = atención institucional) y tamaño de punto proporcional a la severidad.
- **Decisión del equipo:** La clasificación de qué tipos de limpieza constituían "abandono institucional" fue una decisión interpretativa del equipo sobre los datos de la ENOE.

### 2026-04-14 | Corrección de interpretación y actualización de hallazgos
- **Tarea:** La gráfica 3.1 resaltaba Coatzacoalcos como municipio con mayor tasa de desempleo, pero el análisis de los datos ENOE mostraba que Minatitlán tiene la tasa más alta.
- **Resultado:** Gráfica 3.1 corregida para resaltar Minatitlán; hallazgos de la sección 3 actualizados para reflejar correctamente la interpretación de los datos y el contexto petroquímico de ese municipio.
- **Decisión del equipo:** La detección del error de interpretación y la validación contra los datos ENOE fueron realizadas por el equipo. La IA ejecutó la corrección técnica.

---

## Lo que deliberadamente NO delegamos a la IA
- **Selección de indicadores:** Qué medir y por qué (empleo crítico, potencial eólico, concentración en el Golfo) provino de discusiones del equipo y revisión de literatura.
- **Validación del universo de datos:** Acotar el análisis a la rama industrial de la pesca fue una decisión metodológica propia, no una sugerencia de la IA.
- **Arquitectura narrativa:** El orden expositivo (ecosistema → crisis pesquera → desempleo → soberanía energética) fue estructurado por el equipo para generar empatía progresiva antes de la propuesta de solución.
- **Criterios geográficos:** Todas las decisiones sobre qué estados o municipios incluir o resaltar partieron del conocimiento del equipo sobre la zona de impacto real del derrame.
