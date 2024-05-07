import tkinter as tk
from tkinter import filedialog
import cv2

class ThresholdWindow:
    def __init__(self):
        self.threshold_value = 17

    def open_window(self, tab_control):
        self.tab_control = tab_control
        img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if img_path:
            self.thmaker(img_path)

    def thmaker(self, img_path):
        def update_threshold(value):
            self.threshold_value = int(value)
            detector = cv2.FastFeatureDetector_create(self.threshold_value)
            kp = detector.detect(img, None)
            DET = cv2.drawKeypoints(img, kp, None, flags=0)
            cv2.imshow("choose your threshold", DET)

        def save_threshold():
            cv2.destroyAllWindows()
            root.destroy()
            self.tab_control.select(0)

        img = cv2.imread(img_path, 0)

        root = tk.Tk()
        root.title("Choose Threshold")

        threshold_label = tk.Label(root, text="Threshold:")
        threshold_label.pack()

        threshold_scale = tk.Scale(root, from_=0, to=100, orient="horizontal", length=200, command=update_threshold)
        threshold_scale.pack()

        save_button = tk.Button(root, text="Zapisz", command=save_threshold)
        save_button.pack()

        update_threshold(self.threshold_value)
        root.mainloop()