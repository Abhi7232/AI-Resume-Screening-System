from sklearn.tree import DecisionTreeClassifier
import numpy as np

# -----------------------------
# Dummy Training Data
# -----------------------------

X = np.array([
    [95, 90],
    [90, 85],
    [85, 80],
    [80, 75],
    [75, 70],
    [70, 65],
    [65, 60],
    [60, 55],
    [55, 50],
    [50, 45],
    [45, 40],
    [40, 35]
])

# 2 = Selected
# 1 = Shortlisted
# 0 = Rejected

y = np.array([
    2,
    2,
    2,
    2,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0
])

# -----------------------------
# Train Model
# -----------------------------

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# -----------------------------
# Prediction Function
# -----------------------------

def predict_candidate(score, match):

    prediction = model.predict([[score, match]])[0]

    if prediction == 2:
        return "Selected"

    elif prediction == 1:
        return "Shortlisted"

    else:
        return "Rejected"