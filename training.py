import pickle
import numpy as np
from sklearn import svm
import pickle
from sklearn.metrics import precision_recall_fscore_support


"""
Self-training loop for a Support Vector Machine (SVM) 
classifier to improve its performance. The script follows these steps:

1. Define a function to test and evaluate the classifier using precision, recall, 
and F1 score.
2. Load training and test datasets from pickle files.
3. Train an initial SVM classifier using the original T-PAS training data.
4. Test the classifier on the original test set from T-PAS (English) and 
an additional test set (ACL).
5. Perform self-training by iterating over a corpus, predicting probabilities, 
and selectively 
   adding high-confidence predictions to the training data.
6. Retrain the classifier with the expanded training set.
7. Re-evaluate the classifier on both test sets.
8. Implement stopping criteria for the self-training loop and save the best performing 
classifier.

"""


def test_classifier(clf, test_data):
    """Evaluates the given classifier on the provided test data."""
    predicted_labels = clf.predict(test_data["vectors"])
    true_labels = test_data["labels"]
    scores = precision_recall_fscore_support(
        true_labels, predicted_labels, average="binary"
    )
    print(f"F1: {scores[2]}, Precision: {scores[0]}, Recall: {scores[1]}")


probability = 0.9
predication_type = "Information"

# Load Data
with open(f"data/{predication_type}_TPAS.pickle", "rb") as data_file:
    TPAS_train = pickle.load(data_file)["train"]
with open(f"data/{predication_type}_test_EN.pickle", "rb") as data_file:
    TPAS_test = pickle.load(data_file)
ACL_test = ...  # load the test data
ACL_corpus = ...  # load the ACL corpus

# Training a classifier with the original data (T-PAS)
clf = svm.SVC(gamma=0.001, C=100.0, probability=True)
clf.fit(TPAS_train["vectors"], TPAS_train["labels"])

# Test the classifier on the original test set
test_classifier(clf, TPAS_test)

# Test the classifier on ACL test set
test_classifier(clf, ACL_test)

# Self-training loop starts here. Turn this to a loop:

# Apply the classifier to ACL corpus and check the classifier probability and select the sentences based on that
for sentence in ACL_corpus:
    relation_vector = ...  # get the relation vector for each sentence
    y_pred_verb = clf.predict_proba(
        np.asarray(relation_vector, "float64").reshape(1, -1)
    )
    if y_pred_verb[0][1] > probability:  # positives
        # Edit Here
        ...
    elif y_pred_verb[0][0] > probability:  # negatives
        # Edit Here
        ...

# Add new sentences to the original dataset and train a new classifier
# Edit Here

# Test the classifier on the original test set
test_classifier(new_clf, TPAS_test)

# Test the classifier on ACL test set
test_classifier(new_clf, ACL_test)

# Check if we should stop the self-training loop and save the best classifier
# Edit Here
