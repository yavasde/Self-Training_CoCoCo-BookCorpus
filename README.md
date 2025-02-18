# Self-Training_CoCoCo-BookCorpus

This project is for further training the multilingual Information verbal predication classifier that was originally trained on T-PAS. Further training will be done using self-training.


## Objective
With self-training, we aim to increase the performance of the classifiers on domain-specific data. We do that by adding domain-specific training data to the training data of the classifier. This data is extracted automatically by using the annotations provided by the original classifier on ACL data. However, we will only add the sentences to which the classifier assigns a high probability (above 0.9). Then, a new classifier will be trained on T-PAS+selected ACL sentences.

Self-Training is an iterative process. We will train a new classifier every loop and select good examples with the new classifier until we do not see any improvement in the performance or there are no good sentences left in the ACL data. 

## Performance Monitoring
The performance of the classifier will be monitored at every loop by testing its performance on the original test data but also on manually annotated ACL test data. Since the test data is also from ACL, make sure that you don’t include the test data in the training data. We will train and select good examples every loop until we do not see any improvement in the performance or there are no good sentences left. 


## Data and the Model
Our task is to increase the data of the Information verbal predication classifier. It is a binary classifier and we will add both negative and positive sentences from the ACL corpus to the training data. 1: for positive sentences (containing Information predication), 0: for negative sentences (not containing Information predication).

Testing is done in English but the training examples are both in Italian (T-PAS) and in English (ACL). We will use the multilingual RoBERTa model: xlm-roberta-base. 


# Your tasks:
- Prepare the ACL test data for testing the classifiers
- Write the (self-)training code 
- Train and test the classifier

## Important:
- Make sure that you don’t include the ACL test data in the training data.
- Make sure that you don’t include the same sentence more than once

## Report:
- the performance on the original dataset and ACL test set every loop.
- the number of sentences included in each loop



# ACL Test Data Preparation:
You can find the data under "data/testset_acl.tsv". 
1. The annotated data is in TSV format and you need to convert it. There are a few sentences that only contain a punctuation "." and the other content somehow appeared in other lines. You can remove these punctuations and you need to split the sentences where there are two pairs of relations (because they actually belong to two sentences).
2. Extract verb-obj pairs for each sentence
3. Assign a binary label to each sentence based on the annotation provided:
    - If it is Information, it is positive (1),
    - If it contains Information, as in “Event.Information”, it is positive (1),
    - If it is not Information or doesn’t contain Information, it is negative (0),
4. Calculate the relation vector for each sentence
5. Save the resulting vectors and labels in a dictionary as a pickle file.
    (More details in the code file about the format.)


# Training Steps:
1. Train a classifier on the original dataset
2. Test it on the original test set (Information_test_EN)
3. Test it on the ACL test set

## Self-Training Loop
4. Apply the trained classifiers on the ACL corpus (as previously)
5. Check the probability assigned by the classifier to each sentence
6. Select the sentences with a high probability for both negatives and positives
7. Create a new training dataset with T-PAS+new sentences
8. Train a classifier on the new dataset
9. Test on the original dataset
10. Test on the ACL test set
11. Repeat from Step 4
12. Training loop should stop:
    - the performance of the classifier starts to decrease
    - OR you can’t find sentences with a high probability
13. Save the best classifier


