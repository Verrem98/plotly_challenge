# De INNO-plotly challenge
## Inleiding
Binnen het INNO semester ben ik een proof of concept aan het bouwen om een dashboard te bouwen waar zowel studenten als 
docenten de voortgang zien.
## Uitdaging
In het bestand gauge.py wordt nbij het uitvoeren een html gegenereerd met een plaatje van een gauge en een pijltje erbij.
Dit plaatje wil ik graag integreren in een plotly multigraph "make_subplot".
```shell
specs = [[{'type': 'pie'}, {'type': 'scatter'}], [{'type': 'scatter'}, {'type': 'scatter'}]]
titles = ["Peilmomenten", "Team", "Gilde", "Kennis"]
fig = make_subplots(rows=2, cols=2, subplot_titles=titles, specs=specs)
```
Het lukt mij niet om het wijzertje in de gauge te krijgen. De eerste plot accepteerd geen shapes als het van het type 
"pie" is. De oplossing zit misschien in het gebruik van de x en y referentie.
```shell
xref="paper", yref="paper",
```
Wie o wie heeft een oplossing?