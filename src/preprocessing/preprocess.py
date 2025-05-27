import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the raw dataset
df = pd.read_csv("data/heart.csv")

# Drop rows with missing values
df = df.dropna()

# Separate features and target
X = df.drop("target", axis=1)
y = df["target"]

# Normalize input features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create new DataFrame with scaled values
df_scaled = pd.DataFrame(X_scaled, columns=X.columns)
df_scaled["target"] = y.values

# Save to cleaned CSV
df_scaled.to_csv("data/heart_clean.csv", index=False)

print("Preprocessing complete. Cleaned data saved to data/heart_clean.csv")

