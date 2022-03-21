import textstat
import os
import glob
import pdf2txt

def get_text_readability(pdf_file_name):
    """
    This function returns the readability score of the given pdf file.
    """
    pdf2txt.read_pdf(pdf_file_name)
    text_file = open("data/txts/{}txt".format(pdf_file_name.strip("data/pdfs/")), "r")
    text = text_file.read()
    return textstat.flesch_reading_ease(text)

def run_through_all_files(main_dir):
    """
    This function runs through all the pdf files in the given directory and returns the readability scores.
    """
    readability_scores = {}
    for file in glob.glob(os.path.join(main_dir, "*.pdf")):
        readability_scores[file.strip("data/pdfs/").strip(".")] = get_text_readability(file)
    return readability_scores

def export_to_csv(value_dict):
    """
    This function exports the readability scores to a csv file.
    """
    with open("data/readability_scores.csv", "w") as csv_file:
        for key, value in value_dict.items():
            csv_file.write("{},{}\n".format(key, value))

if __name__ == "__main__":
    # print(get_text_readability("watchOS8.pdf"))
    dictionary = run_through_all_files("data/pdfs")
    export_to_csv(dictionary)
    # print(run_through_all_files("data/pdfs"))