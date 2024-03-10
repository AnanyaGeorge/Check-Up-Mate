from docx import Document
from fuzzywuzzy import fuzz

def read_word_document(file_path):
    doc = Document(file_path)
    content = []

    for paragraph in doc.paragraphs:
        content.append(paragraph.text)

    return '\n'.join(content)

def compare_reports(report1, report2):
    similarity_ratio = fuzz.ratio(report1, report2)
    return similarity_ratio


file_path_report1 =r"C:\Users\user\OneDrive\Desktop\bs-rpt.docx"
file_path_report2 =r"C:\Users\user\OneDrive\Desktop\bs-rpt1.docx"

report1_content = read_word_document(file_path_report1)
report2_content = read_word_document(file_path_report2)

similarity_ratio = compare_reports(report1_content, report2_content)

print(f"Similarity ratio between the two reports: {similarity_ratio}%")
rangecheck=(80,100)
if rangecheck[0]<=similarity_ratio<=rangecheck[1]:
    print("\n\t No issues found, please consult doctor for further queries")
else:
    print(f"Similarity ratio between the two reports:v{similarity_ratio}% -issues have been detected , consult doctor immediately")
