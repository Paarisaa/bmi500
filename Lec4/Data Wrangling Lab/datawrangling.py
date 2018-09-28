

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Data=pd.read_csv('./SIIM2016_Messy_Fake_EMRdata.csv')
Data_Frame = pd.DataFrame(Data)
print(Data_Frame)

#for i in range(len(Data_Frame.index)):

#STEP 14:

Data_Frame['resource'][Data_Frame['resource'].str.match('BRCTRMG')]='UMG1'
Data_Frame['resource'][Data_Frame['resource'].str.match('Mammo-2')]='CMG1'
Data_Frame['resource'][Data_Frame['resource'].str.match('XRAY')]='UCR1'
Data_Frame['resource'][Data_Frame['resource'].str.match('MAINCR')]='CCR1'
Data_Frame['resource'][Data_Frame['resource'].str.match('MRI_MAIN')]='UMR1'
Data_Frame['resource'][Data_Frame['resource'].str.match('newMRI')]='CMR1'
Data_Frame['resource'][Data_Frame['resource'].str.match('FAST_MR')]='PMR1'
Data_Frame['resource'][Data_Frame['resource'].str.match('TRCT1')]='TCT1'
Data_Frame['resource'][Data_Frame['resource'].str.match('TRCT2')]='TCT2'
Data_Frame['resource'][Data_Frame['resource'].str.match('CT_MAIN')]='UCT1'
Data_Frame['resource'][Data_Frame['resource'].str.match('newCT')]='CCT1'
Data_Frame['resource'][Data_Frame['resource'].str.match('FAST_CT')]='PCT1'

#STEPS 16 and 17:
Data_Frame['Location'] = Data_Frame['resource'].str[0]
Data_Frame['Modality'] = Data_Frame['resource'].str[1:3]

#STEP 19:
Data_Frame['arrival_time']=pd.to_datetime(Data_Frame.arrival_time)
Data_Frame['arrival_time'] = Data_Frame['arrival_time'].dt.strftime('%m/%d/%Y')

#STEP 20:
Data_Frame=Data_Frame.drop(['first_final_time','first_image_time','complete_time','patient_gender'
                ,'arrival_time','dob','id','resource'],axis=1)

#STEP 21: Histogram of procedure code column

from collections import Counter
a=Data['procedure_code']
letter_counts = Counter(a)
df = pd.DataFrame.from_dict(letter_counts, orient='index')
df.plot(kind='bar')
plt.xlabel('procedure codes')
plt.ylabel('Frequency')
plt.title('Frequency of all procedure codes')

#STEP 22:	The	most frequently	occurring	procedure	description

a=Data['procedure_description']
letter_counts = Counter(a)
Frequency=letter_counts.most_common()
print(['the most common procedure description is:',Frequency[0]])


b=Data['procedure_code']
letter_counts_code = Counter(b)
Frequency2=letter_counts_code.most_common()
print(['the most common procedure code is:',Frequency2[0]])


#sort the procedure code by its count:
sorted_procedure_code = sorted(letter_counts_code, key=letter_counts_code.get, reverse=True)


#STEP 25
Data_Frame=Data_Frame.drop(['accession','MRN','patient_name'],axis=1)


#STEP 26:Save the cleaned data to a new csv file
Data_Frame.to_csv('Cleaned_Data.csv', sep=',')











    