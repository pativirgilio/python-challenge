import os
csvpath = os.path.join('pyboss1.csv')


import csv
from datetime import datetime

new_employee_data = []
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


with open(csvpath, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        
        ID = row['Emp ID']
        Name = row['Name'].split()[0]
        Surname = row['Name'].split()[-1]
        newDOB = datetime.strptime(row['DOB'], '%m/%d/%Y').strftime('%d/%m/%Y')
        SSN = "*" * (len(row['SSN'])-4) + row['SSN'][-4:] 
        SSN1 = (SSN[:3]) + "-" + (SSN[4:6]) + "-" + (SSN[7:9])
        State = row['State']
        State = us_state_abbrev[State]

             
        new_employee_data.append(
           {
               "Emp ID":row['Emp ID'],
               "First Name":row['Name'].split()[0],
               "Last Name":row['Name'].split()[-1],
               "DOB":datetime.strptime(row['DOB'], '%m/%d/%Y').strftime('%d/%m/%Y'),
               "SSN": SSN1,
               "State": State

           }
       )

       
        
 # Write updated data to CSV file:
csvpath = os.path.join("output,""pyboss1.csv")       
with open(csvpath, "w", newline='') as csvfile:
    headers = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
    
    writer = csv.DictWriter(csvfile, fieldnames = headers)
    
    writer.writeheader()
    writer.writerows(new_employee_data)
    
print(new_employee_data)
