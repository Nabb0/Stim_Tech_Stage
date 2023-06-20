import re
import os
import phonenumbers

#!Metodi Generali
#?Check list
def creaLista():
    words = ["Nome:", "Cognome:", "Mittente:", "Destinatario:", "Richiedente:", "Firmatario:", "Testimone:", "Notaio:", "Debitore:", "Creditore:", "Procuratore:", "Beneficiario:", "Garante:", "Contraente:", "Testatore:", "Beneficiario effettivo:", "Amministratore:", "Titolare:", "Proprietario:", "Inquilino:", "Reclamante:", "Responsabile legale:", "Agente:", "Giudice:", "Avvocato:", "Proponente:", "Curatore:", "Supplente:", "Padrone di casa:", "Testimone oculare:", "Assicurato:", "Beneficiario fiduciario:", "Beneficiario di polizza:", "Coobbligato:", "Curatore speciale:", "Datore di lavoro:", "Difensore:", "Donante:", "Esecutore testamentario:", "Garante finanziario:", "Garante solidale:", "Intermediario:", "Legatario:", "Mediatore:", "Perito:", "Premiante:", "Promittente:", "Proposto:", "Referente:", "Richiedente asilo:", "Soggetto obbligato:", "Testimone esperto:", "Tribunale:", "Ufficiale pubblico:", "Valutatore:", "Venditore:", "Acquirente:", "Conduttore:", "Lasciatario:", "Locatore:", "Concessionario:", "Contraente principale:", "Contraente secondario:", "Locatario:", "Mandante:", "Mandatario:", "Offerta:", "Ricevente:", "Sofferente:", "Subappaltatore:", "Subentrante:", "Sublocatario:", "Sublocatore:", "Testimone di nozze:", "Promittente venditore:", "Promissario acquirente:"]

    # Duplica le parole senza i due punti
    words_no_colon = [word.replace(":", "") for word in words]

    # Unisci le due liste
    words_combined = words + words_no_colon

    return words_combined


#?Estrai riga con parola senza spazi
def extract_context(text, keyword):
    pattern = r"\b(\w+)\b"  # Pattern per estrarre le parole nel testo

    # Trova tutte le parole nel testo
    words = re.findall(pattern, text)

    context_words = []
    found_keyword = False

    # Trova l'indice della parola chiave nel testo
    for i, word in enumerate(words):
        if word == keyword:
            found_keyword = True
            keyword_index = i
            break

    # Estrai le tre parole precedenti e le tre parole successive alla parola chiave
    if found_keyword:
        start_index = max(0, keyword_index - 6)
        end_index = min(keyword_index + 8, len(words))

        context_words = words[start_index:end_index]

    return context_words


#?Estrai riga con parola con spazi
def extract_special_context(text, keyword):
    pattern = r"(\b\+39\s*\d{2,3}\s*\d{2,3}\s*\d{2,4}\b|\b\d{2,3}\s*\d{2,3}\s*\d{2,4}\b)"  # Pattern per riconoscere numeri di telefono italiani

    # Trova tutti i numeri di telefono nel testo
    phone_numbers = re.findall(pattern, text)

    context_words = []
    found_keyword = False

    # Trova l'indice del numero di telefono contenente la parola chiave nel testo
    for i, phone_number in enumerate(phone_numbers):
        if keyword in phone_number:
            found_keyword = True
            keyword_index = i
            break

    # Estrai le tre parole precedenti e le tre parole successive al numero di telefono contenente la parola chiave
    if found_keyword:
        start_index = max(0, keyword_index - 6)
        end_index = min(keyword_index + 8, len(phone_numbers))

        context_words = phone_numbers[start_index:end_index]

    return context_words


#?Check method
def checkLists(oggetto):
    for value in oggetto.values(): #Primo ciclo prende i valori delle chiavi
        for i in range(len(value)):
            for j in range(len(value[i])):
                if isinstance(value[i][j], str):
                    var1 = value[i][j]
                    if isinstance(value[i + 1][j], list):
                        for x in value[i + 1][j]:
                            if var1 == x:
                                print('match')


#!Estrazione degli iban
def extract_iban(text):
    pattern = r"\b(?:IT|SM)[0-9]{2}[A-Za-z][0-9]{22}\b"  # Pattern to recognize an Italian or Sanmarinese IBAN

    ibans = re.findall(pattern, text)
    return ibans

def extract_iban_from_txt(text):
    ibans = extract_iban(text)
    return ibans

def visIban(directory):
    lista = []
    listaRighe = []
    file_list = os.listdir(directory)
    for file in file_list:
        if file.endswith(".txt"):
            file_path = os.path.join(directory, file)
            with open(file_path, 'r') as file:
                text = file.read()
            ibans = extract_iban_from_txt(text)
            lista.append(ibans)

            for iban in ibans:
                context = extract_context(text, iban)
                listaRighe.append(context)
            lista.append(listaRighe)
            
    return lista


#!Estrazione codice fiscale
def extract_codice_fiscale(text):
    pattern = r"\b[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]\b"  # Pattern per riconoscere un codice fiscale italiano

    codici_fiscali = re.findall(pattern, text)
    return codici_fiscali

def extract_codice_fiscale_from_txt(text):
    codici_fiscali = extract_codice_fiscale(text)
    return codici_fiscali

def visCodFisc(directory):
    lista = []
    listaRighe = []
    file_list = os.listdir(directory)
    for file in file_list:
        if file.endswith(".txt"):
            file_path = os.path.join(directory, file)
            with open(file_path, 'r') as file:
                text = file.read()
            codici_fiscali = extract_codice_fiscale_from_txt(text)
            lista.append(codici_fiscali)

            for codice_fiscale in codici_fiscali:
                context = extract_context(text, codice_fiscale)
                listaRighe.append(context)
            lista.append(listaRighe)

    return lista


#!Estrazione Nome e Cognome
def extract_nomi(text):
    textSplit = text.split()
    j = 0
    lista = []
    controllo = creaLista()
    for i in textSplit:
        dato = ''
        for k in controllo: 
            if i == k:
                dato = textSplit[j + 1]
                lista.append(dato)
                if textSplit[j + 2][0].isupper() and textSplit[j + 2][1].islower() and textSplit[j + 2] != 'C.F:' and textSplit[j + 2] != 'Cognome:':
                    lista.append(textSplit[j + 2])
        j += 1
    return lista

def extract_nomi_from_txt(text):
    nomi = extract_nomi(text)
    return nomi

def visNome(directory):
    lista = []
    listaRighe = []
    file_list = os.listdir(directory)
    for file in file_list:
        if file.endswith(".txt"):
            file_path = os.path.join(directory, file)
            with open(file_path, 'r') as file:
                text = file.read()
            nomi = extract_nomi_from_txt(text)
            lista.append(nomi)
           
            for nome in nomi:
                context = extract_context(text, nome)
                listaRighe.append(context)
            lista.append(listaRighe)

    return lista


#!Estrazione Date
def extract_dates_from_text(text):
    pattern = r"\b\d{4}[-/]\d{2}[-/]\d{2}\b"  # Pattern to recognize dates in "dd/mm/yyyy" or "dd-mm-yyyy" format

    dates = re.findall(pattern, text)
    return dates

def extract_dates_from_txt(text):
    dates = extract_dates_from_text(text)
    return dates

def visDate(directory):
    lista = []
    listaRighe = []
    file_list = os.listdir(directory)
    for file in file_list:
        if file.endswith(".txt"):
            file_path = os.path.join(directory, file)
            with open(file_path, 'r') as file:
                text = file.read()
            dates = extract_dates_from_txt(text)
            lista.append(dates)

            for date in dates:
                context = extract_special_context(text, date)
                listaRighe.append(context)
            lista.append(listaRighe)
    
    return lista


#!Estrai numero di telefono
def extract_phone_numbers_from_text(text):
    phone_numbers = []

    # Trova tutti i possibili numeri di telefono nel testo
    for match in phonenumbers.PhoneNumberMatcher(text, "IT"):
        phone_number = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        phone_numbers.append(phone_number)

    return phone_numbers

def extract_phone_numbers_from_txt(text):
    phone_numbers = extract_phone_numbers_from_text(text)
    return phone_numbers

def visPhoneNumbers(directory):
    lista = []
    listaRighe = []
    file_list = os.listdir(directory)
    for file in file_list:
        if file.endswith(".txt"):
            file_path = os.path.join(directory, file)
            with open(file_path, 'r') as file:
                text = file.read()
            phone_numbers = extract_phone_numbers_from_txt(text)
            lista.append(phone_numbers)

            for phone_number in phone_numbers:
                context = extract_special_context(text, phone_number)
                listaRighe.append(context)
            lista.append(listaRighe)
    
    return lista


def main():
    directory = "E:/informatica/Visual Studio Code Projects/py projects/Stim Script/Txt/File/"
    # oggetti = {'ibans': visIban(directory), 'codFis': visCodFisc(directory), 'nomi': visNome(directory), 'date': visDate(directory), 'num': visPhoneNumbers(directory)}

    oggetto = {'ibans' : visIban(directory)}
    checkLists(oggetto)
    
    
main()
