from flat import Bill, Flatmate
from reports import PdfReport, FileShare

amount = float(input('Enter the bill amount: '))
period = input('What is the bill period? E.g. December 2022: ')
name1 = input('What is your name?: ')
days_in_house1 = int(input(f'How many days did {name1} stay in the house during the bill period?: '))
name2 = input('What is your flatmate name?: ')
days_in_house2 = int(input(f'How many days did {name2} stay in the house during the bill period?: '))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

pdf_report = PdfReport(period)
pdf_report.generate(flatmate1, flatmate2, the_bill)

file_sharer = FileShare(filepath=f"files/{pdf_report.filename}.pdf")
print(file_sharer.share())
