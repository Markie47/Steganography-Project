# Program for encryption:
import cv2
import os
import string
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from password_storage import PASSWORD

def encrypt():
    image_path = filedialog.askopenfilename()
    image = cv2.imread(image_path)
    
    message = simpledialog.askstring("Input", "Enter secret message: ")
    
    d = {}
    c = {}
    
    for i in range(255):
        d[chr(i)] = i
        c[i] = i
    
    # m, n, z are rgb values for image respectively
    m,n,z = 0, 0, 0
    
    for i in range(len(message)):
        image[n, m, z] = d[message[i]]
        n += 1
        m += 1
        z = (z+1)%3
    
    cv2.imwrite("encryptedImage.jpg", image)
    messagebox.showinfo("Success", "Image encrypted successfully!")
    os.system("start encryptedImage.jpg")

#__main__
root = tk.Tk()
root.title("Encryption")
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack(pady=20)
root.mainloop()