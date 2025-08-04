🐶 Dog Breed Classification using CNN & Flask

This project uses a Convolutional Neural Network (CNN) to classify dog breeds based on input images. The model is trained in a Jupyter Notebook and deployed using a **Flask-based web UI** developed in PyCharm.

🚀 Project Workflow


🔬 Model Training (Jupyter Notebook)
•	Image dataset is preprocessed (resized, normalized, labeled).
•	A CNN model is built and trained using Keras with TensorFlow backend.
•	The trained model is saved as `.h5` for deployment.

🌐 Web UI Deployment (Flask in PyCharm)
•	A simple Flask web app allows users to upload dog images.
•	The uploaded image is passed through the trained model (`model.h5`).
•	The predicted dog breed is shown in the browser.

🧠 Technologies Used

📦 Libraries
•	`TensorFlow` / `Keras` – CNN model building & training
•	`NumPy`, `Pandas` – Data handling
•	`Matplotlib`, `Seaborn` – Visualization
•	`Flask` – Web framework for deployment
•	`OpenCV` or `PIL` – Image handling

🛠 Tools
•	Jupyter Notebook – Model development
•	PyCharm – Flask UI development

