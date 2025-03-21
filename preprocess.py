import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_data(file_path):
    df = pd.read_csv(file_path, header=None)
    encoder = LabelEncoder()
    df[1] = encoder.fit_transform(df[1])
    scaler = StandardScaler()
    df.iloc[:, :-1] = scaler.fit_transform(df.iloc[:, :-1])
    return df

if __name__ == "__main__":
    data = preprocess_data("dataset/KDDTrain+.txt")
    data.to_csv("dataset/processed_train.csv", index=False)
