<a id="readme-top"></a>

# PDF Merger

This program is a terminal tool for merging PDF files, outputted as one combined PDF file.

<p align="left">
   <img width="600" alt="image" src="https://github.com/user-attachments/assets/86380fc3-ab0a-4c5c-a86b-554b0836431e"/>
</p>

## Description
PDF Merger involves the user configuring settings in the `main.py` script including:
- PDF files paths to combine
- output PDF name
- output PDF file path

Then, the program can be run to result in a merged PDF of the original files.

## Built With

- [Python 3.13](https://www.python.org/): Programming language for complete functionality
- [PyPDF2](https://pypi.org/project/PyPDF2/): Library for merging PDF files

## Quick Start

### Prerequisites

- OS
- Python 3.13 or higher
- Terminal or CLI Access

### Installation

To install PDF Merger, follow these steps:

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

### Setup

To use the demo PDF files, skip the following setup steps. Otherwise, to merge your own files, proceed.

5. Open `main.py`:
   - On Windows:
      ```bash
      notepad main.py
      ```
   - On macOS or Linux
      ```bash
      open main.py
      ```
6. Edit the file's configuration variables to input your own PDF file paths, output PDF name and output PDF file path.
      ```bash
      # ENTER PDF FILE PATHS, OUTPUT PDF NAME, AND OUTPUT PDF PATH HERE.
      pdf_list = ["C:/Users/justi/Downloads/test1.pdf","test2.pdf"] # format with forward slashes and no trailing slash OR use relative file paths by placing the file in the same directory as this script
      output_pdf_name = "merged.pdf"
      output_pdf_path = "" # format with forward slashes and no trailing slash OR leave blank for output file destination to be the same directory as this script
      # ---------------------------------------------------------------
      ```
 

### Run

7. Run PDF Merger:
   ```bash
   python main.py
   ```

## Usage

1. Input 2 or more PDF files in pdf_list.
2. Input a merged PDF name in output_pdf_name.
3. Input a merged PDF path in output_pdf_path.
4. Run the program.
5. Your PDF files are now merged, enjoy!

## Contributing

1. Fork & branch off main.
2. Make your changes.
3. PRs welcome!

## Project Structure

```
├── pdf-merger/
│   ├── main.py                        # contains main program code, configuration and logic
│   ├── test1.pdf                      # sample PDF file #1
│   ├── test2.pdf                      # sample PDF file #2
│   └── merged.pdf                     # sample merged PDF output
```

## Acknowledgements
This project was created to easily combine PDF files without using online tools bloated with ads.

## License
This project is licensed under the [MIT](LICENSE.txt) License. See LICENSE.txt for more information.

<br>

---

Thank you!

<p align="left">
  <a href="mailto:justin.matthew.lee.18@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
  </a>
  <a href="https://www.linkedin.com/in/justin-matthew-lee/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>
    <a href="https://github.com/jusl98">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
</p>

<p align="right">(<a href="#readme-top">BACK TO TOP</a>)</p>
