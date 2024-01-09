## IPL DATA VISUALIZER

#### INTRODUCTION:
A Second Year College python mini project
The Project aims to visualize the Indian Premier League(IPL) data using Python.
The Project explores interesting and insightful data from the data of the IPL
Tournament dating back to its inaugural (2008) till the latest ever dataset
available on kaggle (2017). The Pictorial Representation of the following data
helps users get various insights regarding various fields.

1. The Number of Matches Played by different Teams.
2. The Number of Matches Played at Different Venues.
3. The number of matches Won by Different Teams.
4. The Number of Matches in each tournament.
5. The Number of matches played in different cities.

From the Visual representation, Some major Insights one can determine are:

1. The most successful team in IPL history - Team winning most number of matches is regarded as the most
   successful team

2. The oldest team - Team which has played the most number of matches is regarded as
   the oldest team

3. The progress of the IPL tournament - The increase in the number of matches being played each year
   depicts the success of the Tournament.

4. The Development of Cricket Stadiums in India.

   - The number of different stadiums at which IPL matches are played
     tells of the development of cricket stadiums in India.

5. The Fan following in a particular city

   - The number of IPL matches being played in particular city helps us
     determine which city has more cricket followers

6. The Number of Teams Participating in IPL

   - The various teams playing IPL for short term(temporarily - 2 years)
     shows that some regular teams have not played a couple of
     seasons.

7. The Most Number of Finals Played a Team - All teams play a fixed number of matches for the league stage, and
   the team qualifying plays additional playoff matches which helps us
   determine the team which has qualified frequently for playoffs and
   hence is more successful.

We use Tkinter to provide the GUI to the data visualization done by using
matplotlib with the help of numpy and panda libraries of python programming
language. We use the latest data set in csv file format available on Kaggle.com

#### INSTALLATION AND SETUP:

To run the IPL Data Visualization Project, we need to set up the required
dependencies and execute the code.

1. Pre-requisites

   - Python should be installed.

2. Install Dependencies
   - Install matplotlib and pandas using the following command in
     terminal

```python
pip install matplotlib pandas
```

3. Download the code

   - Download the IPL Visualizer Python code uploaded on Google
     Classroom.

4. Download the Dataset

   - Download the IPL Dataset “matches.csv” uploaded on Google
     Classroom. Make sure to store the code and dataset files in the
     same folder.

5. Run the Code
   - Execute the following command in terminal

```python
python3 code\_file\_name.py
```

6. Explore the GUI
   - Successful Execution of the above series of steps will result into the
     popping of GUI on the screen.

#### CLASS OVERVIEW:

The ‘IPLDataVisualizer’ class serves as the core component of the IPL Data
Visualizer project. It encapsulates the functionality for loading, processing, and
visualizing Indian Premier League (IPL) cricket match data. The primary purpose
of this class is to provide a graphical user interface (GUI) for users to explore and
analyze statistical information from IPL matches. It leverages Tkinter for GUI
development, Matplotlib for plotting, and Pandas for efficient data manipulation.
Below is an overview of the key aspects of this class:

ATTRIBUTES:

1. master : Represents the main Tkinter window or master window where the
   GUI is displayed.

2. ipl_df : Pandas DataFrame containing the IPL match data loaded from the
   matches.csv dataset file.

METHODS:

1. \_\_init\_\_(self, master) :

   - It is a constructor method that initializes the IPLDataVisualizer
     instance.
   - It sets up the master window, assigns a title, and reads the default
     IPL dataset ("matches.csv").

2. create_widgets(self) :

   - It creates the graphical user interface, including buttons for various
     data visualizations.

3. display_matches_per_season(self):

   - It displays a bar chart representing the number of matches played
     per season.

4. display_matches_per_venue(self): - It displays a horizontal bar chart depicting the number of matches
   played at each venue.

5. display_matches_per_city(self):

   - It displays a horizontal bar chart illustrating the number of matches
     played in each city.

6. display_matches_per_team(self):

   - It displays a horizontal bar chart showcasing the number of matches
     played by each team.

7. display_wins_per_team(self):
   - It displays a horizontal bar chart revealing the number of wins for
     each IPL team.

To use this class, we instantiate an object of IPLDataVisualizer by passing the
master window. The GUI can then be interacted with to explore and visualize IPL
match statistics.

#### PANDAS & NUMPY :

In the IPL Data Visualizer project, both NumPy and Pandas play crucial roles in
data manipulation and analysis. Let's see the specific roles of each library:

1. Data Loading:

   - Pandas is used to read and load the dataset from a CSV file matches.csv.
   - The dataset is stored in a Pandas DataFrame self.ipl_df which is a two-dimensional, labeled data structure with columns that can hold different types of data.

2. Data Exploration:

   - Pandas provides functionalities to explore and understand the structure of
     the dataset.
   - Methods such as value_counts() and sort_values() are used to analyze
     and count the occurrences of values in specific columns.

3. Data Transformation:
   - The melt function from Pandas is utilized to transform the DataFrame for
     specific visualizations. It reshapes the data from wide to long format.

While the primary focus of the code is on Pandas for data manipulation, NumPy is not
explicitly used in this specific code snippet. However, NumPy is often used in
conjunction with Pandas for numerical operations, mathematical computations, and
handling numerical arrays efficiently.

NumPy is employed for tasks such as

1. Mathematical Operations
2. Array Manipulation

#### GUI CONSTRUCTION:

1. Tkinter Initialization

   - The GUI construction begins with the initialization of the Tkinter main
     window (Tk()). This root window serves as the foundation for the
     entire graphical interface.

2. Button Frame

   - Buttons for initiating specific data visualizations are organized within
     a frame for a more structured layout.

3. Individual Buttons

   - Each button is created with a unique label and associated with a
     corresponding method for executing a specific data visualization.

4. Arrangement using Geometry Managers
   - Widgets are arranged within the window using geometry managers
     (e.g., pack, grid, or place)

#### BUTTON ACTIONS:

1. Matches per season

   - This button initiates the display of a bar chart illustrating the number
     of matches played per season in the Indian Premier League (IPL).
   - A bar chart is generated using Matplotlib, showcasing the count of
     matches played for each IPL season. The x-axis represents the
     seasons, and the y-axis represents the count of matches

2. Matches per Venue

   - This button triggers the visualization of a horizontal bar chart
     depicting the number of matches played at each venue.
   - The generated chart displays the count of matches played at each
     venue. The horizontal bars are colored differently for clarity, and the
     y-axis represents the venue names.

3. Matches per city

   - Clicking this button results in the display of a horizontal bar chart
     showing the distribution of matches played in each city.
   - The chart illustrates the count of matches held in each city, using
     horizontal bars. Colors differentiate between cities for improved
     readability.

4. Matches per Team

   - This button triggers the generation of a horizontal bar chart
     presenting the number of matches played by each IPL team.
   - The chart visualizes the count of matches played by each team, with
     horizontal bars. Colors are used to distinguish between teams.

5. Wins per Team
   - Clicking this button generates a horizontal bar chart showcasing the
     number of wins for each IPL team.
   - The chart displays the count of wins for each team, utilizing
     horizontal bars. Colors enhance the differentiation between teams.

#### EVENT HANDLING:

1.  Button Clicks

        a. Matches per Season

    - When the "Matches per Season" button is clicked, the
      display_matches_per_season method is triggered. This
      method generates a bar chart displaying the number of
      matches played per season.


        b. Matches per Venue
        - Clicking the "Matches per Venue" button invokes the

    display_matches_per_venue method, which produces a
    horizontal bar chart illustrating the number of matches at each
    venue.

        c. Matches per City

    - The "Matches per City" button triggers the
      display_matches_per_city method, generating a horizontal bar
      chart depicting the number of matches played in each city.


        d. Matches per Team

    - Clicking the "Matches per Team" button executes the
      display_matches_per_team method, creating a horizontal bar
      chart presenting the number of matches played by each team.


        e. Wins per Team

    - The "Wins per Team" button invokes the display_wins_per_team method, generating a horizontal bar chart displaying the number of wins per team.

#### CONCLUSION:

The IPL Data Visualizer project successfully accomplishes its primary goal of
providing a user-friendly tool for exploring and analyzing Indian Premier League
(IPL) match statistics. The integration of Tkinter, Matplotlib, and Pandas
facilitates a seamless user experience, allowing users to interactively visualize
various aspects of IPL data.

KEY ACHIEVEMENTS:

1. User-Friendly Interface
2. Diverse Data Visualization
3. Modular and Readable Code
4. Embedded Matplotlib in Tkinter

FUTURE DIRECTIONS:

1. Enhance the GUI by adding more functionalities
2. Advanced Filtering and Providing More Insightful Visualizations
3. Update Dataset whenever latest Dataset is available.

The IPL Data Visualizer project not only serves as a practical tool for IPL
enthusiasts but also stands as a learning resource for Python developers
interested in GUI development and data visualization.
