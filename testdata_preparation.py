"""
Prepares test data from the BookCorpus dataset for the task of Food and Event verbal and adjectival predications.
You can find the data under "data/testset_FoodEvent_BookCorpus.tsv".

The annotated data is in TSV format and you need to convert it. There are a few
sentences that only contain a punctuation "." and the other content somehow appeared
in other lines. You can remove these punctuations and you need to split the sentences
where there are two pairs of relations (because they actually belong to two sentences).

The goal is to create 4 datasets; one for each semantic type + predication (Food+verb, Food+adjective, Event+verb, ...)
For each dataset, classify each sentence using the relevant classifier and assign them a binary label based on the output of the classifier (0 or 1). 
Add the sentence as vector and the binary label to the dataset.

The output is saved in the 'data' folder and consists of a Python dictionary with
the following structure:
- 'vectors': A list of numerical vectors representing the sentences.
- 'labels': A list of binary labels corresponding to each sentence vector.

Example of the output format:
{
    'vectors': [
        [-0.48567355, -0.07828653, 0.20480159, -0.008083422, ...], 
        # Vector for the sentences
    ],
    'labels': [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, ...]  
    # Labels for the sentences
}

Steps involved:
1. Convert tsv 
2. Extract verb-obj pairs for each sentence.
3. Assign a binary label to each sentence based on whether it contains a certain predication.
4. Calculate the relation vector for each sentence. 
5. Save the resulting vectors and labels in a dictionary as a pickle file.
"""
