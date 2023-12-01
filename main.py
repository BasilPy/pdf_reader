import tkinter as tk
from tkinter import filedialog
from pdfminer.high_level import extract_text

class PDFReaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Reader")
        self.root.geometry("600x400")

        self.text_widget = tk.Text(self.root, wrap="word", width=80, height=20, state=tk.NORMAL)
        self.text_widget.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        open_button = tk.Button(self.root, text="Open PDF", command=self.open_pdf)
        open_button.grid(row=1, column=0, pady=10)

        color_button = tk.Button(self.root, text="Change Colors", command=self.open_color_window)
        color_button.grid(row=1, column=1, pady=10)

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

        if file_path:
            text_content = self.read_pdf(file_path)
            self.text_widget.delete(1.0, tk.END)  # Clear previous content
            self.text_widget.insert(tk.END, text_content)

    def read_pdf(self, file_path):
        return extract_text(file_path)

    def open_color_window(self):
        color_window = tk.Toplevel(self.root)
        color_window.title("Change Colors")

        background_label = tk.Label(color_window, text="Background Color:")
        background_label.grid(row=0, column=0, padx=10, pady=10)

        background_color_button = tk.Button(color_window, text="Choose", command=self.change_background_color)
        background_color_button.grid(row=0, column=1, padx=10, pady=10)

        text_label = tk.Label(color_window, text="Text Color:")
        text_label.grid(row=1, column=0, padx=10, pady=10)

        text_color_button = tk.Button(color_window, text="Choose", command=self.change_text_color)
        text_color_button.grid(row=1, column=1, padx=10, pady=10)

    def change_background_color(self):
        color = tk.colorchooser.askcolor()[1]
        self.text_widget.config(bg=color)

    def change_text_color(self):
        color = tk.colorchooser.askcolor()[1]
        self.text_widget.config(fg=color)


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFReaderApp(root)
    root.mainloop()
