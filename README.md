# PDF Cropping Automation Script

## Overview
This Python script automates the process of cropping PDF files, specifically designed to crop the bottom portion of PDF pages. It was developed to streamline the daily task of cropping Meesho labels, a task I previously performed manually. By automating this repetitive work, the script saves time and increases efficiency.

## Features
- **Batch Processing**: The script allows for the cropping of multiple PDF files at once.
- **User-Friendly Interface**: It uses `tkinter` to provide a simple graphical user interface (GUI) to select the folder containing PDFs and input the crop size.
- **Customizable Crop Size**: The user can specify the number of inches to crop from the bottom of each PDF page.
- **Output Folder Creation**: The script creates a new folder on the desktop to store the cropped PDFs, organized by the current date.

## How It Works
1. **Select PDF Folder**: The user selects a folder containing the PDF files they wish to crop.
2. **Enter Crop Size**: The user specifies the number of inches to crop from the bottom of each page (default is 5.850 inches).
3. **PDF Cropping**: The script reads each PDF, modifies the page’s media box to crop the bottom, and saves the modified files to a new folder on the desktop.
4. **Output**: The script outputs the cropped PDFs in a folder named `Cropped_PDFs_YYYY-MM-DD`, where the date is the current day.

## Requirements
- Python 3.x
- `PyPDF2` library
- `tkinter` (comes with standard Python installation)

## How to Run
1. Clone the repository or download the script.
2. Install the required libraries if they are not already installed:
   ```bash
   pip install PyPDF2
