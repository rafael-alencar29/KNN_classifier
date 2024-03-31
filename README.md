# KNN_classifier

K-Nearest Neighbor Classifier with cosine distance and euclidean distance.

The steps necessary to run the Jupiter Notebook file:

- Create virtual environment: python -m venv <"name">
- pip install -r requirements.txt
- Create Jupyter Kernel:
  - python -m ipykernel install --user --name=<"kernel name"> --display-name=<"name">

After running the Jupyter Notebook file the following files will be generated:

- Classification report of the KNN model using cosine distance.
- Classification report of the KNN model using euclidean distance.
- Report with the top K and AUC score.
- ROC curve graph in png format.
