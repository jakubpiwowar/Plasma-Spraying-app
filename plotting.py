import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.lines import Line2D
from scipy.stats import norm

class Plotter:
    def __init__(self):
        pass

    def wizualizacja(self, all_points, ratio, new_zero, ex):
        x_intervals = [(0, 5), (5, 10), (10, 15), (15, 20)]
        x_partitions = []
        for interval in x_intervals:
            x_partition = all_points[(all_points[:, 0] >= interval[0]) & (all_points[:, 0] < interval[1])]
            x_partitions.append(x_partition)

        # Tworzenie wykresu
        fig = plt.figure(figsize=(10, 30))
        gs = GridSpec(5, 4, height_ratios=[7, 2, 2, 2, 2], top=0.92)

        ax0 = fig.add_subplot(gs[0, :])
        ax0.scatter(all_points[:, 0], all_points[:, 1], s=1, alpha=0.5, label='Punkty kluczowe')
        ax0.axhline(0, color='black', linewidth=1)
        for value in range(5, 20, 5):
            ax0.axvline(value, color='gray', linestyle='--', linewidth=1)
        ax0.set_xlim(0, ex[1] * ratio)
        ax0.set_ylim(-new_zero, (ex[0] * ratio) - new_zero)
        ax0.invert_yaxis()
        ax0.set_title('Wykres punktowy punktów charakterystycznych')
        ax0.set_xlabel('Współrzędna X')
        ax0.set_ylabel('Współrzędna Y')

        legend_handles = []
        legend_labels = []

        # Tworzenie histogramów
        for i, x_partition in enumerate(x_partitions):
            ax = fig.add_subplot(gs[2, i])
            num_bins = 20
            hist, bins, _ = ax.hist(x_partition[:, 1], num_bins, orientation='horizontal', density=True)
            max_bin_index = np.argmax(hist)
            max_distribution_point = (bins[max_bin_index] + bins[max_bin_index + 1]) / 2
            ax.axhline(max_distribution_point, color='r', linestyle='--', label='Maksymalny rozkład')
            mu, sigma = np.mean(x_partition[:, 1]), np.std(x_partition[:, 1])
            x = np.linspace(min(x_partition[:, 1]), max(x_partition[:, 1]), len(hist))
            y = norm.pdf(x, mu, sigma)
            bin_centers = 0.5 * (bins[:-1] + bins[1:])
            hist_plot = ax.barh(bin_centers, hist, height=np.diff(bins), color='gray', alpha=0.5, label='Histogram')
            ax.invert_yaxis()
            ax2 = ax.twiny()
            ax2.plot(y, bin_centers, color='b', linestyle='--')
            ax.set_title(f'Part {i+1}')
            ax.set_xlabel('Rozkład cząsteczek')
            ax2.set_xlabel('Rozkład normalny')

        legend_handles.extend([hist_plot[0], Line2D([0], [0], color='r', linestyle='--'), Line2D([0], [0], color='b', linestyle='--')])
        legend_labels.extend(['Histogram', 'Maksymalny rozkład', 'Rozkład normalny'])
        handles, labels = ax0.get_legend_handles_labels()
        legend_handles.extend(handles)
        legend_labels.extend(labels)
        fig.legend(legend_handles, legend_labels, loc='upper center', bbox_to_anchor=(0.5, 0.3), ncol=3)

        plt.tight_layout()
        plt.show()

    def wizualizacja_dwukrotna(self, full_points, ratio, new_zero, ex):
        x_intervals = [(0, 5), (5, 10), (10, 15), (15, 20), (20, 25), (25, 30), (30, 35), (35, 40)]
        x_partitions = []
        for interval in x_intervals:
            x_partition = full_points[(full_points[:, 0] >= interval[0]) & (full_points[:, 0] < interval[1])]
            x_partitions.append(x_partition)

        fig = plt.figure(figsize=(18, 9))
        gs = GridSpec(5, 8, height_ratios=[7, 2, 2, 2, 2], top=0.92)

        ax0 = fig.add_subplot(gs[0, :])
        ax0.scatter(full_points[:, 0], full_points[:, 1], s=1, alpha=0.5, label='Punkty kluczowe')
        ax0.axhline(0, color='black', linewidth=1)

        for value in range(5, 40, 5):
            ax0.axvline(value, color='gray', linestyle='--', linewidth=1)
        ax0.set_xlim(0, 2 * ex[1] * ratio)
        ax0.set_ylim(-new_zero, (ex[0] * ratio) - new_zero)
        ax0.invert_yaxis()
        ax0.set_title('Wykres punktowy punktów charakterystycznych')
        ax0.set_xlabel('Współrzędna X')
        ax0.set_ylabel('Współrzędna Y')

        for i, x_partition in enumerate(x_partitions):
            ax = fig.add_subplot(gs[1, i])
            num_bins = 20
            hist, bins, _ = ax.hist(x_partition[:, 1], num_bins, orientation='horizontal', density=True)
            max_bin_index = np.argmax(hist)
            max_distribution_point = (bins[max_bin_index] + bins[max_bin_index + 1]) / 2
            ax.axhline(max_distribution_point, color='r', linestyle='--', label='Maksymalny rozkład')
            mu, sigma = np.mean(x_partition[:, 1]), np.std(x_partition[:, 1])
            x = np.linspace(min(x_partition[:, 1]), max(x_partition[:, 1]), len(hist))
            y = norm.pdf(x, mu, sigma)
            bin_centers = 0.5 * (bins[:-1] + bins[1:])
            hist_plot = ax.barh(bin_centers, hist, height=np.diff(bins), color='gray', alpha=0.5, label='Histogram')
            ax.invert_yaxis()
            ax2 = ax.twiny()
            ax2.plot(y, bin_centers, color='b', linestyle='--')
            ax.set_title(f'Part {i+1}')
            ax.set_xlabel('Rozkład cząsteczek')
            ax2.set_xlabel('Rozkład normalny')

        legend_handles = []
        legend_labels = []
        legend_handles.extend([hist_plot[0], Line2D([0], [0], color='r', linestyle='--'), Line2D([0], [0], color='b', linestyle='--')])
        legend_labels.extend(['Histogram', 'Maksymalny rozkład', 'Rozkład normalny'])
        handles, labels = ax0.get_legend_handles_labels()
        legend_handles.extend(handles)
        legend_labels.extend(labels)
        fig.legend(legend_handles, legend_labels, loc='upper center', bbox_to_anchor=(0.5, 0.3), ncol=3)

        plt.tight_layout()
        plt.show()