import tkinter as tk
from tkinter import ttk, filedialog
import matplotlib.pyplot as plt
import pandas as pd

class IPLDataVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("IPL Data Visualizer")

        # Read the dataset
        self.ipl_df = pd.read_csv("matches.csv")

     
        # Create GUI widgets
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for buttons
        button_frame = ttk.Frame(self.master)
        button_frame.pack(pady=10)

        # Button to display No of matches played per season
        matches_per_season_button = ttk.Button(button_frame, text="Matches per Season",
                                               command=self.display_matches_per_season)
        matches_per_season_button.grid(row=0, column=0, padx=5)

        # Button to display No of matches at each Venue
        matches_per_venue_button = ttk.Button(button_frame, text="Matches per Venue",
                                              command=self.display_matches_per_venue)
        matches_per_venue_button.grid(row=0, column=1, padx=5)

        # Button to display No of matches Played at each city
        matches_per_city_button = ttk.Button(button_frame, text="Matches per City",
                                             command=self.display_matches_per_city)
        matches_per_city_button.grid(row=0, column=2, padx=5)

        # Button to display No of matches played by each team
        matches_per_team_button = ttk.Button(button_frame, text="Matches per Team",
                                             command=self.display_matches_per_team)
        matches_per_team_button.grid(row=0, column=3, padx=5)

        # Button to display Number of wins per team
        wins_per_team_button = ttk.Button(button_frame, text="Wins per Team",
                                          command=self.display_wins_per_team)
        wins_per_team_button.grid(row=0, column=4, padx=5)

    def open_dataset(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.ipl_df = pd.read_csv(file_path)

    def display_matches_per_season(self):
        plt.figure(figsize=(12, 6))
        self.ipl_df['season'].value_counts().sort_index().plot(kind='bar', color='skyblue')
        plt.title("No of matches played per season")
        plt.xlabel("Season")
        plt.ylabel("Count")
        plt.xticks(rotation='vertical')
        plt.grid(True)
        plt.show()

    def display_matches_per_venue(self):
        plt.figure(figsize=(12, 6))
        self.ipl_df['venue'].value_counts().sort_values().plot(kind='barh', color='lightcoral')
        plt.title("No of matches at each Venue")
        plt.xlabel("Count")
        plt.ylabel("Venue")
        plt.grid(True)
        plt.show()

    def display_matches_per_city(self):
        plt.figure(figsize=(12, 6))
        self.ipl_df['city'].value_counts().sort_values().plot(kind='barh', color='lightgreen')
        plt.title("No of matches Played at each city")
        plt.xlabel("Count")
        plt.ylabel("City")
        plt.grid(True)
        plt.show()

    def display_matches_per_team(self):
        plt.figure(figsize=(12, 6))
        ipl_temp_df = pd.melt(self.ipl_df, id_vars=['id', 'season'], value_vars=['team1', 'team2'])
        ipl_temp_df['value'].value_counts().sort_values().plot(kind='barh', color='gold')
        plt.title("No of matches played by each team")
        plt.xlabel("Count")
        plt.ylabel("Team")
        plt.grid(True)
        plt.show()

    def display_wins_per_team(self):
        plt.figure(figsize=(12, 6))
        self.ipl_df['winner'].value_counts().sort_values().plot(kind='barh', color='lightblue')
        plt.title("Number of wins per team")
        plt.xlabel("Count")
        plt.ylabel("Team")
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = IPLDataVisualizer(root)
    root.mainloop()

    





 