import tkinter as tk
from tkinter import filedialog
from PIL import Image


class ImageCropper:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Image Cropper")
        self.image_path = ""
        self.crop_coordinates = None
        
        self.canvas_width = 600
        self.canvas_height = 600
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()
        
        self.open_button = tk.Button(self.root, text="Open Image", command=self.open_image)
        self.open_button.pack()
        
        self.crop_button = tk.Button(self.root, text="Crop Image", command=self.crop_image)
        self.crop_button.pack()
        
        self.root.mainloop()
    
    def open_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if self.image_path:
            self.display_image()
    
    def display_image(self):
        image = Image.open(self.image_path)
        image.thumbnail((self.canvas_width, self.canvas_height))
        self.image_tk = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk)
        self.canvas.bind("<ButtonPress-1>", self.start_crop)
        self.canvas.bind("<B1-Motion>", self.draw_crop_rectangle)
        self.canvas.bind("<ButtonRelease-1>", self.end_crop)
    
    def start_crop(self, event):
        self.crop_start_x = event.x
        self.crop_start_y = event.y
    
    def draw_crop_rectangle(self, event):
        self.canvas.delete("crop_rectangle")
        self.crop_end_x = event.x
        self.crop_end_y = event.y
        self.canvas.create_rectangle(self.crop_start_x, self.crop_start_y, self.crop_end_x, self.crop_end_y,
                                     outline="red", tags="crop_rectangle")
    
    def end_crop(self, event):
        self.crop_coordinates = (self.crop_start_x, self.crop_start_y, self.crop_end_x, self.crop_end_y)
    
    def crop_image(self):
        if self.image_path and self.crop_coordinates:
            image = Image.open(self.image_path)
            cropped_image = image.crop(self.crop_coordinates)
            cropped_image.show()
        else:
            tk.messagebox.showwarning("Warning", "Please open an image and select a crop region.")

if __name__ == "__main__":
    ImageCropper()
