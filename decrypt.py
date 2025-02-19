# Program for decryption:
import cv2
import os
import string
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from password_storage import PASSWORD

def decrypt():
    image_path = filedialog.askopenfilename()
    image = cv2.imread(image_path)
    
    message_length = simpledialog.askinteger("Input", "Enter the secret message length:")
    pswrd = simpledialog.askstring("Input", "Enter passcode for decryption: ")
    
    mssg = ""
    n, m, z = 0, 0, 0

    if(pswrd == PASSWORD):
        for i in range(message_length):
            mssg += chr(image[n, m, z])
            n += 1
            m += 1
            z = (z+1)%3
        messagebox.showinfo("Decryption Success", f"Decrypted message: {mssg}")
        print(f"Decrypted message: {mssg}")
    else:
        messagebox.showwarning("Error", "You are not authorized!")

#__main__
root = tk.Tk()
root.title("Decryption")
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.pack(pady=20)
root.mainloop()