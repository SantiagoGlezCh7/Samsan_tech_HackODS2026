
# Uso de Inteligencia Artificial 

--------------------------
# AI Log - Equipo SamsanTech

## Herramientas utilizadas
- Google Gemini (Asistente de Jessica)
- Claude (Asistente de Rodolfo)

## Filosofía de uso
Como equipo, decidimos utilizar la IA generativa estrictamente como un **acelerador de sintaxis (pair-programming) y maquetación visual**, no como un motor de decisiones. Nuestra regla fue: la IA puede sugerir cómo escribir el código (Matplotlib, Plotly, JSON crudo), pero el equipo dicta la narrativa, filtra los datos geográficamente e impone el rigor técnico. Si una gráfica no aportaba a nuestra historia del "Viaje del Héroe" en el Golfo de México, la salida de la IA era rechazada o reestructurada.

---

## Registro de uso (Sección Rodolfo - Claude Code)

### 2026-04-13 | Claude Code | Configuración de Repositorio y GitHub Pages
- **Tarea:** Configurar el repositorio de GitHub para despliegue automático con GitHub Actions y GitHub Pages, incluyendo el flujo de CI/CD con Quarto.
- **Prompt:** "como hago para que el repositorio se vea en github pages y que se actualice solo cada que hacemos push"
- **Resultado:** Script `build_site.sh`, archivo `.github/workflows/quarto-ci.yml` para CI automático y configuración de Pages sobre la carpeta `docs/`.
- **Decisión y Modificaciones:** El equipo decidió usar `docs/` en lugar de una rama `gh-pages` separada para mantener todo el historial en `main` y simplificar las revisiones. La lógica de qué notebooks exportar (y con qué nombre) fue definida por el equipo.

### 2026-04-13 | Claude Code | Homogenización Visual de Notebooks
- **Tarea:** Unificar diseño visual entre `storytelling.ipynb`, `03_desempleo.ipynb` e `04_infraestructura.ipynb`: paleta ODS, librería Plotly, numeración de gráficas y hallazgos clave.
- **Prompt:** "necesito que haya mayor homogenizacion entre las graficas de todos, tipos de letras, usa los colores de las ods (amarillo, guinda y azul), numeracion, que sean con plotly, la grafica de distribucion de trabajadores pesqueros por estado se traslapa redimensionar, y la de crecimiento solar y eolica en mexico creo que falta poner el label de que es lo verde"
- **Resultado:** Paleta `ODS_Y=#FDB713`, `ODS_G=#A21942`, `ODS_B=#0A97D9`; función `base_layout()` compartida; conversión de todas las gráficas a Plotly; numeración `1.1, 1.2, 2.1...`; labels explícitos en gráfica solar/eólica; donut chart para distribución pesquera sin solapamiento.
- **Decisión y Modificaciones:** La selección de los tres colores ODS y la decisión de qué elementos merecían hallazgos clave fueron del equipo. La IA propuso una paleta genérica inicialmente; el equipo la reemplazó con los colores oficiales de las ODS 7, 8 y 14.

### 2026-04-13 | Claude Code | Diagnóstico y Corrección del Renderer de Plotly
- **Tarea:** Resolver que las gráficas de Plotly no se veían en Jupyter Notebook después de migrar de Matplotlib.
- **Prompt:** "no se ven las graficas... ok ahorita tengo todo en el repositorio, que tengo que hacer para que se vean las graficas con plotly"
- **Resultado:** Identificación de que `notebook_connected` usa `<script type='module'>` (falla sobre `file://`); solución con `pio.renderers.default = 'notebook'` que embebe Plotly.js completo (~4.8 MB) como salida `text/html`, haciendo el notebook autocontenido.
- **Decisión y Modificaciones:** El equipo aceptó el tamaño mayor del archivo (5 MB vs 40 KB) a cambio de visualización garantizada en cualquier entorno Jupyter sin conexión a internet. La exploración de renderers alternativos fue iterativa; el equipo validó cada opción antes de decidir.

### 2026-04-14 | Claude Code | Integración de Datos Reales y Corrección de Interpretación
- **Tarea:** Reemplazar datos hardcodeados en la gráfica 2.1 con datos reales de DataMéxico; corregir la interpretación errónea de la gráfica 3.1 (Minatitlán es el municipio con mayor desempleo, no Coatzacoalcos).
- **Prompt:** "en la grafica 2.1 'fuerza laboral por ocupacion' se grafico mal usa los datos del csv 'Distribucion-poblacion-Trabajadores'. en la grafica 3.1 de tasa de empleo creo que la interpretacion esta mal minatitlan es la que tiene la mayor tasa de empleo, cambiar lo correspondiente y los hallazgos claves"
- **Resultado:** Sección 2.1 rediseñada para leer `ocupaciones_pesca.csv` (DataMéxico 2025-Q1) con ocupaciones reales; sección 2.2 migrada a `trabajadores_pesqueros_estado.csv` con datos reales por estado; sección 3.1 corregida para resaltar Minatitlán; hallazgos actualizados con números reales.
- **Decisión y Modificaciones:** La detección del error de interpretación (Minatitlán vs Coatzacoalcos) fue 100% del equipo. La IA ejecutó la corrección técnica, pero la validación de cuál municipio tiene la mayor tasa de desempleo provino del conocimiento del equipo sobre los datos ENOE.

---

## Registro de uso (Sección Jessica - Gemini)

### 2026-04-12 | Gemini | Síntesis Visual de Fuentes Documentales (Sin CSV)
- **Tarea:** Transformar literatura científica en formato texto (informes de SEMARNAT, INEGI y Wharton) en métricas visuales de alto impacto para la introducción del tablero ("El Aliento del Planeta").
- **Prompt:** "Quisiera iniciar el storytelling presentando datos sobre la importancia del mar... encontre datos acerca de esto, pero estan escritos, no se como pasarlos a algo grafico... [Pegué fragmentos de texto del Programa Nacional de Restauración Ambiental 2025 y valoraciones del SAM]."
- **Resultado:** Código en Matplotlib para generar gráficas de dona enfocadas en extraer los porcentajes clave mencionados en los textos.
- **Decisión y Modificaciones:** La IA propuso varias formas de mostrar la información, pero el equipo tomó la decisión editorial de aislar solo dos variables críticas: el 25% (biodiversidad en arrecifes) y el >70% (amenaza por actividad humana). La extracción de variables, el cruce de fuentes y la validación de la información fueron procesos 100% humanos; la IA funcionó únicamente como puente para generar la sintaxis de las gráficas de dona que no provenían de un CSV estructurado.

### 2026-04-13 | Gemini | Filtro Geográfico y Diseño de Información (CSV)
- **Tarea:** Generar código en Python para visualizar la fuerza laboral pesquera nacional, pero focalizando la atención visual en la zona de impacto del derrame.
- **Prompt:** "Como corrijo todo el codigo para que resalte solo 3 estados como nos dice la fuente. En la segunda celda que solo resalte veracruz, ya que sinaloa y guerrero no pertenecen a la zona del golfo de mexico."
- **Resultado:** Código para una gráfica de pastel interactiva utilizando listas de comprensión y la función `explode` para separar las variables de interés.
- **Decisión y Modificaciones:** Rechazamos la sugerencia inicial de la IA de resaltar visualmente a todos los estados líderes en pesca del país. El equipo intervino con conocimiento de contexto geográfico: forzamos a la IA a "apagar" (pintar de gris) a Sinaloa y Guerrero, a pesar de su volumen de pesca, porque la crisis analizada (derrame) está en el Golfo. Además, calibramos manualmente las coordenadas de las cajas de texto (x=0.9, y=0.9) para adaptarlas al layout de nuestro tablero en Quarto.

### 2026-04-14 | Gemini | Validación de Datos y Auditoría de Código
- **Tarea:** Unificar el diseño de la gráfica interactiva de Ocupaciones (Plotly) de un compañero con los datos reales de la Secretaría de Economía (DataMéxico).
- **Prompt:** "Hay una parte de la notebook que hizo rodolfo/santiago que no se si confundio... el codigo de mi compañero usa `ocupaciones = pd.DataFrame({'Total': [4200000, 2100000...]})`. Mi código usa `pd.read_csv('Distribucion...csv')`. Necesito unificar esto."
- **Resultado:** Un script híbrido que inyectó el *dataframe* limpio y filtrado en la estructura visual de Plotly generada previamente.
- **Decisión y Modificaciones:** Aceptado y modificado tácticamente. El equipo detectó que un borrador de diseño utilizaba *dummy data* (datos hardcodeados). En lugar de perder el diseño o presentar datos falsos, usamos a la IA para ejecutar la fusión técnica. La decisión de acotar la gráfica exclusivamente a la "rama industrial de la Pesca" provino de nuestra investigación sociodemográfica, corrigiendo la falta de contexto en el código original.

### 2026-04-14 | Gemini | Depuración Estructural (JSON Crudo)
- **Tarea:** Reparar un error fatal de corrupción de archivo (`invalid notebook`) tras editar celdas directamente en el repositorio de GitHub.
- **Prompt:** "Me arrojo que invalida notebook :c Aqui esta la parte del codigo desde la linea 208 a las 241 [captura de código JSON]."
- **Resultado:** Identificación de errores de sintaxis (falta de caracteres de escape `\"` en un Markdown y comas estructurales perdidas).
- **Decisión y Modificaciones:** Aceptación total. Se utilizó la IA como un *linter* de emergencia. La herramienta no generó conocimiento nuevo, sino que identificó un error tipográfico humano en el JSON masivo, permitiéndonos salvar el control de versiones sin perder el hilo narrativo del ODS 8.

---

### Lo que deliberadamente NO delegamos a la IA:
- **La selección de indicadores:** Qué medir y por qué (empleo crítico, potencial eólico, concentración en el Golfo) provino de discusiones del equipo y literatura.
- **Validación del Universo de Datos:** Acotar que la pérdida laboral aplicaba a la "rama industrial de la Pesca" y no al promedio general estatal fue una aclaración metodológica propia.
- **Arquitectura Narrativa:** El orden expositivo (1. El Aliento del Planeta -> 2. La crisis pesquera -> 3. El desempleo -> 4. Soberanía energética) fue estructurado 100% por nosotros para generar empatía progresiva antes de revelar la propuesta de solución.


- Tarea:

 Un mapa interactivo de las zonas afectadas por atencion institucional y sin atencion con los dtos de la ENOE y el mapa de de los sitios afectados, replicar el mapa.

- Promt: 

"Objetivo: Representar visualmente una serie histórica de eventos de derrames de petróleo a lo largo de la costa del Golfo de México, utilizando principios de storytelling de datos para maximizar el impacto visual y la participación de la audiencia. Se implementará una visualización exploradora spatiotemporal.

Datos: El widget se inicializa con datos sobre derrames históricos. Estos datos incluyen ubicaciones (lat/lon aproximadas), fechas, volumen del derrame (gravedad) y tipo de hidrocarburo.

Entradas: 1. Slider de Tiempo para controlar la animación temporal. 2. Filtro de Tipo de Incidente. 3. Toggle de Impacto Ambiental.

Comportamiento: Crea una proyección de mapa interactiva. La animación de los puntos se activa mediante el slider de tiempo. Las propiedades visuales de los puntos (tamaño y color) representan directamente la gravedad del derrame. Utiliza colores de alto contraste, con gradientes intensos para las áreas de mayor severidad (Rojo Alerta vs Gris Contexto)."                

- Resultado:

El mapa interactivo de las zonas de afectacion atentidas por instituciones y las que aun no son atendidas por comunidades e instituciones   

- Modificaciones del equipo : 

No se relizo modificacion  
 
------------------
