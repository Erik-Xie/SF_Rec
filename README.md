# San Francisco Commercial Site Recommendation

## Overview
This project provides a recommendation system to suggest the top 4 potential ZIP codes in San Francisco for commercial site locations based on user preferences. The system leverages **K-Nearest Neighbors (KNN)** and **Knowledge Graph with Random Walk** models to predict the most suitable locations for businesses. Users input their preferences (e.g., expected price, max tax liability, preferred population, etc.), and the system returns the most promising ZIP codes for their commercial type.

## Features
- **User Preferences**: Allows users to input specific preferences like:
  - Expected Price
  - Max Tax Liability
  - Preferred Population
  - Minimum Businesses Number
  - Preferred Adjusted Gross Income (AGI)
  
- **Recommendation Model**:
  - **K-Nearest Neighbors (KNN)**: A machine learning algorithm to find the nearest neighbors based on user inputs and historical data.
  - **Knowledge Graph with Random Walk**: Uses a graph-based model to analyze and predict successful locations by traversing relationships between various commercial and demographic factors.
  
- **Top 4 Recommendations**: Based on the input preferences, the system outputs the top 4 ZIP codes that match the user’s criteria.
  
- **ZIP Code Map**: Displays the geographical locations of the recommended ZIP codes on a map for easy visualization.

## Project Structure
    /SF_REC/
    ├── app
    │   ├── __pycache__
    │   ├── routes
    │   │   ├── __pycache__
    │   │   ├── __init__.py
    │   │   ├── about.py
    │   │   ├── feature.py
    │   │   ├── home.py
    │   │   └── recommendation.py
    │   ├── static
    │   │   ├── pics
    │   │   └── videos
    │   └── templates
    │       ├── about.html
    │       ├── base.html
    │       ├── feature.html
    │       ├── home.html
    │       └── recommendation.html
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── requirements.txt
    └── run.py



### Directory Breakdown:
- **app**: Contains the main application code.
  - **routes**: Python files responsible for the application's routes (e.g., `/home`, `/about`, `/recommendation`).
  - **static**: Static files like images and videos used in the project.
  - **templates**: HTML templates for the web pages of the project (e.g., `home.html`, `recommendation.html`).
  
- **run.py**: The main file that runs the Flask application.
- **requirements.txt**: A list of dependencies required to run the project.
- **LICENSE**: License file for the project.
- **README.md**: This file.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Erik-Xie/SF_Rec.git

2. Navigate to the project folder:
   ```bash
   cd SF_Rec

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
5. Run the application:
   ```bash
   python run.py
The application should now be running at http://127.0.0.1:5000.

You can also see at https://sf-rec.onrender.com.

## Requirements

- Python 3.x

- Flask

- Pandas

- Scikit-learn (for KNN)

- NetworkX (for Knowledge Graph)

- Additional libraries specified in requirements.txt

## Usage
1. Visit the homepage to input user preferences for commercial site recommendations.

2. The system will process the inputs and use KNN and Knowledge Graph with Random Walk models to generate the top 4 recommended ZIP codes.

3. The recommended ZIP codes will be displayed along with a map showing their geographical locations.

## Contributing
Feel free to fork this project and submit pull requests. Please make sure to follow the existing code style and include tests for any new features.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


Now you can simply copy and paste this into your `README.md` file. Let me know if you need any other changes or adjustments!
