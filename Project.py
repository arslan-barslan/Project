import tkinter as tk
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import getSampleStyleSheet

def calculate_sum():
	try:
		num1 = float(entry1.get())
		num2 = float(entry2.get())
		karkass=dropdown_value.get()
		kark=800
		if karkass=='ЛМК':
			kark=1000
		visotka=int(visota_value.get())
		Voroti=Vorota_value.get()
		vorota=139500
		if Voroti=='4,0х4,0':
			vorota=248000
		if Voroti=='2,0х2,0':
			vorota=62000
		Kolichest=int(Kolich_value.get())
		sandwich=int(Buterbrod_value.get())
		if sandwich==80:
			sandwich=1000
		if sandwich==100:
			sandwich=1500
		if sandwich==120:
			sandwich=2000

		result =(kark*(num1*num2*visotka)+vorota*Kolichest+sandwich*(num1*num2*visotka))
		label_result.config(text=f"Цена: {result}")
		pdfmetrics.registerFont(TTFont('Noto_Sans', 'Noto_Sans.ttf','utf-8'))
		pdfinfo=  ['Cтатьи расходов', 'Значение'],['Каркасс',str(kark*(num1*num2*visotka))],['Ворота', str(vorota)],['Сендвич Панели', str(sandwich*(num1*num2*visotka))],['Итоговые Расходы', str(result)]
		doc = SimpleDocTemplate("Результат.PDF", pagesize=letter)

		styles = getSampleStyleSheet()
		title_style = styles['Heading1']
		title_style.fontName = 'Noto_Sans'
		title_style.fontSize = 21
		title = Paragraph("Стоимость быстровозводимого здания", title_style)

		table_style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, -1), 'Noto_Sans'),
    ('FONTSIZE', (0, 0), (-1, -1), 14),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
])
		table = Table(pdfinfo, colWidths=[200, 100], rowHeights=[30]*len(pdfinfo))
		table.setStyle(table_style)
		
		elements = []
		elements.append(title)
		elements.append(table)
		doc.build(elements)
		print("PDF-документ успешно создан!")
	except ValueError:
		label_result.config(text="Введите корректные числа.")

root = tk.Tk()
root.minsize(500, 500)
root.title("Калькулятор стоимости строительства быстровозводимых ангаров.")
labelKarkass = tk.Label(root, text="Каркас здания")
labelKarkass.pack(padx=10, pady=5)
options = ['ЛМК', 'ЛСТК']
dropdown_value = tk.StringVar(root)
dropdown_value.set(options[0])
dropdown_menu = tk.OptionMenu(root, dropdown_value, *options)
dropdown_menu.pack(padx=10, pady=5)
label1 = tk.Label(root, text="Ширина здания, м")
label1.pack(padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.pack(padx=10, pady=5)
label2 = tk.Label(root, text="Длина здания, м")
label2.pack(padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.pack(padx=10, pady=5)
labelVisota = tk.Label(root, text="Высота здания (по коньку), м")
labelVisota.pack(padx=10, pady=5)
V = ['3', '4','5']
visota_value = tk.StringVar(root)
visota_value.set(V[0])  # Set default value
visota_menu = tk.OptionMenu(root, visota_value, *V)
visota_menu.pack(padx=10, pady=5)
labelVorota = tk.Label(root, text="Ворота с установкой, м")
labelVorota.pack(padx=10, pady=5)
Vorota = ['3,0х3,0', '4,0х4,0','2,0х2,0']
Vorota_value = tk.StringVar(root)
Vorota_value.set(Vorota[0])  # Set default value
Vorota_menu = tk.OptionMenu(root, Vorota_value, *Vorota)
Vorota_menu.pack(padx=10, pady=5)
labelKolich = tk.Label(root, text="Количество ворот, шт")
labelKolich.pack(padx=10, pady=5)
Kolich = ['1', '2']
Kolich_value = tk.StringVar(root)
Kolich_value.set(Kolich[0])  # Set default value
Kolich_menu = tk.OptionMenu(root, Kolich_value, *Kolich)
Kolich_menu.pack(padx=10, pady=5)
labelButerbrod = tk.Label(root, text="Толщина стеновых сэндвич панелей, мм")
labelButerbrod .pack(padx=10, pady=5)
Buterbrod  = ['80', '100','120']
Buterbrod_value = tk.StringVar(root)
Buterbrod_value.set(Buterbrod[0])  # Set default value
Buterbrod_menu = tk.OptionMenu(root, Buterbrod_value, *Buterbrod)
Buterbrod_menu.pack(padx=10, pady=5)
button_calc = tk.Button(root, text="Подсчет", command=calculate_sum)
button_calc.pack(padx=10, pady=5)
label_result = tk.Label(root, text="")
label_result.pack(padx=10, pady=5)
root.mainloop()
