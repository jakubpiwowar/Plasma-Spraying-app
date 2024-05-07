import tkinter as tk
from tkinter import ttk, filedialog
from image_processing import ImageProcessor
from plotting import Plotter
from threshold_window import ThresholdWindow 

class MainApp:
    def __init__(self, root):
        self.root = root
        self.processor = ImageProcessor()  # Inicjalizacja instancji ImageProcessor
        self.threshold_window = ThresholdWindow()

        self.tab_control = ttk.Notebook(root)

        self.process_tab = ttk.Frame(self.tab_control)
        self.select_tab = ttk.Frame(self.tab_control)
        self.create_plots_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.process_tab, text="Process")
        self.tab_control.add(self.select_tab, text="Set threshold")
        self.tab_control.add(self.create_plots_tab, text="Create Plots")

        self.folder_path_label = tk.Label(self.process_tab, text="Select Folder:")
        self.folder_path_label.pack()

        self.folder_path_entry = tk.Entry(self.process_tab, width=50)
        self.folder_path_entry.pack()

        self.select_button = tk.Button(self.process_tab, text="Select", command=self.select_folder)
        self.select_button.pack()

        self.create_plots_button = tk.Button(self.process_tab, text="Create Plots", command=self.process)
        self.create_plots_button.pack()

        self.open_button = tk.Button(self.select_tab, text="Open Threshold Window", command=self.open_threshold_window)
        self.open_button.pack()

        self.folder_path_label1 = tk.Label(self.create_plots_tab, text="Select Folder 1:")
        self.folder_path_label1.pack()

        self.folder_path_entry1 = tk.Entry(self.create_plots_tab, width=50)
        self.folder_path_entry1.pack()

        self.select_button1 = tk.Button(self.create_plots_tab, text="Select", command=self.select_folder1)
        self.select_button1.pack()

        self.folder_path_label2 = tk.Label(self.create_plots_tab, text="Select Folder 2:")
        self.folder_path_label2.pack()

        self.folder_path_entry2 = tk.Entry(self.create_plots_tab, width=50)
        self.folder_path_entry2.pack()

        self.select_button2 = tk.Button(self.create_plots_tab, text="Select", command=self.select_folder2)
        self.select_button2.pack()

        self.create_plots_button = tk.Button(self.create_plots_tab, text="Create Plots", command=self.create_plots)
        self.create_plots_button.pack()

        self.tab_control.pack(expand=1, fill="both")

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_path_entry.delete(0, tk.END)
            self.folder_path_entry.insert(tk.END, folder_path)

    def select_folder1(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_path_entry1.delete(0, tk.END)
            self.folder_path_entry1.insert(tk.END, folder_path)

    def select_folder2(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_path_entry2.delete(0, tk.END)
            self.folder_path_entry2.insert(tk.END, folder_path)

    def open_threshold_window(self):
        self.threshold_window.open_window(self.tab_control)

    def process(self):
        folder_path = self.folder_path_entry.get()
        if folder_path:
            plotter = Plotter()
            ratio = self.processor.kalibracja()
            kp_list, new_zero, ex = self.processor.detekcja(folder_path, ratio, self.threshold_window.threshold_value)
            all_points = self.processor.segregacja(kp_list, ratio, new_zero, ex)
            plotter.wizualizacja(all_points, ratio, new_zero, ex)

    def create_plots(self):
        folder_path1 = self.folder_path_entry1.get()
        folder_path2 = self.folder_path_entry2.get()
        if folder_path1 and folder_path2:
            plotter = Plotter()

            # Detekcja, segregacja i wizualizacja dla pierwszego folderu
            ratio = self.processor.kalibracja()
            kp_list1, new_zero, ex = self.processor.detekcja(folder_path1, ratio, self.threshold_window.threshold_value)
            kp_list2 = self.processor.detekcja2(folder_path2, self.threshold_window.threshold_value)
            
            # Segregacja dla obu zestawów punktów
            full_points = self.processor.segregacja(kp_list1, ratio, new_zero, ex, kp_list2)
            # Wizualizacja połączonych punktów
            plotter.wizualizacja_dwukrotna(full_points, ratio, new_zero, ex)
            


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image Analysis")
    root.geometry("800x600+100+50")
    MainApp(root)
    root.mainloop()