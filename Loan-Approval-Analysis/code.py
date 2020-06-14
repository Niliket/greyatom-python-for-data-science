# --------------
import pandas as pd
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)

#step 2
banks = bank.drop(['Loan_ID'],axis=1)
print(banks.isnull().sum())
bank_mode = banks.mode()
banks = banks.fillna(bank_mode)
print(banks.isnull().sum().values.sum())

#step 3
avg_loan_amount = banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount',aggfunc='mean')
print(round(avg_loan_amount['LoanAmount'][1],2))


#step 4
                        # & has higher precedence than ==
loan_approved_se = len(banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status'] =='Y')])
loan_approved_nse = len(banks[(banks['Self_Employed']=='No') & (banks['Loan_Status'] =='Y')])

percentage_se = round((loan_approved_se/614)*100,2)
percentage_nse = round((loan_approved_nse/614)*100,2)


#step 5
loan_term = banks[['Loan_Amount_Term']].apply(lambda x: x/12)
big_loan_term = len(loan_term[loan_term['Loan_Amount_Term']>=25])
print(big_loan_term)


#step 6
loan_groupby = banks.groupby(['Loan_Status'])
loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.mean()
print(round(mean_values.iloc[1,0], 2))


