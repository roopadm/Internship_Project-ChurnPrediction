
# coding: utf-8

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn import metrics
from flask import Flask, request, render_template
import pickle


app= Flask("__name__")

df_1=pd.read_csv("new_data_telco.csv")

q = ""

@app.route("/")
def loadPage():
	return render_template('home.html', query="")


@app.route("/", methods=['POST'])
def predict():
    
    '''
       'Number_of_Referrals', 'Monthly_Charge', 'Total_Regular_Charges',
       'Total_Refunds', 'Total_Extra_Data_Charges',
       'Total_Long_Distance_Charges', 'Number_of_Dependents',
       'Referred_a_Friend', 'Phone_Service',
        'Multiple_Lines',
       'Internet_Service', 'Internet_Type',
       'Online_Security', 
       'Online_Backup',
       'Device_Protection_Plan',
       'Premium_Tech_Support', 'Streaming_TV',
       'Streaming_Movies', 'Streaming_Music',
        'Unlimited_Data',
       'Contract',
       'Paperless_Billing',
       'Payment_Method', 'Gender',
       'Under_30', 'Senior_Citizen',
       'Married', 'Dependents',
        'Tenure_in_Months'
    '''
    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']
    inputQuery5 = request.form['query5']
    inputQuery6 = request.form['query6']
    inputQuery7 = request.form['query7']
    inputQuery8 = request.form['query8']
    inputQuery9 = request.form['query9']
    inputQuery10 = request.form['query10']
    inputQuery11 = request.form['query11']
    inputQuery12 = request.form['query12']
    inputQuery13 = request.form['query13']
    inputQuery14 = request.form['query14']
    inputQuery15 = request.form['query15']
    inputQuery16 = request.form['query16']
    inputQuery17 = request.form['query17']
    inputQuery18 = request.form['query18']
    inputQuery19 = request.form['query19']
    inputQuery20 = request.form['query20']
    inputQuery21 = request.form['query21']
    inputQuery22 = request.form['query22']
    inputQuery23 = request.form['query23']
    inputQuery24 = request.form['query24']
    inputQuery25 = request.form['query25']
    inputQuery26 = request.form['query26']
    inputQuery27 = request.form['query27']
    inputQuery28 = request.form['query28']
    inputQuery29 = request.form['query29']
   
    
    model = pickle.load(open("best_model.save", "rb"))
    
    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5, inputQuery6, inputQuery7, 
             inputQuery8, inputQuery9, inputQuery10, inputQuery11, inputQuery12, inputQuery13, inputQuery14,
             inputQuery15, inputQuery16, inputQuery17, inputQuery18, inputQuery19,inputQuery20,inputQuery21,
            inputQuery22,inputQuery23,inputQuery24,inputQuery25,inputQuery26,inputQuery27,inputQuery28,inputQuery29
            ]]
    
    new_df = pd.DataFrame(data, columns = ['Number_of_Referrals', 'Monthly_Charge', 'Total_Regular_Charges',
       'Total_Refunds', 'Total_Extra_Data_Charges',
       'Total_Long_Distance_Charges', 'Number_of_Dependents',
       'Referred_a_Friend', 'Phone_Service',
        'Multiple_Lines',
       'Internet_Service', 'Internet_Type',
       'Online_Security', 
       'Online_Backup',
       'Device_Protection_Plan',
       'Premium_Tech_Support', 'Streaming_TV',
       'Streaming_Movies', 'Streaming_Music',
        'Unlimited_Data',
       'Contract',
       'Paperless_Billing',
       'Payment_Method', 'Gender',
       'Under_30', 'Senior_Citizen',
       'Married', 'Dependents',
        'Tenure_in_Months'
])
    '''
    df_2 = pd.concat([df_1, new_df], ignore_index = True) 
    # Group the tenure in bins of 12 months
    labels = ["{0} - {1}".format(i, i + 11) for i in range(1, 72, 12)]
    
    df_2['tenure_group'] = pd.cut(df_2.Tenure_in_Months.astype(float), range(1, 80, 12), right=False, labels=labels)

    #drop column customerID and tenure
    df_2.drop(columns= ['Tenure_in_Months'], axis=1, inplace=True)   
    
    '''
    
    
    new_df__dummies = pd.get_dummies(new_df[['Number_of_Referrals', 'Monthly_Charge', 'Total_Regular_Charges',
       'Total_Refunds', 'Total_Extra_Data_Charges',
       'Total_Long_Distance_Charges', 'Number_of_Dependents',
       'Referred_a_Friend', 'Phone_Service',
        'Multiple_Lines',
       'Internet_Service', 'Internet_Type',
       'Online_Security', 
       'Online_Backup',
       'Device_Protection_Plan',
       'Premium_Tech_Support', 'Streaming_TV',
       'Streaming_Movies', 'Streaming_Music',
        'Unlimited_Data',
       'Contract',
       'Paperless_Billing',
       'Payment_Method', 'Gender',
       'Under_30', 'Senior_Citizen',
       'Married', 'Dependents',
        'Tenure_in_Months']])
    
    
    #final_df=pd.concat([new_df__dummies, new_dummy], axis=1)
        
    
    single = model.predict(new_df__dummies.tail(1))
    probablity = model.predict_proba(new_df__dummies.tail(1))[:,1]
    
    if single==1:
        o1 = "This customer is likely to be churned!!"
        o2 = "Confidence: {}".format(probablity*100)
    else:
        o1 = "This customer is likely to continue!!"
        o2 = "Confidence: {}".format(probablity*100)
        
    return render_template('home.html', output1=o1, output2=o2, 
                           query1 = request.form['query1'], 
                           query2 = request.form['query2'],
                           query3 = request.form['query3'],
                           query4 = request.form['query4'],
                           query5 = request.form['query5'], 
                           query6 = request.form['query6'], 
                           query7 = request.form['query7'], 
                           query8 = request.form['query8'], 
                           query9 = request.form['query9'], 
                           query10 = request.form['query10'], 
                           query11 = request.form['query11'], 
                           query12 = request.form['query12'], 
                           query13 = request.form['query13'], 
                           query14 = request.form['query14'], 
                           query15 = request.form['query15'], 
                           query16 = request.form['query16'], 
                           query17 = request.form['query17'],
                           query18 = request.form['query18'], 
                           query19 = request.form['query19'],
                           query20 = request.form['query20'],
                           query21 = request.form['query21'],
                           query22 = request.form['query22'],
                           query23 = request.form['query23'],
                           query24 = request.form['query24'],
                           query25 = request.form['query25'],
                           query26 = request.form['query26'],
                           query27 = request.form['query27'],
                           query28 = request.form['query28'],
                           query29 = request.form['query29']
                          )
    
app.run(host='0.0.0.0', port=5000, debug=True)


