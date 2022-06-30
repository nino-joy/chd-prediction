import csv
import pandas as pd
with open('HN14_ALL.csv', mode ='r')as file:

	df = pd.read_csv("HN14_ALL.csv", usecols = ['age','HE_chol','HE_HDL_st2','HE_sbp','HE_BMI','HE_wc','N_FAT'])
	df.to_csv('new.csv')
df2= pd.read_csv("new.csv")
df2.drop("Unnamed: 0",axis=1)
