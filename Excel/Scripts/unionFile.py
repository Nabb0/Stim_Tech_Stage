import os
import pandas as pd

# ottieni la directory corrente
current_dir = "Excel/ProvaComplessa/"

# specifichiamo il pattern di ricerca dei file con estensione .xlsx
pattern = "*.xlsx"

# utilizziamo la funzione glob per cercare i file con il pattern specificato
excel_files = [f for f in os.listdir(current_dir) if f.endswith('.xlsx')]

# Crea un elenco vuoto per contenere i dati di ogni foglio di lavoro
data_frames = []

# Loop attraverso i nomi dei fogli di lavoro e leggi i dati in un oggetto DataFrame
for file_name in excel_files:
    excel_file = pd.ExcelFile(os.path.join(current_dir, file_name))
    for sheet_name in excel_file.sheet_names:
        df = pd.read_excel(excel_file, sheet_name)
        data_frames.append(df)

# Unisci i dati di tutti i fogli di lavoro in un unico DataFrame
merged_df = pd.concat(data_frames, ignore_index=True)

# Salva il DataFrame unito in un nuovo file Excel
merged_df.to_excel("Excel/NewGenerated/sovrascrittura.xlsx", index=False)

