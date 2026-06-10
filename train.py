from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from joblib import dump

# Load dataset
data = fetch_olivetti_faces()

X = data.data
y = data.target

# 70-30 split
X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.30,random_state=42,stratify=y
)

# Training model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Save model
dump(model, "savedmodel.pth")

print("Model saved as savedmodel.pth")
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")