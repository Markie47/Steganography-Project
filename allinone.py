# Program for both encryption and decryption
import cv2
import os
import string
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def stego():
    image_path = filedialog.askopenfilename()
    image = cv2.imread(image_path)
    
    message = simpledialog.askstring("Input", "Enter secret message: ")
    password = simpledialog.askstring("Input", "Enter passcode for encryption: ")
    
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
    
    mssg = ""
    n, m, z = 0, 0, 0
    
    pswrd = simpledialog.askstring("Input", "Enter passcode for decryption: ")
    if password == pswrd:
        for i in range(len(message)):
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
root.title("Steganogrphy")
button = tk.Button(root, text="Start", command=stego)
button.pack(pady=20)
root.mainloop()