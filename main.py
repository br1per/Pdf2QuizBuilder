import fitz  
import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox
from PIL import Image, ImageTk
import json
import os

page_index = 0
questions = [] 
rect_coords = None
rect = None
start_x = None
start_y = None

def get_next_question_id():
    global questions
    if questions:
        last_id = max([q["id"] for q in questions])
        return last_id + 1
    else:
        return 1

def on_press(event):
    global rect, start_x, start_y, canvas
    total_height = canvas.bbox("all")[3]
    start_frac, _ = canvas.yview()
    visible_top_y = start_frac * total_height

    start_x = event.x
    start_y = event.y + visible_top_y
    if rect:
        canvas.delete(rect)
    rect = canvas.create_rectangle(start_x, start_y, start_x, start_y, outline="red", width=2, dash=(4, 2))

def on_drag(event):
    global rect, start_x, start_y, canvas
    total_height = canvas.bbox("all")[3]
    start_frac, _ = canvas.yview()
    visible_top_y = start_frac * total_height
    canvas.coords(rect, start_x, start_y, event.x, event.y + visible_top_y)

def on_release(event):
    global rect, start_x, start_y, rect_coords
    total_height = canvas.bbox("all")[3]
    start_frac, _ = canvas.yview()
    visible_top_y = start_frac * total_height
    rect_coords = (start_x, start_y, event.x, event.y + visible_top_y)
    ask_for_answer()

def ask_for_answer():
    correct_answer = simpledialog.askstring("Answer", "Enter the correct answer:")
    if correct_answer:
        save_question_data(correct_answer)

def save_question_data(correct_answer):
    global page_index, questions, rect_coords
    question_id = get_next_question_id()
    question_data = {
        "id": question_id,
        "page_number": page_index,
        "coords": rect_coords,
        "question": "",
        "correct_answer": correct_answer,
        "image_path": f"resources/{question_id}.png"
    }

    if not os.path.exists("resources"):
        os.makedirs("resources")

    save_selected_image(question_id)
    questions.append(question_data)

    with open("output.json", "w") as f:
        json.dump(questions, f, indent=4)
    print(f"Saved question {question_id}")

def save_selected_image(question_id):
    global img, rect_coords, canvas
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    img_width, img_height = img.size
    aspect_ratio = img_width / img_height

    if canvas_width / aspect_ratio > canvas_height:
        crop_ratio = img_width / canvas_width
    else:
        crop_ratio = img_height / canvas_height

    if rect_coords:
        left, top, right, bottom = rect_coords
        if left > right:
            left, right = right, left
        if top > bottom:
            top, bottom = bottom, top
        cropped_image = img.crop((left * crop_ratio, top * crop_ratio, right * crop_ratio, bottom * crop_ratio))
        cropped_image.save(f"resources/{question_id}.png")

def next_page():
    global total_pages, page_index
    if page_index < total_pages - 1:
        page_index += 1
        load_page(page_index)

def previous_page():
    global page_index
    if page_index > 0:
        page_index -= 1
        load_page(page_index)

def load_page(page_number):
    global img, root, canvas, doc
    if not os.path.exists("tmp"):
        os.mkdir("tmp")

    page = doc.load_page(page_number)
    pix = page.get_pixmap()
    pix.save("tmp/current.png")
    img = Image.open("tmp/current.png")
    canvas.tk_img = ImageTk.PhotoImage(img)
    update_image(root, canvas, img)

def update_image(root, canvas, img):
    root.update()
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    img_width, img_height = img.size
    aspect_ratio = img_width / img_height

    if canvas_width / aspect_ratio > canvas_height:
        new_width = canvas_width
        new_height = int(canvas_width / aspect_ratio)
    else:
        new_height = canvas_height
        new_width = int(canvas_height * aspect_ratio)

    new_width = max(1, new_width)
    new_height = max(1, new_height)

    resized_img = img.resize((new_width, new_height), Image.LANCZOS)
    canvas.tk_img = ImageTk.PhotoImage(resized_img)
    canvas.config(scrollregion=canvas.bbox("all"))
    canvas.delete("all")
    canvas.create_image(0, 0, image=canvas.tk_img, anchor="nw")

def on_resize(event):
    global root, canvas, img
    update_image(root, canvas, img)

def load_questions():
    global questions
    if not os.path.exists("output.json"):
        questions = []
    else:
        with open("output.json", "r") as f:
            questions = json.load(f)

def start(pdf):
    global root, canvas, img, doc, total_pages, page_index
    load_questions()
    canvas = tk.Canvas(width=300, height=200, bg="#dddddd")
    canvas.pack(expand=True, fill="both")

    v_scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
    v_scrollbar.pack(anchor="e", fill="y")
    canvas.config(yscrollcommand=v_scrollbar.set)

    h_scrollbar = tk.Scrollbar(canvas, orient="horizontal", command=canvas.xview)
    h_scrollbar.pack(anchor="s", fill="x")
    canvas.config(xscrollcommand=h_scrollbar.set)

    doc = fitz.open(pdf)
    total_pages = len(doc)
    page_index = 0

    load_page(page_index)

    control_panel = tk.Frame(root, bg="#f0f0f0", pady=5)
    control_panel.pack(fill="x")

    previous_button = tk.Button(control_panel, text="← Previous Page", width=15, command=previous_page)
    previous_button.pack(side="left", padx=10)

    next_button = tk.Button(control_panel, text="Next Page →", width=15, command=next_page)
    next_button.pack(side="right", padx=10)

    root.update()
    root.bind("<Configure>", on_resize)
    canvas.bind("<ButtonPress-1>", on_press)
    canvas.bind("<B1-Motion>", on_drag)
    canvas.bind("<ButtonRelease-1>", on_release)
    update_image(root, canvas, img)

def main():
    global root
    root = tk.Tk()
    root.geometry("800x600")
    root.title("QuestionSnap")

    pdf_path = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not pdf_path:
        messagebox.showinfo("No file selected", "Closing the application.")
        root.destroy()
        return

    root.title(f"QuestionSnap - {os.path.basename(pdf_path)}")
    start(pdf_path)
    root.mainloop()

if __name__ == "__main__":
    main()
