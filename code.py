from bs4 import BeautifulSoup
import pandas as pd

html_path = r"YOUR_DIRECT_HTML_FILE_HERE"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "lxml")
tables = soup.find_all("table")

with pd.ExcelWriter("data.xlsx", engine="openpyxl") as writer:
    for i, table in enumerate(tables):
        try:
            df = pd.read_html(str(table))[0]
            sheet_name = f"Sheet{i+1}"
            df.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"✅ Successfully recorded to sheet: {sheet_name}")
        except Exception as e:
            print(f"❌ Can't process the table {i+1}: {e}")
