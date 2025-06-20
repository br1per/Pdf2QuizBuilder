# QuestionSnap

**QuestionSnap** is a Python-powered graphical tool that lets you visually mark up questions on any PDF file. Simply select a region of interest, assign an answer, and it automatically extracts cropped images and generates a structured JSON file—perfect for creating quizzes, building datasets, or preparing test materials.

---

## 🚀 Features

- Load PDF files into an interactive canvas
- Draw rectangles to highlight question zones
- Prompt for the correct answer after each selection
- Save cropped image of each marked area
- Generate a JSON file with all annotations
- Navigate between PDF pages within the interface

---

## 📦 Dependencies

Make sure you have the following installed:

```bash
pip install pymupdf pillow
```

> `tkinter`, `json`, and `os` are standard libraries. On some Linux distros, you may need to install `tkinter` separately (e.g. `sudo apt install python3-tk`).

---

## 🛠️ How to Use

```bash
python main.py
```

1. Choose a PDF file via the file dialog that appears.
2. Use your mouse to draw a rectangle on a question area.
3. When you release, input the correct answer in the pop-up dialog.
4. The app crops that region and saves it as a `.png` file in `resources/`.
5. The answer, image path, and bounding box data are stored in `output.json`.
6. Use the **Next Page** and **Previous Page** buttons to navigate the PDF.
7. Close the app when you’re done. Your data is saved automatically.

---

## 📂 Output Structure

```
QuestionSnap/
├── main.py
├── output.json
├── resources/
│   ├── 1.png
│   ├── 2.png
│   └── ...
└── tmp/
    └── current.png
```

### Example JSON Entry

```json
{
  "id": 1,
  "page_number": 0,
  "coords": [100, 150, 300, 250],
  "question": "",
  "correct_answer": "42",
  "image_path": "resources/1.png"
}
```

---

## 🧠 Use Cases

- Teachers generating visual tests and answer keys
- Dataset curation for machine learning or OCR
- Educational startups and EdTech prototyping
- Fast visual quiz creation for worksheets or apps

---

## 🔮 Future Improvements

Here are some ideas to make **QuestionSnap** even more powerful:

- ✏️ Add support for freehand annotation or multi-shape selection (e.g. circles, polygons)
- 💬 Enable question text input (not just correct answer)
- 🌐 Export to different formats: CSV, Excel, or custom XML
- 🗂️ Organize questions by tags, chapters, or difficulty levels
- 🌍 Multilingual interface for international users
- 🧠 OCR integration to auto-fill questions or answers based on selected region
- 🖼️ Preview cropped image in dialog before saving
- 🔁 Undo/Redo history for annotation actions
- ☁️ Cloud sync or GitHub integration to manage datasets across devices

Feel free to contribute or suggest more ideas via Issues or Pull Requests!

---

## 📜 License

This project is licensed under the **MIT License**. See `LICENSE` file for details.

---

## ✨ Author

Made with 💡 and 📚 by [@br1per](https://github.com/br1per)
