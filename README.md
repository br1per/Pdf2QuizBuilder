# Pdf2QuizBuilder

Pdf2QuizBuilder is a Python GUI application that allows users to visually select question regions from a PDF, assign correct answers, and automatically save this data in a structured `output.json` file. Each selected region is also cropped and saved as an image.

This tool is ideal for teachers, examiners, dataset creators, and anyone who needs to extract quiz content from PDF documents.

## ✨ Features

- Load any PDF file using a file picker dialog
- Scroll and navigate pages
- Draw a rectangle to select a question area
- Enter the correct answer in a popup prompt
- Save:
  - Page number and coordinates of the selection
  - The answer
  - A cropped image of the selected region
  - Data as structured JSON

## 🖥️ User Interface

- Click and drag to draw a red dashed rectangle over a question
- A prompt will request the correct answer
- Use the **← Previous Page** and **Next Page →** buttons to navigate
- All questions are saved to `output.json`
- Cropped images are saved in the `resources/` directory

## 📦 Requirements

- Python 3.7+
- [PyMuPDF](https://pypi.org/project/PyMuPDF/)
- Pillow

Install dependencies:

```bash
pip install PyMuPDF Pillow
