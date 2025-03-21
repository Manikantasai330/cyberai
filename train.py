import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

data = pd.read_csv("dataset/processed_train.csv")
X, y = data.iloc[:, :-1], data.iloc[:, -1]

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

joblib.dump(model, "model/intrusion_model.pkl")
print("Model saved successfully!")
