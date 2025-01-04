from PyPDF2 import PdfWriter, PdfReader

# ENTER PDF FILE NAMES, OUTPUT PDF NAME, AND OUTPUT PDF PATH HERE.
pdf_list = ["test1.pdf","test2.pdf"]
output_pdf_name = "merged.pdf"
output_pdf_path = "C:/Users/justi/Downloads" # format with forward slashes and no trailing slash
# ---------------------------------------------------------------

new_pdf = {
    "pdf_name": output_pdf_name,
    "pdf_path": [f"{output_pdf_path}/{output_pdf_name}" if output_pdf_path else output_pdf_name][0],
    "total_num_of_pages": 0,
}

def main() -> None:
    status = True
    
    print("\n*********  PDF MERGER  *********\n")
    print("Attempting to merge the following PDFs:")
    print(f"- {"\n- ".join(pdf_list)}")
    print("-----------------------------\n")

    for pdf in pdf_list:
        try:
            num_of_pages = len(PdfReader(pdf).pages)
            print(f"✓ - PDF {pdf_list.index(pdf)+1}, '{pdf}' has {num_of_pages} page." if num_of_pages == 1 else f"✓ - PDF {pdf_list.index(pdf)+1}, {pdf} has {num_of_pages} pages.")
            new_pdf["total_num_of_pages"] += num_of_pages

            merger.append(pdf)

        except FileNotFoundError:
            print(f"X - PDF {pdf_list.index(pdf)+1} '{pdf}' not found.")
            status = False

    return status

if __name__ == "__main__":
    merger = PdfWriter()
    try:
        status = main()

        if status:
            merger.write(new_pdf["pdf_path"])
            print("\n-----------------------------")
            print(f"PDFs successfully merged as '{new_pdf["pdf_name"]}' with {new_pdf["total_num_of_pages"]} total pages.")
            print(f"Output PDF path: {new_pdf['pdf_path']}\n")
            merger.close()
        elif not status:
            print("\n-----------------------------")
            print(f"Exiting program. Please check the original pdf file paths and try again. ({', '.join(pdf_list)})\n")
            exit()
    except FileNotFoundError:
        print("\n-----------------------------")
        print(f"Exiting program. Please check the merged output path and try again. ({output_pdf_path})\n")
    except Exception as e:
        print("\n-----------------------------")
        print(f"Exiting program. An error occurred: {e}\n")