from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from joblib import load

# Load dataset
data = fetch_olivetti_faces()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.30,random_state=42,stratify=y
)

# Loading saved model
model = load("savedmodel.pth")

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"Test Accuracy: {accuracy:.4f}")