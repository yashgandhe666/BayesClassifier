import csv
import pandas as pd
import numpy as np



trainingData = 'P1_data/P1_data_train.csv'
trainingLabel = 'P1_data/P1_labels_train.csv'

dRows = []
lRows = []
# Lists with classified data
c5 = []
c6 = []
iter = 0
sample = 0

# def gaussian(matrix, x, x_mean):
# 	return np.exp(np.dot(np.dot((x - x_mean).transpose), np.linalg.inv(matrix)), x - x_mean)/(np.power(2*np.pi, 32)* np.linalg.det(matrix))

with open(trainingData, 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	for row in csvreader:
		dRows.append(row)
		sample += 1

with open(trainingLabel, 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	for row in csvreader:
		lRows.append(row)

# Converted the lists to ints
i = 0
temp = []
for y in dRows:
	temp.append([int(x) for x in y])
	i += 1

for row in lRows:
	if(row == ['5']):
		c5.append(temp[iter])
	elif(row == ['6']):
		c6.append(temp[iter])
	iter += 1

c5_mean = np.mean(c5, axis = 0)
c6_mean = np.mean(c6, axis = 0)

# cov_c5 = np.dot((c5-c5_mean).transpose(),(c5-c5_mean)) / sample

cov_c5 = np.cov(np.transpose(c5))
cov_c6 = np.cov(np.transpose(c6))
x = c5[1]
print(x)
print(c5_mean)

# print(np.exp(np.dot(np.dot((x - c5_mean).transpose), np.linalg.inv(cov_c5)), x - c5_mean)/(np.power(2*np.pi, 32)* np.linalg.det(cov_c5)))
# np.exp(np.dot(np.dot((x - c5_mean).transpose), np.linalg.inv(cov_c5)), x - c5_mean)/(np.power(2*np.pi, 32)* np.linalg.det(cov_c5))

