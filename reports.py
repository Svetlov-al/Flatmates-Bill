import webbrowser

from fpdf import FPDF

from filestack import Client
from dotenv import load_dotenv
import os

load_dotenv()

FILESTACK_API_KEY = os.getenv('FILESTACK_API_KEY')


class PdfReport:
    """
    Creates a pdf file that contains data about
    the flatmates such as ther names, their due amount
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', format='A4', unit='pt')
        pdf.add_page()

        # Add icon
        pdf.image('files/house.png', w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)

        # Insert period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period', border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=f"{flatmate1.pays(bill, flatmate2)} $", border=1, ln=1)
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=f"{flatmate2.pays(bill, flatmate1)} $", ln=1, border=1)
        pdf.output(f"files/{self.filename}.pdf")
        webbrowser.open('file://' + os.path.realpath(f"files/{self.filename}") + '.pdf')


class FileShare:

    def __init__(self, filepath, api_key=FILESTACK_API_KEY):
        self.api_key = api_key
        self.filepath = filepath

    def share(self):
        new_client = Client(self.api_key)
        new_link = new_client.upload(filepath=self.filepath)
        return new_link.url
