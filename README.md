# Big Data Visualization Dashboard

This project is a simple yet scalable big data visualization dashboard built using Python, Dash, and Plotly. It uses a public dataset to demonstrate interactive visualizations for exploring and analyzing large datasets.

## Features

- Displays top 20 countries based on selected metrics (e.g., total cases, total deaths, cases per million).
- Interactive dropdown to select visualization metrics.
- Dynamic and responsive bar charts using Plotly.

## Technologies Used

- **Python**: Data processing and server-side scripting.
- **Dash**: Web framework for building interactive web applications.
- **Plotly**: High-quality data visualization.
- **Pandas**: Data manipulation and preprocessing.

## Dataset

The project uses the [OWID COVID-19 Dataset](https://github.com/owid/covid-19-data) as an example. The dataset is fetched directly from a public URL:
```
https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv
```
You can replace this URL with any other dataset for similar visualizations.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/big-data-visualization-dashboard.git
   cd big-data-visualization-dashboard
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
http://127.0.0.1:8050
   ```


