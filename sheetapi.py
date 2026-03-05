import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=scopes
)

client = gspread.authorize(creds)

sheet = client.open_by_key(
    "1n-eXUsHuDEWaLY4XYKAstwU2dyxE8XaAFbwbQ7WSlWk"
).sheet1

# เพิ่มแถวใหม่
#sheet.append_row(["Sirichai", "Test OK", "2026"])
#sheet.update("A1:C1", [["ว/ด/ป","สถานะ",""]]) อัพเดตข้อมูล
""" sheet.append_row(["01/03/69", "เปิด"])
data = sheet.get_all_values()
print(data)
print("เพิ่มข้อมูลเรียบร้อย") """

def appendsheet(brand, model, year, price):
    sheet.append_row([brand, model, year, price])

def deleterow(row):
    sheet.delete_rows(row)

def update_price(row, price):
    sheet.update_cell(row, 4, price)