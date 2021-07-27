import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def marks_prediction(hrs):
    data = pd.read_csv("data_student.csv")

    imputingvals = data[(data.student_marks >= 75.39)  & (data.student_marks <= 78.68) & data.study_hours.notnull()]
    imputingvals = imputingvals.study_hours.mean()
    data.study_hours = data.study_hours.fillna(6.79)

    y = data.drop(columns = 'study_hours')
    X = data.drop(columns = 'student_marks')

    X = X.values
    y = y.values

    model = LinearRegression()
    model.fit(X, y)

    X_test = np.array(hrs)
    X_test = X_test.reshape((1, -1))

    return model.predict(X_test)

