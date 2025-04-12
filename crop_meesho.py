import os
import PyPDF2

from datetime import datetime
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def crop_pdf(input_folder, output_folder, crop_bottom_inches):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace(".pdf", "_cropped.pdf"))

            with open(input_path, "rb") as infile:
                reader = PyPDF2.PdfReader(infile)
                writer = PyPDF2.PdfWriter()

                for page in reader.pages:
                    media_box = page.mediabox
                    crop_amount = crop_bottom_inches * 72  # Convert inches to points (1 inch = 72 points)
                    page.mediabox.lower_left = (media_box.lower_left[0], media_box.lower_left[1] + crop_amount)
                    writer.add_page(page)

                with open(output_path, "wb") as outfile:
                    writer.write(outfile)

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask user to select the folder containing PDFs
    input_folder = filedialog.askdirectory(title="Select Folder Containing PDFs")
    if not input_folder:
        messagebox.showerror("Error", "No folder selected. Exiting...")
        return

    # Ask for crop size (default: 5.850 inches)
    crop_bottom_inches = simpledialog.askfloat("Crop Size", "Enter crop size in inches (default: 5.850):", initialvalue=5.850)
    if crop_bottom_inches is None:
        messagebox.showerror("Error", "No crop size entered. Exiting...")
        return

    # Create output folder on Desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_folder = os.path.join(desktop_path, f"Cropped_PDFs_{datetime.now().strftime('%Y-%m-%d')}")

    # Crop PDFs
    crop_pdf(input_folder, output_folder, crop_bottom_inches)

    messagebox.showinfo("Success", f"All PDFs cropped successfully!\nSaved in: {output_folder}")

if __name__ == "__main__":
    main()
