Ecco alcuni script per la manipolazione di dati in Excel, PDF e Word:

## Manipolazione di dati in Excel

### Leggere dati da un file Excel

Per leggere dati da un file Excel usando Python, è possibile utilizzare la libreria `pandas`. In questo esempio, supponiamo di voler leggere i dati dal foglio di lavoro "Sheet1" del file "data.xlsx".

```python
import pandas as pd

df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
```

### Scrivere dati in un file Excel

Per scrivere dati in un file Excel usando Python, è possibile utilizzare la libreria `openpyxl`. In questo esempio, supponiamo di voler scrivere i dati nel foglio di lavoro "Sheet1" del file "output.xlsx".

```python
from openpyxl import Workbook

# crea un oggetto Workbook
wb = Workbook()

# seleziona il foglio di lavoro
ws = wb.active
ws.title = "Sheet1"

# scrivi i dati in celle specifiche
ws['A1'] = 'Nome'
ws['B1'] = 'Cognome'
ws['A2'] = 'Mario'
ws['B2'] = 'Rossi'

# salva il file
wb.save('output.xlsx')
```

## Manipolazione di dati in PDF

### Leggere dati da un file PDF

Per leggere dati da un file PDF usando Python, è possibile utilizzare la libreria `PyPDF2`. In questo esempio, supponiamo di voler leggere il testo dal file "document.pdf".

```python
import PyPDF2

# apri il file in modalità lettura binaria
with open('document.pdf', 'rb') as pdf_file:
    # crea un oggetto PdfFileReader
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # seleziona la prima pagina
    page = pdf_reader.getPage(0)

    # estrai il testo dalla pagina
    text = page.extractText()

    print(text)
```

### Scrivere dati in un file PDF

Per scrivere dati in un file PDF usando Python, è possibile utilizzare la libreria `reportlab`. In questo esempio, supponiamo di voler scrivere il testo "Hello, world!" nel file "output.pdf".

```python
from reportlab.pdfgen import canvas

# crea un oggetto Canvas
pdf_canvas = canvas.Canvas('output.pdf')

# scrivi il testo sulla pagina
pdf_canvas.drawString(100, 750, "Hello, world!")

# salva il file
pdf_canvas.save()
```

## Manipolazione di dati in Word

### Leggere dati da un file Word

Per leggere dati da un file Word usando Python, è possibile utilizzare la libreria `python-docx`. In questo esempio, supponiamo di voler leggere il testo dal file "document.docx".

```python
import docx

# apri il file
doc = docx.Document('document.docx')

# estrai il testo dal file
text = ''
for paragraph in doc.paragraphs:
    text += paragraph.text

print(text)
```

### Scrivere dati in un file Word

Per scrivere dati in un file Word usando Python, è possibile utilizzare la libreria `python-docx`. In questo esempio, supponiamo di voler scrivere il testo "Hello, world!" nel file "output.docx".

```python
import docx

# crea un nuovo documento
doc = docx.Document()

# aggiungi un paragrafo al documento
doc.add_paragraph('Hello, world!')

# salva il file
doc.save('output.docx')
```

