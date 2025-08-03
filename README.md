# Dementia Prediction Web Application 🧠

This is a **Django-based web application** that leverages a **machine learning model** to predict whether a person is likely to be **Demented** or **Nondemented** based on various input parameters. The app integrates a **pre-trained SVM model** along with a numerical transformer, both stored as **pickle files** for efficient prediction.

---

## 🚀 Features

### ✅ **User-Friendly Interface**
- A clean, **responsive HTML form** to collect user input (e.g., age, education, brain activity scores, etc.).

### 🤖 **Machine Learning Integration**
- Uses a **SVM model** to classify whether the person is demented or nondemented.

### 🔄 **Easy Navigation**
- Django's URL routing allows users to **switch seamlessly** between the input form and the prediction results.

---

## 🔧 Technologies Used
- **Python & Django** (Web framework)
- **NumPy** (Numerical processing)
- **Scikit-Learn** (Machine learning)
- **Pickle** (Model persistence)

---

## 📊 Input Features
The model uses the following **medical and cognitive features** for prediction:

| Feature | Description |
|---------|-------------|
| **EDUC** | Years of education |
| **SES** | Socioeconomic status (1 - Middle, 2 - Middle, 3 - High, 4 - Prestige) |
| **MMSE** | Brain activity examination (Score ≤ 23 suggests dementia) |
| **CDR** | Cognitive impairment rating (0.0 - No impairment, 3 - Severe impairment) |
| **eTIV** | Estimated total intracranial volume (measured in milliliters) |
| **nWBV** | Normalized whole brain volume |
| **ASF** | Atlas Scaling Factor (Brain shape and volume reference) |

---

## 📂 Directory Structure

```
├── dementia_prediction/        # Main Django project folder
│   ├── settings.py            # Django settings
│   ├── urls.py                # URL routing
│   ├── views.py               # Handles form submission and prediction
│   ├── models.py              # Django model definitions (if applicable)
│   ├── templates/             # HTML templates for UI
│   │   ├── index.html         # User input form
│   │   ├── result.html        # Prediction results page
│   ├── static/                # CSS and JS files
│
├── requirements.txt           # Dependencies list
├── manage.py                  # Django project management file
```

---

### **2️⃣ Run the Django Server**
Start the web application:
```bash
python manage.py runserver
```
Visit **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** in your browser to access the app.

---

## 🔍 Usage
### **1️⃣ Enter Patient Data**
- Fill in details like **age, education, SES, MMSE, CDR, eTIV, nWBV, and ASF**.

### **2️⃣ Submit & Get Prediction**
- Click **Predict** to process the input through the **SVM model** and receive the **Demented / Nondemented** classification.

---

## 🧠 Machine Learning Model
- **Model Used**: **Support Vector Machine (SVM)**
- **Preprocessing**: Numerical transformations stored in `transformer.pkl`.
- **Prediction**: Model takes in preprocessed data and outputs `Demented` or `Nondemented`.

---
##  Demo Pictures
 ![image](https://github.com/user-attachments/assets/0eb2988f-cd81-4934-9250-616fa7c289bd)
![image](https://github.com/user-attachments/assets/cedd1ada-deaf-4eee-9903-44200c604452)

## 🔮 Future Enhancements
- **Deep Learning Model**: Implement **Neural Networks** for improved accuracy.
- **Better UI/UX**: Add interactive visualizations for data analysis.
- **Deployment**: Deploy to **AWS/GCP** using Docker.


