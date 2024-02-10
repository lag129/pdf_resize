import ctypes
import os
import subprocess
import tkinter as tk
from tkinter import filedialog

def compress_pdf(input_file_path, output_file_path, quality):
    gs_command = f'gswin64c -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/{quality} -dNOPAUSE -dQUIET -dBATCH -sOutputFile={output_file_path} {input_file_path}'
    subprocess.call(gs_command, shell=True)

def open_file_dialog():
    filepath = filedialog.askopenfilename()
    return filepath

def open_file_name():
    filename = os.path.basename(open_file_dialog)
    return filename

def save_file_dialog():
    filepath = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile=open_file_name)
    return filepath

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
root = tk.Tk()
root.withdraw()  # Hide the main window

# 入力PDFファイルのパス
input_file_path = open_file_dialog()

# 出力PDFファイルのパス
output_file_path = save_file_dialog()

# PDFの品質（'screen', 'ebook', 'printer', 'prepress', 'default'のいずれか）
quality = 'ebook'

# PDFファイルを圧縮
compress_pdf(input_file_path, output_file_path, quality)