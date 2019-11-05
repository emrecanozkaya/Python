
import numpy as np
import pandas as pd


dataframe = pd.read_csv('Plaza_Coffee.csv', sep=";")


Company_column_data = dataframe.iloc[:,0]
Order_column_data = dataframe.iloc[:,0]
Quantity_column_data = dataframe.iloc[:,0]
Payment_column_data = dataframe.iloc[:,0]


KPMG_data = dataframe[dataframe.Company == "KPMG"]
EY_data = dataframe[dataframe.Company == "EY"]
DT_data = dataframe[dataframe.Company == "Deloite & Touche"]
PWC_data = dataframe[dataframe.Company == "PWC"]


DT_cash_data = DT_data[(DT_data.Payment == "Cash")]
DT_cash_buyer_number = 0 
    
for i in DT_cash_data.Quantity:
    DT_cash_buyer_number += i

    
DT_credit_data = DT_data[(DT_data.Payment == "Credit")]
DT_credit_buyer_number = 0

for i in DT_credit_data.Quantity:
        DT_credit_buyer_number += i
 

KPMG_cash_data = KPMG_data[(KPMG_data.Payment == "Cash")]
KPMG_cash_buyer_number = 0
   
for i in KPMG_cash_data.Quantity:
    KPMG_cash_buyer_number += i

  
KPMG_credit_data = KPMG_data[(KPMG_data.Payment == "Credit")]
KPMG_credit_buyer_number = 0

for i in KPMG_credit_data.Quantity:
        KPMG_credit_buyer_number += i
    

PWC_cash_data = PWC_data[(PWC_data.Payment == "Cash")]
PWC_cash_buyer_number = 0
   
for i in PWC_cash_data.Quantity:
    PWC_cash_buyer_number += i

  
PWC_credit_data = PWC_data[(PWC_data.Payment == "Credit")]
PWC_credit_buyer_number = 0

for i in PWC_credit_data.Quantity:
        PWC_credit_buyer_number += i
   
    

EY_cash_data = EY_data[(EY_data.Payment == "Cash")]
EY_cash_buyer_number = 0
 
for i in EY_cash_data.Quantity:
    EY_cash_buyer_number += i

    
EY_credit_data = EY_data[(EY_data.Payment == "Credit")]
EY_credit_buyer_number = 0

for i in EY_credit_data.Quantity:
        EY_credit_buyer_number += i

print("From KPMG "+str(KPMG_cash_buyer_number)+" have bought stuffs on discount and paid in cash, also assistants got "+str(KPMG_credit_buyer_number)+" servings of coffee on credit.")
print("From PWC "+str(PWC_cash_buyer_number)+" have bought stuffs on discount and paid in cash, also assistants got "+str(PWC_credit_buyer_number)+" servings of coffee on credit.")
print("From EY "+str(KPMG_cash_buyer_number)+" have bought stuffs on discount and paid in cash, also assistants got "+str(EY_credit_buyer_number)+" servings of coffee on credit.")
print("From Deloite & Touche "+str(DT_cash_buyer_number)+" have bought stuffs on discount and paid in cash, also assistants got "+str(DT_credit_buyer_number)+" servings of coffee on credit.")




