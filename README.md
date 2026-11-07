
# Student Performance Analysis and Prediction System

## Project Overview
The Student Performance Analysis and Prediction System is a Machine Learning project that analyzes students' academic data and predicts their final examination scores using Linear Regression.

The project uses Python, Pandas, NumPy, Matplotlib, Seaborn and Scikit-learn for data processing, visualization and model development.

## Objectives
- Analyze student academic performance.
- Identify factors affecting final examination scores.
- Perform Exploratory Data Analysis (EDA).
- Build a Linear Regression prediction model.
- Evaluate model performance using MAE, RMSE and R2 Score.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

## Dataset
The dataset contains 1000 student records and 12 columns, including:
- Study Time Hours
- Attendance Percentage
- Previous Grade
- Final Exam Score
- Final Grade
- Gender
- Parental Education
- Internet Access
- Extracurricular Activities
- Sleep Hours
- Part-Time Job

## Project Workflow
1. Data Collection
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis
4. Feature Engineering
5. Train-Test Split
6. Linear Regression Model Training
7. Model Evaluation
8. Prediction and Model Saving

## Model Performance

| Metric | Result |
|---|---:|
| MAE | 4.9846 |
| RMSE | 6.4157 |
| R2 Score | 0.6176 |

## Project Structure
```text
Student_Performance_Analysis/
├── data/
├── notebooks/
├── src/
│   ├── model.py
│   ├── linear_regression_model.pkl
│   └── model_features.pkl
├── outputs/
│   ├── evaluation_results/
│   └── visualizations/
├── screenshots/
├── Project_Report.pdf
├── README.md
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Jupyter Notebook:

```bash
jupyter notebook
```

## Model Usage

The trained model is saved using Joblib and can be loaded through `src/model.py`.

## Results
The Linear Regression model achieved an R2 score of approximately 0.6176 on the test dataset.

## Future Improvements
- Experiment with additional regression algorithms.
- Improve model accuracy through hyperparameter tuning.
- Develop an interactive web application.
- Add more student performance features.

## Author
Student Performance Analysis Project

## License
This project is developed for educational purposes.
