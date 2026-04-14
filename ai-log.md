
# Uso de Inteligencia Artificial 

--------------------------
# AI Log - Equipo SamsanTech

## Herramientas utilizadas
- Google Gemini (Asistente de Jessica)
- Claude (Asistente de Rodolfo)
- [Si alguien usó Copilot, agregarlo aquí]

## Filosofía de uso
Como equipo, decidimos utilizar la IA generativa estrictamente como un **acelerador de sintaxis (pair-programming) y maquetación visual**, no como un motor de decisiones. Nuestra regla fue: la IA puede sugerir cómo escribir el código (Matplotlib, Plotly, JSON crudo), pero el equipo dicta la narrativa, filtra los datos geográficamente e impone el rigor técnico. Si una gráfica no aportaba a nuestra historia del "Viaje del Héroe" en el Golfo de México, la salida de la IA era rechazada o reestructurada.

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
