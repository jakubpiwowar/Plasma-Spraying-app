import cv2
import os
import numpy as np

class ImageProcessor:
    def __init__(self):
        pass

    def kalibracja(self):
        ratio = 12.5 / 677
        return ratio

    def detekcja(self, folder_path, ratio, t=17):
        kp_list = []

        for file_name in os.listdir(folder_path):
            if file_name.lower().endswith('.bmp'):
                file_path = os.path.join(folder_path, file_name)
                img = cv2.imread(file_path, 0)

                if img is not None:
                    _, th2 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
                    contours, _ = cv2.findContours(th2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    largest_contour = max(contours, key=cv2.contourArea)
                    x, y, w, h = cv2.boundingRect(largest_contour)
                    detector = cv2.FastFeatureDetector_create(t)
                    kp = detector.detect(img, None)
                    new_zero = (y + h / 2) * ratio
                    ex = img.shape
                    kp_list.extend(kp)

        return kp_list, new_zero, ex

    def detekcja2(self, folder_path, t=17):
        kp_list2 = []

        for file_name in os.listdir(folder_path):
            if file_name.lower().endswith('.bmp'):
                file_path = os.path.join(folder_path, file_name)
                img = cv2.imread(file_path, 0)

                if img is not None:
                    detector = cv2.FastFeatureDetector_create(t)
                    kp = detector.detect(img, None)
                    kp_list2.extend(kp)

        return kp_list2

    def segregacja(self, kp_list, ratio, new_zero, ex, kp_list2=None):
        x_points = np.array([point.pt[0] for point in kp_list])
        y_points = np.array([point.pt[1] for point in kp_list])
        x_points_scaled = x_points * ratio
        y_points_scaled = (y_points * ratio) - new_zero
        all_points = np.column_stack((x_points_scaled, y_points_scaled))
        print(new_zero)
        print(ratio)

        if kp_list2 is not None:
            x_points2 = np.array([point.pt[0] for point in kp_list2])
            y_points2 = np.array([point.pt[1] for point in kp_list2])
            x_points2_scaled = (x_points2 + ex[1]-15) * ratio
            y_points2_scaled = (y_points2 * ratio) - new_zero
            all_points2 = np.column_stack((x_points2_scaled, y_points2_scaled))
            full_points = np.concatenate((all_points, all_points2))
            return full_points
        else:
            return all_points
