## Naive Bayes Classifier

**P1_data Dataset Description:** Optical Recognition of Handwritten Digits Dataset from the *UCI repository*. The original dataset consists of normalized bitmaps of handwritten digits (0 − 9). 32x32 bitmaps are divided into non-overlapping blocks of 4x4 and the number of ON pixels are counted in each block. This generates an input matrix of 8x8 where each element is an integer in the range 0 − 16. This reduces dimensionality and gives invariance to small distortions.
The given dataset is a modified version of the above dataset, consisting of the data corresponding to the handwritten digits 5 & 6 extracted from the original dataset.
1. Training data: 'P1 data train.csv' consisting of 777 instances(rows) of 64 attributes(cols) corresponding to the handwritten digit value(5 or 6) given in 'P1 labels train.csv'.
2. Test data: 'P1 data test.csv' consisting of 333 instances(rows) of 64 attributes(cols) corresponding to the handwritten digit value(5 or 6) given in 'P1 labels test.csv'.

Problem: Learn the parameters μ5, μ6, 􏰂5, 􏰂6 and π by maximizing the likelihood, π = Pr(r = C5) Pr(x|C5) = N(x|μ5, 􏰂5)
1 − π = Pr(r = C6) Pr(x|C6) = N(x|μ6, 􏰂6)
Use Bayes decision criterion to classify the test data. Estimate the misclassification rates of both classes and populate the 2x2 confusion matrix.

**P2_data Dataset Description:** 
1. Training data: 'P2 train.csv' consisting of 310 instances, 2 attributes +1 class label. 
2. Test data: 'P2 test.csv' consisting of 90 instances, 2 attributes +1 class label.

## Decision Trees

**P1_data Dataset Description:** Wisconsin Diagnostic Breast Cancer(WDBC) dataset from the *UCI repository*. Each row in the dataset represents a sample of biopsied tissue. The tissue for each sample is imaged and 10 characteristics of the nuclei of cells present in each image are characterized. These characteristics are: Radius, Texture, Perimeter, Area, Smoothness, Compactness, Concavity, Number of concave portions of contour, Symmetry, Fractal dimension. Each sample used in the dataset is a feature vector of length 30. The first 10 entries in this feature vector are the mean of the characteristics listed above for each image. The second 10 are the standard deviation and last 10 are the largest value of each of these characteristics present in each image.
1. Training data: 'trainX.csv' consisting of 455 samples, 30 attributes. The label associated with each sample is provided in 'trainY.csv'. A label of value 1 indicates the sample was for malignant (cancerous) tissue, 0 indicates the sample was for benign tissue. .  
2. Test data: 'testX.csv' consisting of 57 samples, 30 attributes. The label associated with each sample is provided in 'testY.csv'.

Problem: Use decision trees to classify the test data. Estimate the misclassification rates of both classes and populate the 2x2 confusion matrix.
1. Report the following: 
    - Plot of decision tree model. 
    - the total number of nodes in the tree. 
    - the total number of leaf nodes in the tree.
2. Train your binary decision tree with increasing sizes of training set, say 10%, 20%, ..., 100%. and test the trees with the test set. Make a plot to show how training and test accuracies vary with number of training samples.

**P2_data Dataset Description:** The data set is derived from a two-year usage log of a Washington, D.C. bike sharing system called Captial Bike Sharing (CBS). Bike sharing systems are variants of traditional bicycle rentals, where the process of renting and returning is heavily automated; typically, bikes can be rented at one location and returned at another without ever having to deal with a human being. The goal is to predict the daily level of bicycle rentals from environmental and seasonal variables using decision trees.

Data: 'bikes.csv' has the following attributes:
    - date: The full date, in year-month-day format.
    - season: Season of the year, 1 to 4
    - year: Year, 0=2011, 1=2012
    - month: Month (1 to 12)
    - holiday: Whether the day is holiday or not
    - weekday: Day of the week (coded by 0-6)
    - workingday: 1 for working days, 0 for weekends and holidays
    - weather: Weather, coded as follows:
        + Clear to partly cloudy
        + Mist but no heavier precipitation
        + Light rain or snow, possibly with thunder 4. Heavy rain or snow
    - temp: Normalized temperature in Celsius. The values are derived via (t − tmin)/(tmax − tmin); tmin = −8, tmax = +39.
    - humidity: Normalized humidity ( actual humidity divided by 100 ).
    - windspeed: Normalized wind speed ( actual wind speed in miles per hour divided by 67 ).
    - count: Count of total bike rentals that day, including both casual and registered users.
****The response variable of interest is count, the total number of rentals each day.****

Problem: Build a regression tree predicting daily bike rentals from all available variables.
1. Report the following: (a) Plot of regression tree 
    - The total number of leaf nodes in the tree
    - Into how many different groups of days does the tree divide the data 
    - Which variables appear in the tree, (e) Which variables are important, (f) The MSE.
2. Now re-code the months so that January and February share one code, May through October shares another, and March, April, November and December share a third. Re-estimate the regression tree. How does the tree change (if at all)? What is the MSE? Did it improve the fit?


## Dependencies:

- pip
- jupyter
- scikit-learn
- pandas
- graphviz

## Run the script:

- Create a virtual environment by a method of your choice.
MacOS: pyvenv
Ubuntu: venv
- `pip3 install numpy`
- `pip3 install scikit-learn`
- `pip3 install pandas`
- `pip3 install graphviz`
- `jupyter notebook`
- Run the code in your browser.
  + *Bayes_Class.ipynb* for first dataset of Bayes Classifier
  + *Bayes_Contour.ipynb* for second dataset of Bayes Classifier

  + *Question1.ipynb* for first dataset of Decision Trees
  + *Question2.ipynb* for second dataset of Decision Trees