# Golfo de México: Del Derrame a la Transición

![Imagen del derrame](/image/derrame_petroleo.png)


# Objetivo

Nuestro proyecto analiza cómo la dependencia petrolera de México expone a las
comunidades costeras del Golfo a riesgos socioambientales, tomando como eje el
derrame de marzo de 2026: más de 600 km de litoral afectados, siete áreas
naturales protegidas dañadas y decenas de miles de pescadores sin sustento.

Los ODS 7, 8 y 14 fallan al mismo tiempo cuando el modelo energético depende
del petróleo. Elegimos estas ODS porque describen tanto el problema como la
dirección para no repetirlo: energía limpia, trabajo digno y ecosistemas
protegidos. No es un caso hipotético — es la noticia de hoy.



# Objetivos de Desarrollo Sostenible propuestos:

- ODS 8   Trabajo decente y crecimiento económico
  
- ODS 14  Vida submarina(ecosistema del Golfo)
  
- ODS 7   Energía asequible y no contaminante 

   



| Nombre de la Fuente de información                                        | Enlace / Referencia                                                                                                                                                            |
| --------------------------------------------------------------------------| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Encuesta Nacional de Ocupación y Empleo (ENOE)                            | [INEGI ENOE](https://www.inegi.org.mx/programas/enoe/15ymas/)                                                                                                                  |
| Sitios afectados — Derrame de Petróleo Veracruz-Tabasco 2026              | [Google Maps](https://www.google.com/maps/d/u/0/viewer?mid=1Ku4wk-WcKmPcrna08enfELqsr5pp9LA&ll=20.841486120822935%2C-97.37267330407846&z=7)                                    |
| Noticia del derrame de petróleo                                           | [EL PAÍS](https://elpais.com/mexico/2025-10-28/la-huella-del-derrame-de-pemex-agudiza-la-emergencia-en-comunidades-de-veracruz.html)                                           |
| Imagen de portada                                                         | [PROCESO](https://www.proceso.com.mx/nacional/estados/2026/3/4/derrame-de-petroleo-se-extiende-largo-de-casi-170-kilometros-del-litoral-veracruzano-369642.html)               |
| Objetivos de Desarrollo Sostenible                                        | [CEPAL ODS](https://www.cepal.org/es/temas/agenda-2030-desarrollo-sostenible/objetivos-desarrollo-sostenible-ods)                                                              |
| Balance Nacional de Energía — SENER SIE                                   | Secretaría de Energía, Sistema de Información Energética (SIE), datos 2015-2023                                                                                                |
| Electricity Generation by Source — Our World in Data / Ember              | Ember, *Global Electricity Review*; reproducido en Our World in Data (electricity_sources.csv)                                                                                 |
| Potencial Solar — Global Solar Atlas (GSA)                                | World Bank / Solargis, *Global Solar Atlas 2.0*, datos de irradiación horizontal global, 2024                                                                                  |
| Potencial Eólico — Global Wind Atlas (GWA)                                | Technical University of Denmark (DTU), *Global Wind Atlas 3.3*, velocidad de viento a 100 m, 2024                                                                             |
| Distribución de la Población Ocupada por Ocupación 2025-Q1               | DataMéxico / STPS-INEGI, *ENOE 2025 T1 — Distribución de trabajadores pesqueros por ocupación*                                                                                |
| Trabajadores en Actividades Pesqueras por Estado 2025-Q1                  | DataMéxico / STPS-INEGI, *ENOE 2025 T1 — Población ocupada en actividades pesqueras por entidad*                                                                              |
| Unidades Económicas del Sector Minero-Petrolero por Estado                | INEGI, *Directorio Estadístico Nacional de Unidades Económicas (DENUE)*, 2014                                                                                                  |



## Elaboración del Proyecto 

- Jessica Alvarez Esquivel
- Santiago Gonzalez Chavez
- Rodolfo Enrique Rentería Ramírez

## Información del repositorio (para la rúbrica HackODS)

- **Nombre del equipo:** Samsan_tech
- **URL del repositorio:** https://github.com/SantiagoGlezCh7/Samsan_tech_HackODS2026
- **ODS elegidos:** ODS 7, ODS 8, ODS 14
- **Pregunta central:** ¿Cómo ha afectado el reciente derrame de petróleo en la costa de Veracruz-Tabasco al empleo y a las comunidades costeras, y qué zonas requieren atención prioritaria?

## Estructura del proyecto

- `datos/` : datasets usados (CSV, KML)
- `scripts/` : scripts para procesar y construir el sitio
- `dashboard/` : archivos `.qmd` del tablero (prototipo)
- `docs/` : sitio generado (carpeta usada por GitHub Pages)

## Cómo ver el dashboard (despliegue)

- Versión pública GitHub Pages: https://santiagoglezch7.github.io/Samsan_tech_HackODS2026/
- El sitio se construye con Quarto. Localmente:

```bash
# construir sitio localmente (requiere Quarto)
quarto render
# o usar el script
./scripts/build_site.sh
```

- En GitHub se ejecuta la acción `.github/workflows/quarto-ci.yml` que genera la carpeta `docs/` y la commitea a `main`. Asegúrate en la configuración del repositorio (Settings → Pages) que la fuente de Pages esté en `main` / `docs`.

## Declaración de uso de IA

- Archivo con registro de uso de IA: `ai-log.md` (registro de prompts y resultados). Si se requiere la plantilla oficial, indíquenmelo y la adapto aquí.

## Metadatos de los datos

- Ver `DATASETS.md` para descripción, fuente, fecha de descarga y licencias de cada dataset.

## Licencia

- Este repositorio incluye un archivo `LICENSE` (CC BY-SA). Ver `LICENSE`.

## Checklist de cumplimiento (rúbrica HackODS)

El siguiente checklist mapea los ítems de la rúbrica al estado actual del repositorio. Marca "Sí" si el ítem está presente/implementado.

| Ítem | Requisito | Estado | Evidencia |
|---|---:|---|---|
| A1 | Licencia CC BY-SA | Sí | `LICENSE` presente |
| A2 | README completo (equipo, integrantes, ODS, descripción) | Parcial → Mejorado | Esta sección añadida arriba |
| A3 | Metadatos de los datos (fuente, fecha, licencia, variables) | Parcial | `DATASETS.md` añadido (completa/ajustar fechas si es necesario) |
| A4 | Estructura de carpetas (`datos/`, `scripts/`, `dashboard/`) | Sí | Carpetas existentes |
| A5 | Declaratoria de uso de IA (plantilla oficial) | Parcial | `ai-log.md` presente; si se requiere plantilla oficial, la añado |
| D0 | Existencia de `.qmd` o `.ipynb` | Sí | `dashboard/index.qmd` existe |
| D1 | Visualizaciones | Sí | Visualizaciones en `dashboard` y `docs/` generadas |
| D2 | Estructura del tablero | Sí | `dashboard/index.qmd` y `docs/` con layout de Quarto Dashboard |

Si quieres, puedo completar las fechas de descarga y las licencias exactas en `DATASETS.md`, y/o crear el archivo de Declaratoria de IA con la plantilla oficial.



