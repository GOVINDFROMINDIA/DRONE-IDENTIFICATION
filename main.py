import tkinter as tk
from tkinter import filedialog
import PIL
import cv2

def choose_file():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("image files", ("*.jpg", "*.png")), ("all files", "*.*")))
    file_path = root.filename
    capture = cv2.VideoCapture(file_path)
    size = (224, 224)
    image = Image.open(file_path).convert("RGB")
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array
    #daynight(data[0])

def open_camera():
    capture = cv2.VideoCapture(0)
    ret, image = capture.read()
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    cv2.imshow("Webcam Image", image)
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    image = (image / 127.5) - 1
    #daynight(image)

root = tk.Tk()
root.title("Drone Identification")
root.geometry("800x533")
bg_image = tk.PhotoImage(file="drone.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

file_image = tk.PhotoImage(file="upload.png")
file_button = tk.Button(root, image=file_image, command=choose_file)
file_button.pack(side=tk.LEFT, pady=10, padx=(200, 20), anchor=tk.N)

camera_image = tk.PhotoImage(file="open.png")
camera_button = tk.Button(root, image=camera_image, command=open_camera)
camera_button.pack(side=tk.LEFT, pady=10, padx=(20, 200), anchor=tk.N)
root.mainloop()