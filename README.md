# Naive Bayes Classifier

**P1_data Dataset Description:** Optical Recognition of Handwritten Digits Dataset from the *UCI repository*. The original dataset consists of normalized bitmaps of handwritten digits (0 − 9). 32x32 bitmaps are divided into non-overlapping blocks of 4x4 and the number of ON pixels are counted in each block. This generates an input matrix of 8x8 where each element is an integer in the range 0 − 16. This reduces dimensionality and gives invariance to small distortions.
The given dataset is a modified version of the above dataset, consisting of the data corresponding to the handwritten digits 5 & 6 extracted from the original dataset.
1. Training data: ‘ P1 data train.csv ′ consisting of 777 instances(rows) of 64 attributes(cols) corresponding to the handwritten digit value(5 or 6) given in ‘ P1 labels train.csv ′.
2. Test data: ‘ P1 data test.csv ′ consisting of 333 instances(rows) of 64 attributes(cols) cor- responding to the handwritten digit value(5 or 6) given in ‘ P1 labels test.csv '.

**P2_data Dataset Description:** 
1. Training data: ‘ P2 train.csv ′ consisting of 310 instances, 2 attributes +1 class label. 
2. Test data: ‘ P2 test.csv ′ consisting of 90 instances, 2 attributes +1 class label.

## Dependencies:

1. pip
2. jupyter

## Run the script:

1. Create a virtual environment by a method of your choice.
MacOS: pyvenv
Ubuntu: venv
2. `pip3 install numpy`
3. `jupyter notebook`
4. Run the code in your browser.
  * *Bayes_Class.ipynb* for first dataset
  * *Bayes_Contour.ipynb* for second dataset