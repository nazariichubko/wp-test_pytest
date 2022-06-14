import requests
import xlwt
from xlwt import Workbook

wb = Workbook()
sheet = wb.add_sheet("test_result.csv")

def get_localhost_website():
    response = requests.get("http://localhost:3000/users")
    return response


print(get_localhost_website())

if get_localhost_website().status_code == 200:
    positive_result = "Website is running"
    print(positive_result)
    sheet.write(1, 0, positive_result)
else:
    negative_result = "website is not reached"
    print(negative_result)
    sheet.write(1, 0, negative_result)

wb.save("test_result.csv")