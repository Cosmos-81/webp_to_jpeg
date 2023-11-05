import os
# import convert
import tkinter as tk
from tkinter import filedialog

# 入力フォルダを選択する
def select_input_folder():
    input_folder_path = filedialog.askdirectory()
    input_folder_entry.delete(0, tk.END)
    input_folder_entry.insert(0, input_folder_path)

# 出力フォルダを選択する
def select_output_folder():
    output_folder_path = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, output_folder_path)

# ボタン「変換開始」: 画像をPDFに変換する
def convert_images_to_pdf():

    input_folder_path = input_folder_entry.get()    # INPUT
    output_folder_path = output_folder_entry.get()  # OUTPUT

    # 空白でないかチェック
    if(input_folder_path == ""):
        write_debug("入力フォルダを指定してください。")
        return False
    if(os.path.exists(input_folder_path) == False):
        write_debug("入力フォルダが存在しません。")
        return False

    # 空白でないかチェック
    if(output_folder_path == ""):
        write_debug("出力フォルダを指定してください。")
        return False
    if(os.path.exists(output_folder_path) == False):
        write_debug("出力フォルダが存在しません。")
        return False

    write_debug("変換処理を開始します")
    write_debug(f'入力フォルダ: {input_folder_path}')
    write_debug(f'出力フォルダ: {output_folder_path}')

    # # 変換処理を実行
    # process_status = convert.image_to_pdf(input_folder_path, output_folder_path)

    # if(process_status == ""):
    #     write_debug("変換処理が完了しました。")
    # else:
    #     write_debug(f'E: {process_status}')


def write_debug(text):  
    text_box.insert(tk.END, text + "\n")
    text_box.see(tk.END)

root = tk.Tk()
root.title("jpg to pdf converter")

# 入力要素設定セクション

# ラジオボタン[jpg]or[png]
radio_var = tk.StringVar()
radio_var.set("jpg")

input_format_label = tk.Label(root, text="入力画像フォーマット:")
input_format_label.grid(row=0, column=0, padx=5, pady=5)

input_radio_button_jpg = tk.Radiobutton(root, text="jpg", variable=radio_var, value="jpg")
input_radio_button_jpg.grid(row=0, column=1, padx=5, pady=5)

input_radio_button_png = tk.Radiobutton(root, text="png", variable=radio_var, value="png")
input_radio_button_png.grid(row=0, column=2, padx=5, pady=5)

input_folder_label = tk.Label(root, text="入力フォルダ:")
input_folder_label.grid(row=1, column=0, padx=5, pady=5)

input_folder_entry = tk.Entry(root, width=50)
input_folder_entry.grid(row=1, column=1, padx=5, pady=5)

input_folder_button = tk.Button(root, text="参照", command=select_input_folder)
input_folder_button.grid(row=1, column=2, padx=5, pady=5)

# 出力要素設定セクション

# ラジオボタン[jpg]or[png]
radio_var = tk.StringVar()
radio_var.set("png")

output_format_label = tk.Label(root, text="出力フォーマット:")
output_format_label.grid(row=2, column=0, padx=5, pady=5)

output_radio_button_jpg = tk.Radiobutton(root, text="jpg", variable=radio_var, value="jpg")
output_radio_button_jpg.grid(row=2, column=1, padx=5, pady=5)

output_radio_button_png = tk.Radiobutton(root, text="png", variable=radio_var, value="png")
output_radio_button_png.grid(row=2, column=1, padx=5, pady=5)

output_radio_button_pdf = tk.Radiobutton(root, text="pdf", variable=radio_var, value="pdf")
output_radio_button_pdf.grid(row=2, column=1, padx=5, pady=5)


output_folder_label = tk.Label(root, text="出力フォルダ:")
output_folder_label.grid(row=3, column=0, padx=5, pady=5)

output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.grid(row=3, column=1, padx=5, pady=5)

output_folder_button = tk.Button(root, text="参照", command=select_output_folder)
output_folder_button.grid(row=3, column=2, padx=5, pady=5)

submit_button = tk.Button(root, text="変換開始", command=convert_images_to_pdf)
submit_button.grid(row=4, column=1, padx=5, pady=5)

text_box = tk.Text(root, height=15)
text_box.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
