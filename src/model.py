
import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

model = joblib.load(BASE_DIR / "linear_regression_model.pkl")
features = joblib.load(BASE_DIR / "model_features.pkl")


def predict_score(student_data):
    student_df = pd.DataFrame([student_data])

    student_df = pd.get_dummies(student_df)

    student_df = student_df.reindex(
        columns=features,
        fill_value=0
    )

    prediction = model.predict(student_df)

    return round(prediction[0], 2)
