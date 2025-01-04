<p align="center">
   <img width="500" alt="image" src="https://github.com/user-attachments/assets/86380fc3-ab0a-4c5c-a86b-554b0836431e"/>
</p>

# PDF Merger
PDF Merger is a tool to easily merge PDF files, including error handling which I created using the PyPDF2 library.

## About This Project
This PDF merger works by inputting two or more PDF files by changing the PDF file paths, output PDF name and output PDF path in the main.py script and running the program to result in a merged PDF of the original files.

## Technologies Used
- Python 3.13
- PyPDF2 Library

## Installation
To install the PDF Merger, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/jusL98/pdf-merger.git
   cd pdf-merger
   ```

2. Ensure that you have python running on your system.

3. Create and activate a virtual environment:
   - On Windows:

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

   - On macOS and Linux:
   
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

4. Install the required dependencies:

   ```bash
   pip install PyPDF2 
   ```

5. Run the PDF Merger to view the demo which saves the merged file in the same directory as the main.py script using two test PDF files.
   ```bash
   python main.py
   ```

6. **To merge your own files:**
   - Repeat steps 1-4
   - Navigate to the cloned directory
   - Edit main.py to input your own PDF file paths, output PDF name and output PDF file path.
      ```bash
      # ENTER PDF FILE PATHS, OUTPUT PDF NAME, AND OUTPUT PDF PATH HERE.
      pdf_list = ["C:/Users/justi/Downloads/test1.pdf","test2.pdf"] # format with forward slashes and no trailing slash OR use relative file paths by placing the file in the same directory as this script
      output_pdf_name = "merged.pdf"
      output_pdf_path = "" # format with forward slashes and no trailing slash OR leave blank for output file destination to be the same directory as this script
      # ---------------------------------------------------------------
      ```
   - Run the program and locate the merged PDF file

## Usage
1. Input two or more PDF files in pdf_list.
2. Input a merged PDF name in output_pdf_name.
3. Input a merged PDF path in output_pdf_path.
4. Run the program.
5. Your PDF files are now merged!

---

Thank you!
