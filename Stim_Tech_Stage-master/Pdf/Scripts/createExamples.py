from faker import Faker
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

faker = Faker('it_IT')

def create_pdf(filename, num_rows):
    pdf = canvas.Canvas(filename, pagesize=letter)

    # Imposta il font
    pdf.setFont("Helvetica", 10)

    # Scrivi i dati nel PDF
    for _ in range(num_rows):
        # Genera dati inventati utilizzando Faker
        nome = faker.first_name()
        cognome = faker.last_name()
        iban = faker.iban()
        data = faker.date()
        numero_telefono = faker.phone_number()

        # Scrivi i dati nel PDF
        pdf.drawString(50, pdf._pagesize[1] - 50, f"Nome: {nome}")
        pdf.drawString(50, pdf._pagesize[1] - 65, f"Cognome: {cognome}")
        pdf.drawString(50, pdf._pagesize[1] - 80, f"IBAN: {iban}")
        pdf.drawString(50, pdf._pagesize[1] - 95, f"Data: {data}")
        pdf.drawString(50, pdf._pagesize[1] - 110, f"Numero di telefono: {numero_telefono}")

        # Aggiungi una nuova pagina per ogni riga
        pdf.showPage()

    # Salva il PDF
    pdf.save()


def main():
    # Numero di righe da generare nel PDF
    num_rows = 20
    # Crea il file PDF
    i = 1
    for i in range(1, 6):
        create_pdf("E:/informatica/Visual Studio Code Projects/py projects/Stim Script/Pdf/File/dati{}.pdf".format(i), num_rows)


main()


