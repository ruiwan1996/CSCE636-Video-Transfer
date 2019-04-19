from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk, threading
from PIL import ImageTk, Image
import imageio

class Root(Tk):

    def __init__(self):
        super(Root, self).__init__()
        self.title("Video Style Transfer")
        self.minsize(640,400)

        self.video_name = StringVar()
        self.transfered_video_name = StringVar()

        self.image_labelFrame = ttk.LabelFrame(self, text = "Select A Target Image")
        self.image_labelFrame.grid(column = 0, row = 0, padx = 20, pady = 20)
        self.image_canvas = Canvas(self, bg="white", height=200, width=250)
        self.image_canvas.grid(column=0, row=1)
        self.open_image_button()

        self.video_labelFrame = ttk.LabelFrame(self, text="Select A Source Video")
        self.video_labelFrame.grid(column=1, row=0, padx=20, pady=20)
        self.video_canvas = Canvas(self, bg="white", height=400, width=600)
        self.video_canvas.grid(column=1, row=1)
        self.open_video_button()

        #self.transfer_label = ttk.Label(self, text = "Style Transferred Video")
        #self.transfer_label.grid(column = 2, row = 0, padx = 20, pady = 20)
        transfer_canvas = Canvas(self, bg="white", height=400, width=600)
        transfer_canvas.grid(column=2, row=1, padx = 20, pady = 20)

        self.play()
        #self.pause()

    def open_image_button(self):
        self.browse_image_button = ttk.Button(self.image_labelFrame, text = "Browse A File", command = self.image_fileDialog)
        self.browse_image_button.grid(column = 1, row = 1)

    def image_fileDialog(self):
        self.image_filename = filedialog.askopenfilename(initialdir = "/", title = "Select A File", filetype = (("jpeg", "*.jpg"), ("All Files", "*.*")))
        self.label = ttk.Label(self.image_labelFrame, text = "")
        self.label.grid(column = 1, row = 2)
        self.label.configure(text = self.image_filename)

        img = Image.open(self.image_filename)
        new_img = img.resize((250, 200), Image.BILINEAR)
        self.image_canvas.image = ImageTk.PhotoImage(new_img)
        self.image_canvas.create_image(0, 0, image=self.image_canvas.image, anchor='nw')

    def open_video_button(self):
        self.browse_video_button = ttk.Button(self.video_labelFrame, text="Browse A File", command=self.video_fileDialog)
        self.browse_video_button.grid(column=1, row=1)

    def video_fileDialog(self):
        self.video_filename = filedialog.askopenfilename(initialdir="/", title="Select A File",filetype=(("avi", "*.avi"),("mp4", "*.mp4"), ("All Files", "*.*")))
        self.label = ttk.Label(self.video_labelFrame, text="")
        self.label.grid(column=1, row=2)
        self.label.configure(text=self.video_filename)
        self.video_name.set(self.video_filename)
        self.transfered_video_name.set('D:/transfered_' + self.video_filename[3:])

    def play(self):
        self.play_button = ttk.Button(self, text="PLAY", command = self.play_origin_video)
        self.play_button.grid(column = 1, row = 2, sticky=SE)

    def play_origin_video(self):

        my_label = tk.Label(self, height=400, width=600)
        my_label.grid(column=1, row=1)

        thread = threading.Thread(target=self.stream, args=(my_label,))
        thread.daemon = 1
        thread.start()

        my_label_t = tk.Label(self, height=400, width=600)
        my_label_t.grid(column=2, row=1)

        thread_t = threading.Thread(target=self.stream_t, args=(my_label_t,))
        thread_t.daemon = 1
        thread_t.start()

    def stream_t(self, label_t):
        video_t = imageio.get_reader(str(self.transfered_video_name.get()))
        for image in video_t.iter_data():
            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
            label_t.config(image=frame_image)
            label_t.image = frame_image

    def stream(self, label):
        video = imageio.get_reader(str(self.video_name.get()))
        for image in video.iter_data():
            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
            label.config(image=frame_image)
            label.image = frame_image

    def pause(self):
        self.pause_button = ttk.Button(self, text="PAUSE")
        self.pause_button.grid(column=1, row=1, sticky=SW)

if __name__ == "__main__":
    root = Root()
    root.mainloop()