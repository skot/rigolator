import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import socket
import time
import threading
import io

class RigolScopeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rigolator")

        self.ip_label = tk.Label(root, text="IP Address:")
        self.ip_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.ip_entry = tk.Entry(root)
        self.ip_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.get_screenshot_button = tk.Button(root, text="Get Screenshot", command=self.get_screenshot)
        self.get_screenshot_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        self.image_label = tk.Label(root)
        self.image_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        self.progress = ttk.Progressbar(root, mode='indeterminate')
        self.progress.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def get_screenshot(self):
        ip_address = self.ip_entry.get()
        
        if not ip_address:
            messagebox.showerror("Error", "IP Address cannot be empty")
            return
        
        self.progress.start()
        threading.Thread(target=self.capture_and_display, args=(ip_address,)).start()

    def capture_and_display(self, ip_address):
        image_data = self.capture_screenshot(ip_address, 5555)
        if image_data:
            self.display_image(image_data)
        self.progress.stop()

    def capture_screenshot(self, ip, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            
            s.send(b':DISP:DATA?\n')
            time.sleep(1)
            
            header = s.recv(11)
            if header[0] != ord('#'):
                raise ValueError("Invalid header received")
            
            length_digits = int(header[1:2].decode())
            data_length = int(header[2:2 + length_digits].decode())
            
            data = b''
            while len(data) < data_length:
                part = s.recv(4096)
                data += part
            
            s.close()
            return data
        except Exception as e:
            messagebox.showerror("Error", f"Failed to capture screenshot: {e}")
            return None

    def display_image(self, image_data):
        try:
            image = Image.open(io.BytesIO(image_data))
            photo = ImageTk.PhotoImage(image)
            
            self.image_label.config(image=photo)
            self.image_label.image = photo
        except Exception as e:
            messagebox.showerror("Error", f"Failed to display image: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RigolScopeApp(root)
    root.mainloop()