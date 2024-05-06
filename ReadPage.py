import pdfminer.high_level

def read_pdf_text_miner(filepath):
  """
  This function reads text from a PDF file using PDFMiner library.

  Args:
      filepath: Path to the PDF file.

  Returns:
      A string containing the extracted text from the PDF file.
  """
  text = ""
  with open(filepath, 'rb') as pdf_file:
    doc = pdfminer.high_level.extract_text(pdf_file)
    text = "\n".join(doc)
  return text

# Example usage
filepath = "your_pdf_file.pdf"
extracted_text = read_pdf_text_miner(filepath)
print(extracted_text)