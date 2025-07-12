# 📄 Copy Data from View-Only Google Sheet

This tool allows you to extract data from a **view-only Google Sheet** by leveraging the `htmlview` format and converting the content into an Excel file.  
No Google API access or permission required!

---

## ✅Features

- Bypass Google Sheet "View-Only" restrictions
- Extract clean tabular data into Excel format
- Easy setup using Python, Pandas, and BeautifulSoup

---

## ⚙️Requirements

Make sure you have the following installed:

- [Python 3.x](https://www.python.org/)
- [Visual Studio Code](https://code.visualstudio.com/) (or any code editor)
- Python libraries:
  - `pandas`
  - `beautifulsoup4`
---
## 🚀How to Use
1. Open your view-only Google Sheet in the browser.  
2. Change the URL to `htmlview`  ![Change-the-URL](https://github.com/just-a-dummy/copy-only-view-ggsheet/blob/18d359a3bb055ae6f5ddc678bd9e3bf59b14d409/vid%20(1).gif)  
   - → Press `Enter` to fully load. Save the complete page (.html file) in Complete Web Page mode.  
3. In your Python file, update the path to your downloaded HTML file:  
<img width="390" height="30" alt="image" src="https://github.com/user-attachments/assets/2e41b770-d3f6-4269-9743-a5385f84b2e4" />  
4. Run the script. After running, a new Excel file named `data.xlsx` will be created in the same folder as your Python script.


