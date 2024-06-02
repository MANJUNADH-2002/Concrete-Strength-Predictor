import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
data = pd.read_excel('Concrete_Data.xls') 
# Split data into features and target
X = data.iloc[:, :-1]  # All columns except the last one
y = data.iloc[:, -1]   # The last column
# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
# Evaluate model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
# Save model and scaler
joblib.dump(model, 'concrete_strength_model.pkl')
joblib.dump(scaler, 'scaler.pkl')