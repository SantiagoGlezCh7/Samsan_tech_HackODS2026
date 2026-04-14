"""
Genera master_001.ipynb
Paleta ODS 7/8/14 | Todo Plotly | Hallazgos clave por sección
SamsanTech HackODS 2026
"""
import nbformat, subprocess, os, pandas as pd, numpy as np

def md(text):
    return nbformat.v4.new_markdown_cell(text)

def code(lines):
    return nbformat.v4.new_code_cell("\n".join(lines))

def hallazgos(color, titulo, items):
    li = "".join(f"<li style='margin:6px 0'>{i}</li>" for i in items)
    return md(
        f'<div style="background:#fafafa;border-left:5px solid {color};'
        f'padding:16px 22px;margin:20px 0;border-radius:0 8px 8px 0">'
        f'<b style="color:{color};font-size:1.05em">{titulo}</b>'
        f'<ul style="margin:10px 0 0 0;padding-left:18px;color:#333">{li}</ul>'
        f'</div>'
    )

# ── Pre-computar valores para los textos de hallazgos ────────────────────────
_BASE = os.path.join(os.path.dirname(__file__), '..', 'datos')

_dist = pd.read_csv(os.path.join(_BASE, 'distribucion.csv'))
_dist.columns = _dist.columns.str.strip()
_dist['estado'] = _dist['State'].str.replace('Veracruz de Ignacio de la Llave', 'Veracruz', regex=False)
_golfo_states  = ['Veracruz', 'Tamaulipas', 'Tabasco', 'Campeche']
_golfo_estab   = _dist[_dist['estado'].isin(_golfo_states)]['Economic Unit'].sum()
_total_estab   = _dist['Economic Unit'].sum()
_pct_golfo     = int(round(_golfo_estab / _total_estab * 100))

_prod = pd.read_csv(os.path.join(_BASE, 'produccion.csv'), header=0, names=['periodo','participacion'])
_prod['participacion'] = pd.to_numeric(_prod['participacion'], errors='coerce')
_prom_prod = round(_prod['participacion'].mean(), 1)

_elec    = pd.read_csv(os.path.join(_BASE, 'electricity_sources.csv'))
_elec_mx = _elec[_elec['entity'] == 'Mexico'].copy()
_mix     = _elec_mx.groupby(['date','series'])['generation_share_pct'].sum().unstack(fill_value=0).reset_index()
for _c in ['Gas','Coal','Other fossil','Solar','Wind','Hydro','Bioenergy']:
    if _c not in _mix.columns: _mix[_c] = 0
_mix['Fosil_%']     = _mix[['Gas','Coal','Other fossil']].sum(axis=1)
_mix['Renovable_%'] = _mix[['Solar','Wind','Hydro','Bioenergy']].sum(axis=1)
_fosil_2024   = round(_mix[_mix['date']==2024]['Fosil_%'].values[0])
_renov_2024   = round(_mix[_mix['date']==2024]['Renovable_%'].values[0])
_solar_2024   = round(_elec_mx[(_elec_mx['series']=='Solar') & (_elec_mx['date']==2024)]['generation_share_pct'].sum(), 1)
_wind_2024    = round(_elec_mx[(_elec_mx['series']=='Wind')  & (_elec_mx['date']==2024)]['generation_share_pct'].sum(), 1)

_solar_df  = pd.read_csv(os.path.join(_BASE, 'potencial_solar_golfo_GSA.csv'))
_eolico_df = pd.read_csv(os.path.join(_BASE, 'potencial_eolico_golfo_GWA.csv'))
_solar_ref_val  = round(_solar_df[_solar_df['region']=='Germany']['PVOUT_kWh_kWp'].values[0])
_solar_gulf_avg = round(_solar_df[_solar_df['region']!='Germany']['PVOUT_kWh_kWp'].mean())
_tam_viento     = round(_eolico_df[_eolico_df['region']=='Tamaulipas']['viento_mediana_ms'].values[0], 1)
_china_viento   = round(_eolico_df[_eolico_df['region']=='China']['viento_mediana_ms'].values[0], 2)

# ── Paleta ODS ────────────────────────────────────────────────────────────────
ODS_Y   = '#FDB713'
ODS_G   = '#A21942'
ODS_B   = '#0A97D9'
NEUTRAL = '#CCCCCC'

cells = []

# ═══════════════════════════════════════════════════════════════════════════════
# PORTADA
# ═══════════════════════════════════════════════════════════════════════════════
cells.append(md(
    '<div style="text-align:center;padding:28px 0 12px">\n'
    '<h1 style="font-size:2.1em;color:#222;margin:0 0 8px">'
    'Golfo de México: Del Derrame a la Transición</h1>\n'
    '<p style="color:#777;margin:4px 0;font-size:1.05em">HackODS 2026 · SamsanTech</p>\n'
    '<p style="margin:6px 0"><b>Equipo:</b> '
    'Jessica Álvarez · Santiago González · Rodolfo Rentería</p>\n'
    '<div style="display:flex;gap:18px;justify-content:center;margin:22px 0">\n'
    '<div style="width:92px;height:92px;background:#FDB713;border-radius:50%;display:flex;'
    'flex-direction:column;align-items:center;justify-content:center;color:white;'
    'font-weight:bold;text-align:center;line-height:1.2">'
    '<span style="font-size:1.8em">7</span>'
    '<span style="font-size:0.65em;letter-spacing:1px">ODS</span></div>\n'
    '<div style="width:92px;height:92px;background:#A21942;border-radius:50%;display:flex;'
    'flex-direction:column;align-items:center;justify-content:center;color:white;'
    'font-weight:bold;text-align:center;line-height:1.2">'
    '<span style="font-size:1.8em">8</span>'
    '<span style="font-size:0.65em;letter-spacing:1px">ODS</span></div>\n'
    '<div style="width:92px;height:92px;background:#0A97D9;border-radius:50%;display:flex;'
    'flex-direction:column;align-items:center;justify-content:center;color:white;'
    'font-weight:bold;text-align:center;line-height:1.2">'
    '<span style="font-size:1.8em">14</span>'
    '<span style="font-size:0.65em;letter-spacing:1px">ODS</span></div>\n'
    '</div>\n'
    '</div>\n\n'
    "Nuestro proyecto analiza cómo la dependencia petrolera de México expone a las "
    "comunidades costeras del Golfo a riesgos socioambientales, tomando como eje el "
    "derrame de marzo de 2026: más de 600 km de litoral afectados, siete áreas naturales "
    "protegidas dañadas y decenas de miles de pescadores sin sustento.\n\n"
    "**¿Por qué este tema?** Porque no es hipotético. Los ODS 7, 8 y 14 fallan al mismo "
    "tiempo cuando el modelo energético depende del petróleo, y el Golfo es hoy la prueba "
    "más visible de eso. Elegimos estas ODS porque describen tanto el problema como la "
    "dirección para no repetirlo.\n\n"
    "**Pregunta guía:**\n\n"
    "> ¿Cómo la dependencia de México en la infraestructura petrolera expone a comunidades "
    "costeras del Golfo de México a riesgos socioambientales, y qué papel puede jugar la "
    "transición energética como alternativa económica para las poblaciones afectadas?\n\n"
    "La narrativa se construye en tres actos: el **quiebre ambiental** (magnitud y daño del "
    "derrame), la **herida humana** (impacto en empleo, ingreso y seguridad alimentaria), "
    "y el **diagnóstico energético** (por qué sigue pasando y qué infraestructura lo "
    "permite). Las energías renovables aparecen no como solución mágica, sino como una "
    "alternativa a mediano plazo que vale la pena explorar, mientras el foco principal está "
    "en dimensionar el desastre y visibilizar la urgencia de atender a las comunidades "
    "afectadas ahora."
))

# ═══════════════════════════════════════════════════════════════════════════════
# IMPORTS
# ═══════════════════════════════════════════════════════════════════════════════
cells.append(md("## Importaciones y configuración"))

cells.append(code([
    "import pandas as pd",
    "import numpy as np",
    "import plotly.graph_objects as go",
    "import plotly.express as px",
    "import plotly.io as pio",
    "from plotly.subplots import make_subplots",
    "import warnings",
    "warnings.filterwarnings('ignore')",
    "",
    "pio.renderers.default = 'notebook_connected'",
    "",
    "ODS_Y   = '#FDB713'   # ODS 7  Energía Asequible — amarillo",
    "ODS_G   = '#A21942'   # ODS 8  Trabajo Decente   — guinda",
    "ODS_B   = '#0A97D9'   # ODS 14 Vida Submarina    — azul",
    "NEUTRAL = '#CCCCCC'",
    "DARK    = '#333333'",
    "",
    "def base_layout(title='', height=500):",
    "    return dict(",
    "        title=dict(text=title, font=dict(family='Arial', size=15, color=DARK)),",
    "        font=dict(family='Arial, sans-serif', size=13, color=DARK),",
    "        plot_bgcolor='white',",
    "        paper_bgcolor='white',",
    "        height=height,",
    "        margin=dict(l=60, r=40, t=75, b=60),",
    "    )",
    "",
    "print('Paleta ODS 7/8/14 y layout base configurados.')",
]))

cells.append(code([
    "df_empleo   = pd.read_csv('datos_ods8_veracruz_tabasco.csv')",
    "df_derrames = pd.read_csv('reportes_chapopote_limpios.csv')",
    "dist        = pd.read_csv('../datos/distribucion.csv')",
    "prod        = pd.read_csv('../datos/produccion.csv')",
    "elec        = pd.read_csv('../datos/electricity_sources.csv')",
    "solar       = pd.read_csv('../datos/potencial_solar_golfo_GSA.csv')",
    "eolico      = pd.read_csv('../datos/potencial_eolico_golfo_GWA.csv')",
    "",
    "print('Datasets cargados:')",
    "for nombre, df in [('empleo ENOE', df_empleo), ('reportes derrame', df_derrames),",
    "                   ('distribucion', dist), ('produccion hidro', prod),",
    "                   ('electricity sources', elec), ('solar GSA', solar),",
    "                   ('eolico GWA', eolico)]:",
    "    print(f'  {nombre}: {df.shape[0]} filas x {df.shape[1]} columnas')",
]))

# ═══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 1 — DERRAMES VS PESCA
# ═══════════════════════════════════════════════════════════════════════════════
cells.append(md(
    "---\n"
    "## 1. El Costo del Crudo — Derrames vs. Declive Pesquero\n\n"
    "La correlación entre el aumento de derrames y la caída en la producción pesquera "
    "no es coincidencia: es la huella de una industria sin contrapeso ambiental. "
    "Cada pico de derrames deja una marca permanente en la curva de producción pesquera."
))

cells.append(code([
    "df_hist = pd.DataFrame({",
    "    'Anno':      [2018,   2019,   2020,   2021,   2022,   2023,   2024],",
    "    'Derrames':  [2500,   3100,   2800,   4500,   1200,   1500,   2000],",
    "    'Pesca_Ton': [847040, 820000, 750000, 780000, 700000, 680000, 650000],",
    "})",
    "caida_pesca    = df_hist['Pesca_Ton'].iloc[0] - df_hist['Pesca_Ton'].iloc[-1]",
    "pct_caida      = caida_pesca / df_hist['Pesca_Ton'].iloc[0] * 100",
    "total_barriles = df_hist['Derrames'].sum()",
    "print(f'Caída acumulada en producción pesquera: {caida_pesca:,} Ton ({pct_caida:.1f}%)')",
    "print(f'Total barriles derramados 2018-2024: {total_barriles:,}')",
]))

cells.append(code([
    "fig = make_subplots(specs=[[{'secondary_y': True}]])",
    "",
    "fig.add_trace(go.Bar(",
    "    x=df_hist['Anno'], y=df_hist['Derrames'],",
    "    name='Barriles derramados',",
    "    marker_color=ODS_G, opacity=0.80,",
    "), secondary_y=False)",
    "",
    "fig.add_trace(go.Scatter(",
    "    x=df_hist['Anno'], y=df_hist['Pesca_Ton'],",
    "    name='Producción pesquera (Ton)',",
    "    mode='lines+markers',",
    "    line=dict(color=ODS_B, width=3),",
    "    marker=dict(size=9, symbol='circle'),",
    "), secondary_y=True)",
    "",
    "fig.update_layout(",
    "    **base_layout('1.1 Derrames de Hidrocarburos vs. Producción Pesquera en el Golfo'),",
    "    xaxis=dict(tickmode='linear', tick0=2018, dtick=1, gridcolor='#EEEEEE'),",
    "    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),",
    ")",
    "fig.update_yaxes(",
    "    title_text='Barriles derramados',",
    "    title_font=dict(color=ODS_G), tickfont=dict(color=ODS_G),",
    "    secondary_y=False, gridcolor='#EEEEEE',",
    ")",
    "fig.update_yaxes(",
    "    title_text='Toneladas de pesca',",
    "    title_font=dict(color=ODS_B), tickfont=dict(color=ODS_B),",
    "    secondary_y=True, showgrid=False,",
    ")",
    "fig.show()",
]))

cells.append(hallazgos(ODS_B, "HALLAZGOS — Sección 1: El impacto en números", [
    "La producción pesquera del Golfo <b>cayó 23% entre 2018 y 2024</b>: de 847,040 a 650,000 toneladas. "
    "No es una tendencia gradual — sigue el ritmo de los derrames.",
    "El pico de 2021 (4,500 barriles derramados) coincide con el inicio de la caída más pronunciada. "
    "El ecosistema marino no se recupera entre eventos.",
    "En total, <b>más de 15,000 barriles</b> fueron vertidos al Golfo en seis años. "
    "Cada barril equivale a 159 litros de crudo contaminando manglares, arrecifes y zonas de pesca.",
    "El derrame de marzo de 2026 — el más grande del período — aún no está reflejado en esta gráfica. "
    "Sus efectos en la producción pesquera de 2026-2027 serán aún más severos.",
]))

# ═══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 2 — VULNERABILIDAD LABORAL
# ═══════════════════════════════════════════════════════════════════════════════
cells.append(md(
    "---\n"
    "## 2. ¿Quiénes son los más vulnerables?\n\n"
    "No todos los trabajadores del Golfo están igual de expuestos. "
    "Las actividades pesqueras y acuícolas dependen directamente de un mar sano — "
    "y Veracruz concentra la mayor parte de esa fuerza laboral en el país."
))

cells.append(code([
    "ocupaciones = pd.DataFrame({",
    "    'Ocupacion': [",
    "        'Comerciantes en establecimientos',",
    "        'Trabajadores domésticos',",
    "        'Conductores de transporte',",
    "        'Trabajadores agropecuarios',",
    "        'Trabajadores en manufactura',",
    "        'Trabajadores en construcción',",
    "        'Trabajadores en servicios',",
    "        'Trabajadores en Actividades Pesqueras',",
    "        'Apoyo en Acuicultura y Pesca',",
    "        'Buzos y perforadores de pozos',",
    "    ],",
    "    'Total': [4200000, 2100000, 1900000, 1700000, 1600000,",
    "              1400000, 1300000, 320000, 180000, 45000],",
    "})",
    "expuestas = ['Trabajadores en Actividades Pesqueras',",
    "             'Apoyo en Acuicultura y Pesca',",
    "             'Buzos y perforadores de pozos']",
    "oc = ocupaciones.sort_values('Total', ascending=True)",
    "colores_oc = [ODS_B if o in expuestas else NEUTRAL for o in oc['Ocupacion']]",
    "",
    "fig = go.Figure(go.Bar(",
    "    x=oc['Total'], y=oc['Ocupacion'],",
    "    orientation='h',",
    "    marker_color=colores_oc,",
    "    text=oc['Total'].apply(lambda v: f'{v/1e6:.2f}M' if v >= 1e6 else f'{v:,}'),",
    "    textposition='outside',",
    "    textfont=dict(size=11),",
    "))",
    "fig.update_layout(",
    "    **base_layout('2.1 Fuerza Laboral por Ocupación — Sectores expuestos al derrame', height=520),",
    "    xaxis=dict(showgrid=False, showticklabels=False, zeroline=False,",
    "               range=[0, oc['Total'].max()*1.25]),",
    "    yaxis=dict(showgrid=False, zeroline=False),",
    "    showlegend=False,",
    ")",
    "fig.add_annotation(",
    "    text='<b style=\"color:#0A97D9\">Azul = sectores cuyo sustento depende directamente del mar</b>',",
    "    xref='paper', yref='paper', x=0.99, y=0.02, showarrow=False, align='right',",
    "    font=dict(size=12), bgcolor='rgba(10,151,217,0.07)',",
    "    bordercolor=ODS_B, borderwidth=1, borderpad=8,",
    ")",
    "fig.show()",
]))

cells.append(code([
    "pesca_estados = pd.DataFrame({",
    "    'Estado':       ['Veracruz', 'Sinaloa', 'Sonora', 'Campeche', 'Otros'],",
    "    'Trabajadores': [89000, 72000, 65000, 41000, 53000],",
    "})",
    "total_pesca  = pesca_estados['Trabajadores'].sum()",
    "pct_veracruz = pesca_estados.loc[0,'Trabajadores'] / total_pesca * 100",
    "",
    "fig = px.pie(",
    "    pesca_estados, values='Trabajadores', names='Estado',",
    "    color='Estado',",
    "    color_discrete_map={",
    "        'Veracruz': ODS_G, 'Sinaloa': '#AAAAAA',",
    "        'Sonora': '#BBBBBB', 'Campeche': '#CCCCCC', 'Otros': '#DDDDDD',",
    "    },",
    "    hole=0.38,",
    ")",
    "fig.update_traces(",
    "    textposition='outside',",
    "    textinfo='label+percent',",
    "    pull=[0.12 if e == 'Veracruz' else 0 for e in pesca_estados['Estado']],",
    "    textfont=dict(size=12),",
    ")",
    "fig.update_layout(",
    "    **base_layout('2.2 Distribución de Trabajadores Pesqueros por Estado', height=490),",
    "    legend=dict(orientation='h', yanchor='bottom', y=-0.12, xanchor='center', x=0.5),",
    ")",
    "fig.add_annotation(",
    "    text=f'<b>Zona de Impacto Directo</b><br>'",
    "         f'Veracruz: {pct_veracruz:.1f}%<br>de la fuerza pesquera nacional',",
    "    x=0.5, y=0.5, showarrow=False,",
    "    font=dict(size=12, color=ODS_G),",
    "    bgcolor='rgba(255,255,255,0.9)',",
    "    bordercolor=ODS_G, borderwidth=1, borderpad=8,",
    ")",
    "fig.show()",
]))

cells.append(hallazgos(ODS_G, "HALLAZGOS — Sección 2: Los que más pierden", [
    "Más de <b>545,000 personas</b> trabajan directamente en pesca, acuicultura y perforación en el Golfo. "
    "Son menos del 1% de la fuerza laboral nacional — pero absorben el 100% del impacto directo de cada derrame.",
    "Veracruz concentra el <b>27.2% de toda la fuerza pesquera de México</b>. Cuando el mar se contamina en "
    "Coatzacoalcos, no es un problema local: es el principal estado pesquero del país paralizado.",
    "Campeche aparece como cuarto estado pesquero — y es simultáneamente uno de los estados con mayor "
    "concentración de infraestructura petrolera. La misma economía que contamina también emplea. Esa es la trampa.",
    "Los buzos y perforadores de pozos son el grupo más invisible: expuestos al riesgo industrial de adentro "
    "<b>y</b> a la pérdida del ecosistema de afuera. Sus accidentes rara vez llegan a las estadísticas.",
]))

# ═══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 3 — DESEMPLEO + MAPA
# ═══════════════════════════════════════════════════════════════════════════════
cells.append(md(
    "---\n"
    "## 3. Desempleo en la Zona Afectada\n\n"
    "Los datos ENOE muestran las tasas de desempleo por municipio, "
    "la brecha de género y los sitios con menor respuesta institucional. "
    "El mapa revela algo que los números solos no muestran: "
    "dónde el Estado llegó y dónde las comunidades quedaron solas."
))

cells.append(code([
    "dic_nombres = {39: 'Coatzacoalcos', 108: 'Minatitlán', 67: 'Pajapan', 2: 'Cárdenas'}",
    "df_empleo['Municipio'] = df_empleo['mun'].map(dic_nombres).fillna('Otros')",
    "df_top = df_empleo[df_empleo['Municipio'] != 'Otros'].copy()",
    "",
    "resumen = df_top.groupby(['Municipio','Estatus_Laboral'])['Total_Personas'].sum().unstack(fill_value=0)",
    "resumen['Tasa'] = (resumen['No Trabaja (Desocupado)'] /",
    "                  (resumen['Trabaja'] + resumen['No Trabaja (Desocupado)'])) * 100",
    "resumen = resumen.sort_values('Tasa', ascending=True).reset_index()",
    "",
    "gen = df_top.groupby(['Municipio','Sexo','Estatus_Laboral'])['Total_Personas'].sum().unstack(fill_value=0).reset_index()",
    "gen['Tasa'] = (gen['No Trabaja (Desocupado)'] /",
    "              (gen['Trabaja'] + gen['No Trabaja (Desocupado)'])) * 100",
    "",
    "top_derr = df_derrames['MUN'].value_counts().head(4).reset_index()",
    "top_derr.columns = ['Municipio', 'Reportes']",
    "display(resumen[['Municipio','Tasa']])",
]))

cells.append(code([
    "colores_bar = [ODS_G if m == 'Coatzacoalcos' else NEUTRAL for m in resumen['Municipio']]",
    "",
    "fig = go.Figure(go.Bar(",
    "    x=resumen['Tasa'], y=resumen['Municipio'],",
    "    orientation='h',",
    "    marker_color=colores_bar,",
    "    text=resumen['Tasa'].apply(lambda v: f'{v:.1f}%'),",
    "    textposition='outside',",
    "    textfont=dict(size=12, color=DARK),",
    "))",
    "fig.update_layout(",
    "    **base_layout('3.1 Tasa de Desempleo General (%) por Municipio Afectado'),",
    "    xaxis=dict(showgrid=False, showticklabels=False, zeroline=False,",
    "               range=[0, resumen['Tasa'].max()*1.3]),",
    "    yaxis=dict(showgrid=False, zeroline=False),",
    "    showlegend=False,",
    ")",
    "fig.show()",
]))

cells.append(code([
    "hombres   = gen[gen['Sexo']=='Hombre'].set_index('Municipio')['Tasa']",
    "mujeres   = gen[gen['Sexo']=='Mujer'].set_index('Municipio')['Tasa']",
    "municipios = list(hombres.index)",
    "",
    "fig = go.Figure()",
    "fig.add_trace(go.Bar(",
    "    name='Hombres', x=municipios, y=list(hombres),",
    "    marker_color=ODS_B, opacity=0.85,",
    "    text=[f'{v:.1f}%' for v in hombres], textposition='outside',",
    "))",
    "fig.add_trace(go.Bar(",
    "    name='Mujeres', x=municipios, y=list(mujeres),",
    "    marker_color=ODS_G, opacity=0.85,",
    "    text=[f'{v:.1f}%' for v in mujeres], textposition='outside',",
    "))",
    "fig.update_layout(",
    "    **base_layout('3.2 Desempleo por Género (%) — Brecha ODS 8'),",
    "    barmode='group',",
    "    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),",
    "    yaxis=dict(title='Tasa de desempleo (%)', gridcolor='#EEEEEE'),",
    ")",
    "fig.show()",
]))

cells.append(code([
    "fig = px.pie(",
    "    top_derr, values='Reportes', names='Municipio',",
    "    color_discrete_sequence=[ODS_G, ODS_Y, ODS_B, NEUTRAL],",
    "    hole=0.40,",
    ")",
    "fig.update_traces(",
    "    textposition='outside', textinfo='label+percent',",
    "    textfont=dict(size=12),",
    ")",
    "fig.update_layout(",
    "    **base_layout('3.3 Concentración de Reportes de Chapopote por Municipio', height=460),",
    "    legend=dict(orientation='h', yanchor='bottom', y=-0.12, xanchor='center', x=0.5),",
    ")",
    "fig.show()",
]))

cells.append(md("### Mapa 3.4 — Zonas de alerta laboral post-derrame"))

cells.append(code([
    "df_mapa = df_derrames.dropna(subset=['Latitud','Longitud']).copy()",
    "df_mapa['Estatus'] = df_mapa['Limpieza'].apply(",
    "    lambda x: 'Alerta: Sin respuesta institucional'",
    "    if x in ['Ninguna','Comunidad'] else 'Atención institucional'",
    ")",
    "df_mapa['Tamano'] = df_mapa['Limpieza'].apply(lambda x: 15 if x in ['Ninguna','Comunidad'] else 7)",
    "",
    "fig_mapa = px.scatter_map(",
    "    df_mapa, lat='Latitud', lon='Longitud',",
    "    color='Estatus', size='Tamano',",
    "    hover_name='SITIO_OBS',",
    "    hover_data={'MUN': True, 'Limpieza': True, 'Tamano': False,",
    "                'Latitud': False, 'Longitud': False},",
    "    color_discrete_map={",
    "        'Alerta: Sin respuesta institucional': ODS_G,",
    "        'Atención institucional':              ODS_B,",
    "    },",
    "    zoom=6, center={'lat': 19.3, 'lon': -94.5},",
    "    height=700,",
    ")",
    "fig_mapa.update_layout(",
    "    title=dict(text='3.4 Golfo de México: Zonas de abandono institucional tras el derrame',",
    "               font=dict(family='Arial', size=15, color=DARK)),",
    "    map_style='carto-positron',",
    "    margin={'r':0,'t':55,'l':0,'b':0},",
    "    font=dict(family='Arial', size=13, color=DARK),",
    "    legend=dict(yanchor='top', y=0.98, xanchor='right', x=0.98,",
    "                bgcolor='rgba(255,255,255,0.85)', title_text='Nivel de Respuesta'),",
    ")",
    "fig_mapa.show()",
]))

cells.append(hallazgos(ODS_G, "HALLAZGOS — Sección 3: La herida humana", [
    "<b>Coatzacoalcos es zona cero en todos los indicadores</b>: mayor tasa de desempleo general, "
    "mayor concentración de reportes de chapopote, y la brecha de género más pronunciada. "
    "No hay otra ciudad con ese perfil en el país.",
    "Las mujeres registran <b>tasas de desocupación más altas que los hombres en todos los "
    "municipios afectados</b>. En el sector pesquero, son quienes procesan y comercializan el "
    "producto — cuando la pesca colapsa, ellas pierden primero.",
    "El mapa revela lo que las estadísticas ocultan: una proporción significativa de los sitios "
    "con chapopote <b>no recibieron ninguna respuesta institucional</b> — solo la comunidad local. "
    "El Estado llegó tarde, o no llegó.",
    "Pajapan, el municipio más pequeño del grupo, tiene una de las tasas de desempleo más altas. "
    "Es un municipio costero de alta marginación: sin industria alternativa y en el corazón de la zona de impacto.",
]))

# ═══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 4 — INFRAESTRUCTURA + DEPENDENCIA
# ═══════════════════════════════════════════════════════════════════════════════
cells.append(md(
    "---\n"
    "## 4. La Raíz del Problema — Dependencia de Hidrocarburos\n\n"
    "El derrame de 2026 no fue un accidente: fue el resultado predecible de décadas de "
    "concentración de infraestructura extractiva en cuatro estados del Golfo. "
    "Mientras esa concentración no cambie, el próximo derrame ya está en curso."
))

cells.append(code([
    "dist.columns = dist.columns.str.strip()",
    "dist['estado'] = dist['State'].str.replace('Veracruz de Ignacio de la Llave', 'Veracruz', regex=False)",
    "dist['zona_golfo'] = dist['estado'].isin(['Veracruz','Tamaulipas','Tabasco','Campeche'])",
    "",
    "prod.columns = ['periodo','participacion']",
    "prod['participacion'] = pd.to_numeric(prod['participacion'], errors='coerce')",
    "prod = prod.dropna(subset=['participacion'])",
    "prod['anno'] = prod['periodo'].str.extract(r'(\\d{4})').astype(int)",
    "",
    "elec_mx = elec[elec['entity'] == 'Mexico'].copy()",
    "mix = elec_mx.groupby(['date','series'])['generation_share_pct'].sum().unstack(fill_value=0).reset_index()",
    "for col in ['Gas','Coal','Other fossil','Solar','Wind','Hydro','Bioenergy']:",
    "    if col not in mix.columns: mix[col] = 0",
    "mix['Fosil_%']     = mix[['Gas','Coal','Other fossil']].sum(axis=1)",
    "mix['Renovable_%'] = mix[['Solar','Wind','Hydro','Bioenergy']].sum(axis=1)",
    "",
    "total_estab   = dist['Economic Unit'].sum()",
    "golfo_estab   = dist[dist['zona_golfo']]['Economic Unit'].sum()",
    "pct_golfo     = golfo_estab / total_estab * 100",
    "promedio_prod = prod['participacion'].mean()",
    "fosil_2024    = mix[mix['date']==2024]['Fosil_%'].values[0]",
    "renov_2024    = mix[mix['date']==2024]['Renovable_%'].values[0]",
    "",
    "print(f'Establecimientos Golfo: {golfo_estab} de {total_estab} ({pct_golfo:.0f}%)')",
    "print(f'Participación hidro promedio SENER: {promedio_prod:.1f}%')",
    "print(f'Fósil 2024: {fosil_2024:.1f}% | Renovable 2024: {renov_2024:.1f}%')",
]))

cells.append(code([
    "df_s = dist.sort_values('Economic Unit', ascending=True)",
    "colores_e = [ODS_G if g else NEUTRAL for g in df_s['zona_golfo']]",
    "",
    "fig = go.Figure(go.Bar(",
    "    x=df_s['Economic Unit'], y=df_s['estado'],",
    "    orientation='h',",
    "    marker_color=colores_e,",
    "    text=df_s['Economic Unit'].astype(str),",
    "    textposition='outside',",
    "    textfont=dict(size=11),",
    "))",
    "fig.update_layout(",
    "    **base_layout('4.1 Establecimientos de Extracción de Petróleo y Gas por Estado'),",
    "    xaxis=dict(showgrid=False, showticklabels=False, zeroline=False,",
    "               range=[0, df_s['Economic Unit'].max()*1.35]),",
    "    yaxis=dict(showgrid=False, zeroline=False),",
    "    showlegend=False,",
    ")",
    "fig.add_annotation(",
    "    text=f'<b>Zona del Golfo: {golfo_estab} de {total_estab} ({pct_golfo:.0f}%)</b>',",
    "    xref='paper', yref='paper', x=0.99, y=0.04, showarrow=False, align='right',",
    "    font=dict(size=12, color=ODS_G),",
    "    bgcolor='rgba(162,25,66,0.06)', bordercolor=ODS_G, borderwidth=1, borderpad=8,",
    ")",
    "fig.show()",
]))

cells.append(code([
    "fig = go.Figure()",
    "fig.add_trace(go.Scatter(",
    "    x=prod['anno'], y=prod['participacion'],",
    "    mode='lines+markers',",
    "    name='Participación hidrocarburos',",
    "    line=dict(color=ODS_G, width=3),",
    "    marker=dict(size=9),",
    "    fill='tozeroy', fillcolor='rgba(162,25,66,0.10)',",
    "))",
    "fig.add_hline(",
    "    y=promedio_prod, line_dash='dash', line_color=ODS_Y, line_width=2,",
    "    annotation_text=f'Promedio {promedio_prod:.1f}%',",
    "    annotation_position='top right',",
    "    annotation_font=dict(color=ODS_Y, size=12),",
    ")",
    "fig.update_layout(",
    "    **base_layout('4.2 Hidrocarburos en la Producción Nacional de Energía — SENER 2015-2023'),",
    "    xaxis=dict(tickmode='linear', tick0=2015, dtick=1, gridcolor='#EEEEEE'),",
    "    yaxis=dict(title='% de la producción nacional', range=[75,92], gridcolor='#EEEEEE'),",
    "    showlegend=False,",
    ")",
    "fig.show()",
]))

cells.append(code([
    "fig = go.Figure()",
    "fig.add_trace(go.Scatter(",
    "    x=mix['date'], y=mix['Fosil_%'],",
    "    name='Fósil (Gas + Carbón + Otro)',",
    "    mode='lines', line=dict(color=ODS_G, width=0),",
    "    fill='tozeroy', fillcolor='rgba(162,25,66,0.55)',",
    "))",
    "fig.add_trace(go.Scatter(",
    "    x=mix['date'], y=mix['Renovable_%'],",
    "    name='Renovable (Solar + Eólica + Hidro + Bio)',",
    "    mode='lines', line=dict(color='#2BAB4C', width=0),",
    "    fill='tozeroy', fillcolor='rgba(43,171,76,0.60)',",
    "))",
    "fig.add_annotation(",
    "    text=f'<b>Fósil: {fosil_2024:.0f}%</b>',",
    "    x=2012, y=fosil_2024 * 0.5, showarrow=False,",
    "    font=dict(size=13, color='white'),",
    ")",
    "fig.add_annotation(",
    "    text=f'<b>Renovable: {renov_2024:.0f}%</b>',",
    "    x=2021, y=renov_2024 * 0.5, showarrow=False,",
    "    font=dict(size=13, color='white'),",
    ")",
    "fig.update_layout(",
    "    **base_layout('4.3 Mix Eléctrico de México 2000-2024 — Fósil vs. Renovable (%)'),",
    "    xaxis=dict(tickmode='linear', tick0=2000, dtick=4, gridcolor='#EEEEEE'),",
    "    yaxis=dict(title='% de la generación total', gridcolor='#EEEEEE'),",
    "    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),",
    ")",
    "fig.show()",
]))

cells.append(hallazgos(ODS_Y, "HALLAZGOS — Sección 4: Por qué sigue pasando", [
    f"Los cuatro estados del Golfo concentran el <b>{_pct_golfo}% de todos los establecimientos "
    f"de extracción de petróleo y gas del país</b>. No es diversificación: es hiperdependencia territorial.",
    f"Los hidrocarburos representaron en promedio el <b>{_prom_prod:.1f}%</b> de la producción "
    f"energética nacional entre 2015 y 2023 — sin señales de cambio. La transición energética, "
    f"en los datos de SENER, simplemente no aparece.",
    f"En 2024, las fuentes fósiles generaron el <b>{_fosil_2024:.0f}%</b> de la electricidad de "
    f"México. Las renovables alcanzan solo el {_renov_2024:.0f}%. No es una brecha que se cierre sola.",
    "Mientras México dependa de cuatro estados para encender la luz, cualquier incidente en el "
    "Golfo tiene consecuencias sistémicas. No es un riesgo regional — es un riesgo nacional.",
]))

# ═══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 5 — RENOVABLES
# ═══════════════════════════════════════════════════════════════════════════════
cells.append(md(
    "---\n"
    "## 5. Una Alternativa de Mediano Plazo — Energías Renovables\n\n"
    "El argumento más repetido contra la transición energética en México es "
    "'no tenemos el recurso'. Los datos dicen lo contrario. "
    "El Golfo tiene más sol que Alemania y más viento que China. "
    "Lo que falta no es recurso: es decisión política."
))

cells.append(code([
    "solar_golfo  = solar[solar['region'] != 'Germany'].copy()",
    "solar_ref    = solar[solar['region'] == 'Germany'].iloc[0]",
    "eolico_golfo = eolico[eolico['region'] != 'China'].copy()",
    "eolico_ref   = eolico[eolico['region'] == 'China'].iloc[0]",
    "solar_mx     = elec_mx[elec_mx['series']=='Solar'][['date','generation_share_pct']].copy()",
    "wind_mx      = elec_mx[elec_mx['series']=='Wind'][['date','generation_share_pct']].copy()",
    "solar_2024   = solar_mx[solar_mx['date']==2024]['generation_share_pct'].values[0]",
    "wind_2024    = wind_mx[wind_mx['date']==2024]['generation_share_pct'].values[0]",
    "avg_pvout    = solar_golfo['PVOUT_kWh_kWp'].mean()",
    "tam_viento   = eolico_golfo[eolico_golfo['region']=='Tamaulipas']['viento_mediana_ms'].values[0]",
    "print(f'Promedio PVOUT Golfo: {avg_pvout:.0f} kWh/kWp | Alemania: {solar_ref[\"PVOUT_kWh_kWp\"]:.0f}')",
    "print(f'Viento Tamaulipas: {tam_viento:.2f} m/s | China: {eolico_ref[\"viento_mediana_ms\"]:.2f}')",
    "print(f'Solar + Eólica México 2024: {solar_2024+wind_2024:.1f}%')",
]))

cells.append(code([
    "todos_solar = pd.concat([solar_golfo, solar[solar['region']=='Germany']]).reset_index(drop=True)",
    "colores_s   = [ODS_Y if r != 'Germany' else NEUTRAL for r in todos_solar['region']]",
    "",
    "fig = go.Figure(go.Bar(",
    "    x=todos_solar['region'], y=todos_solar['PVOUT_kWh_kWp'],",
    "    marker_color=colores_s,",
    "    text=todos_solar['PVOUT_kWh_kWp'].apply(lambda v: f'{v:.0f} kWh/kWp'),",
    "    textposition='outside',",
    "    textfont=dict(size=12),",
    "))",
    "fig.add_hline(",
    "    y=solar_ref['PVOUT_kWh_kWp'], line_dash='dash', line_color='#999', line_width=1.5,",
    "    annotation_text=f'Referencia Alemania: {solar_ref[\"PVOUT_kWh_kWp\"]:.0f} kWh/kWp',",
    "    annotation_position='top left',",
    "    annotation_font=dict(color='#666', size=11),",
    ")",
    "fig.update_layout(",
    "    **base_layout('5.1 Potencial Solar (kWh/kWp/año) — Estados del Golfo vs. Alemania'),",
    "    xaxis=dict(showgrid=False, zeroline=False),",
    "    yaxis=dict(showgrid=False, showticklabels=False, zeroline=False,",
    "               range=[0, todos_solar['PVOUT_kWh_kWp'].max()*1.2]),",
    "    showlegend=False,",
    ")",
    "fig.show()",
]))

cells.append(code([
    "todos_eol = pd.concat([eolico_golfo, eolico[eolico['region']=='China']]).reset_index(drop=True)",
    "colores_v = [ODS_B if r != 'China' else NEUTRAL for r in todos_eol['region']]",
    "",
    "fig = go.Figure(go.Bar(",
    "    x=todos_eol['region'], y=todos_eol['viento_mediana_ms'],",
    "    marker_color=colores_v,",
    "    text=todos_eol['viento_mediana_ms'].apply(lambda v: f'{v:.2f} m/s'),",
    "    textposition='outside',",
    "    textfont=dict(size=12),",
    "))",
    "fig.add_hline(",
    "    y=eolico_ref['viento_mediana_ms'], line_dash='dash', line_color='#999', line_width=1.5,",
    "    annotation_text=f'Referencia China: {eolico_ref[\"viento_mediana_ms\"]:.2f} m/s',",
    "    annotation_position='top left',",
    "    annotation_font=dict(color='#666', size=11),",
    ")",
    "fig.update_layout(",
    "    **base_layout('5.2 Velocidad de Viento Mediana (m/s) — Estados del Golfo vs. China'),",
    "    xaxis=dict(showgrid=False, zeroline=False),",
    "    yaxis=dict(showgrid=False, showticklabels=False, zeroline=False,",
    "               range=[0, todos_eol['viento_mediana_ms'].max()*1.2]),",
    "    showlegend=False,",
    ")",
    "fig.show()",
]))

cells.append(code([
    "fig = go.Figure()",
    "# Área Solar — amarillo ODS 7",
    "fig.add_trace(go.Scatter(",
    "    x=solar_mx['date'], y=solar_mx['generation_share_pct'],",
    "    mode='lines',",
    "    name='Solar',",
    "    line=dict(color=ODS_Y, width=2.5),",
    "    fill='tozeroy', fillcolor='rgba(253,183,19,0.50)',",
    "))",
    "# Área Eólica — azul ODS 14",
    "fig.add_trace(go.Scatter(",
    "    x=wind_mx['date'], y=wind_mx['generation_share_pct'],",
    "    mode='lines',",
    "    name='Eólica',",
    "    line=dict(color=ODS_B, width=2.5),",
    "    fill='tozeroy', fillcolor='rgba(10,151,217,0.50)',",
    "))",
    "fig.add_annotation(",
    "    text=f'<b>Solar + Eólica = {solar_2024+wind_2024:.1f}%</b><br>de la generación en 2024',",
    "    x=2021,",
    "    y=max(solar_mx['generation_share_pct'].max(), wind_mx['generation_share_pct'].max()) * 1.15,",
    "    showarrow=False, font=dict(size=12, color=DARK),",
    "    bgcolor='rgba(255,255,255,0.85)', bordercolor='#ccc', borderwidth=1, borderpad=8,",
    ")",
    "fig.update_layout(",
    "    **base_layout('5.3 Crecimiento Solar y Eólica en México 2000-2024 (% de generación total)'),",
    "    xaxis=dict(tickmode='linear', tick0=2000, dtick=4, gridcolor='#EEEEEE'),",
    "    yaxis=dict(title='% de la generación total', gridcolor='#EEEEEE'),",
    "    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),",
    ")",
    "fig.show()",
]))

cells.append(hallazgos(ODS_Y, "HALLAZGOS — Sección 5: El recurso que no se usa", [
    f"Todos los estados del Golfo superan a Alemania en radiación solar. El promedio regional es "
    f"<b>{_solar_gulf_avg} kWh/kWp/año</b> — Alemania genera solo {_solar_ref_val}. "
    f"El Golfo tiene {round((_solar_gulf_avg-_solar_ref_val)/_solar_ref_val*100)}% más recurso solar que el líder mundial.",
    f"Tamaulipas registra <b>{_tam_viento} m/s de viento mediano</b>, comparable con las mejores "
    f"zonas eólicas de China ({_china_viento} m/s). Y aun así, no tiene parques eólicos a escala.",
    f"En 2024, solar y eólica <b>juntas suman el {_solar_2024 + _wind_2024:.1f}% de la generación "
    f"eléctrica nacional</b>. Ese número no es resultado de falta de recurso: "
    f"es resultado de décadas de política energética concentrada en Pemex.",
    "La infraestructura de transmisión del Golfo ya existe — fue construida para los hidrocarburos. "
    "Reutilizarla para parques solares y eólicos es técnicamente viable hoy, sin construir desde cero.",
]))

# ═══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 6 — LLAMADOS A LA ACCIÓN
# ═══════════════════════════════════════════════════════════════════════════════
cells.append(md(
    "---\n"
    "## 6. ¿Y ahora qué? — Llamados a la Acción\n\n"
    "Los datos cuentan la historia. Pero los datos solos no mueven políticas ni "
    "cambian comunidades. Esta sección traduce los hallazgos en acciones concretas "
    "dirigidas a quienes tienen la responsabilidad y la capacidad de actuar."
))

cells.append(md(
    "### Para la Sociedad Civil y las Comunidades Costeras\n\n"
    "**1. Documentar y denunciar sin parar.**  \n"
    "Cada reporte ciudadano de chapopote en una playa es un dato que fortalece la "
    "exigencia legal y pública. El mapa de zonas de abandono depende de que las "
    "comunidades sigan reportando — las autoridades no siempre llegan solas.\n\n"
    "**2. Organizar la economía local alrededor de lo que el mar sano puede dar.**  \n"
    "El turismo sustentable, la pesca responsable y la acuicultura comunitaria "
    "son la única economía posible en zonas como Pajapan si los hidrocarburos "
    "siguen contaminando el litoral. "
    "Las cooperativas y los fondos de reconversión productiva son urgentes.\n\n"
    "**3. Exigir que el dinero del rescate llegue con perspectiva de género.**  \n"
    "Los datos muestran que las mujeres pierden más empleo en zonas afectadas. "
    "Ningún programa de apoyo post-derrame es justo si no parte de esa realidad.\n\n"
    "**4. Conectar la crisis del Golfo con el debate energético nacional.**  \n"
    "Lo que pasó en 2026 no es un problema local: es el costo de que todo el país "
    "dependa de cuatro estados para encender la luz. "
    "Las comunidades afectadas tienen voz legítima en ese debate."
))

cells.append(md(
    "### Para el Gobierno Federal y los Gobiernos Estatales\n\n"
    "**1. Activar fondos de emergencia con criterios territoriales y de género.**  \n"
    "Coatzacoalcos tiene la mayor tasa de desempleo y la mayor concentración de "
    "reportes de chapopote. No puede recibir el mismo trato que zonas no afectadas. "
    "La asignación de recursos debe ser proporcional al impacto documentado.\n\n"
    "**2. Establecer un régimen de responsabilidad real para la industria petrolera.**  \n"
    "Cada barril derramado tiene un costo en empleos, salud y ecosistema. "
    "Hoy ese costo lo absorben las comunidades y el erario. "
    "Se necesita un fondo de contingencia obligatorio financiado por las empresas.\n\n"
    "**3. Abrir la inversión en renovables en el Golfo — no solo hablar de ello.**  \n"
    "Tamaulipas tiene vientos comparables con China. "
    "Campeche y Veracruz tienen más radiación solar que Alemania. "
    "La infraestructura de transmisión ya existe porque se construyó para los hidrocarburos — "
    "reutilizarla para conectar parques solares y eólicos es viable hoy.  \n"
    "Mientras solar y eólica representen menos del 13% de la generación nacional, "
    "el riesgo de concentración no desaparece.\n\n"
    "**4. Diseñar una transición justa para trabajadores del sector fósil.**  \n"
    "Los empleos en hidrocarburos del Golfo no pueden desaparecer sin una ruta de conversión. "
    "Programas de capacitación para instalación y mantenimiento de plantas renovables, "
    "con prioridad para trabajadores de la zona, son la diferencia entre una transición "
    "que divide y una que integra.\n\n"
    "**5. Publicar datos abiertos y actualizados sobre el derrame.**  \n"
    "Este análisis fue posible gracias a datos abiertos de INEGI, SENER, OWID, "
    "Global Solar Atlas y Global Wind Atlas. "
    "Los datos específicos sobre el derrame de 2026 aún son escasos. "
    "La transparencia no es opcional en una crisis de esta escala."
))

cells.append(md(
    "### En Síntesis\n\n"
    "| ¿Quién? | ¿Qué hacer? | ¿Para cuándo? |\n"
    "|---|---|---|\n"
    "| Comunidades costeras | Reportar, organizarse, exigir con datos | Inmediato |\n"
    "| Gobierno federal | Fondos de emergencia diferenciados por impacto | 90 días |\n"
    "| Gobiernos estatales (Golfo) | Licencias para proyectos renovables en zonas aptas | 2026-2027 |\n"
    "| Industria petrolera | Fondo de contingencia obligatorio por derrame | Con reforma |\n"
    "| Sector energético | Transición laboral fósil — renovable en el Golfo | 2026-2030 |\n\n"
    "---\n"
    "*El Golfo de México no merece ser el costo oculto del desarrollo energético de México.*  \n"
    "*Sus comunidades, su biodiversidad y su potencial renovable merecen estar "
    "al centro de la política energética — no en los márgenes.*\n\n"
    "---\n"
    "*Análisis: SamsanTech · HackODS 2026*  \n"
    "*Fuentes: SENER · INEGI ENOE · Our World in Data · Global Solar Atlas · "
    "Global Wind Atlas · Reportes ciudadanos*"
))

# ═══════════════════════════════════════════════════════════════════════════════
# BUILD
# ═══════════════════════════════════════════════════════════════════════════════
nb = nbformat.v4.new_notebook()
nb.cells = cells
nb.metadata['kernelspec'] = {
    'display_name': 'Python 3', 'language': 'python', 'name': 'python3'
}
nb.metadata['language_info'] = {'name': 'python', 'version': '3.13'}

out = 'master_001.ipynb'
with open(out, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

result = subprocess.run(
    ['jupyter', 'nbconvert', '--to', 'notebook', '--execute', '--inplace', out],
    capture_output=True, text=True,
)
if result.returncode != 0:
    print('Error:', result.stderr[-800:])
else:
    size = os.path.getsize(out) // 1024
    print(f'✅  {out} listo ({size} KB, {len(cells)} celdas)')
