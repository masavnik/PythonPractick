from openpyxl import load_workbook

workbook = load_workbook(filename="Example.xlsx")
sheet = workbook.active
sheet.freeze_panes = "C2"
workbook.save("sample_frozen.xlsx")