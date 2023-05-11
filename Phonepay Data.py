#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# extracting the data from github
get_ipython().system('git clone https://github.com/PhonePe/pulse.git')
------------------------------------------------------------------------------------------------------
#Required libraries for the program
import pandas as pd
import json
import os
from pandas import json_normalize
-----------------------------------------------------------------------------------------------------------

#Once created the clone of GIT-HUB repository then,
#This is to direct the path to get the data as states

path = "/content/pulse/data/aggregated/transaction/country/india/state/"
Agg_state_list = os.listdir(path)
#print(Agg_state_list)

clm={'State':[], 'Year':[],'Quater':[],'Transacion_type':[], 'Transacion_count':[], 'Transacion_amount':[]}

for i in Agg_state_list:
  path_i = path+i+"/"
  Agg_year_list = os.listdir(path_i)
  #print(Agg_year_list)
  for j in Agg_year_list:
    path_j = path_i+j+'/'
    Agg_quarter_list = os.listdir(path_j)
    #print(Agg_quarter_list)
    for k in Agg_quarter_list:
      path_k = path_j+k
      Data = open(path_k,'r')
      data =  json.load(Data)
      #print(data)
      try:
          for z in data['data']['transactionData']:
            #print(z)
            Name=z['name']
            #print(Name)
            count=z['paymentInstruments'][0]['count']
            amount=z['paymentInstruments'][0]['amount']
            clm['Transacion_type'].append(Name)
            clm['Transacion_count'].append(count)
            clm['Transacion_amount'].append(amount)
            clm['State'].append(i)
            clm['Year'].append(j)
            clm['Quater'].append(int(k.strip('.json')))
      except:
        pass 
#Succesfully created a dataframe
Agg_Trans=pd.DataFrame(clm)
# Exporting the DataFrame to csv file
Agg_Trans.to_csv('Aggregated_Transaction.csv', sep=',',index=False)
Agg_Trans
---------------------------------------------------------------------------------------------------------------------------
path="/content/pulse/data/aggregated/user/country/india/state/"
user_state_list=os.listdir(path)
#Agg_state_list--> to get the list of states in India
#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

#This is to extract the data's to create a dataframe

colm={'State':[], 'Year':[],'Quater':[],'registeredUsers':[],'appOpens':[],'user_brand':[], 'user_count':[], 'user_percentage':[]}
for i in user_state_list:
    path_i=path+i+"/"
    user_yr=os.listdir(path_i)    
    for j in user_yr:
        path_j=path_i+j+"/"
        user_yr_list=os.listdir(path_j)        
        for k in user_yr_list:
            path_k=path_j+k
            Data=open(path_k,'r')
            Da=json.load(Data)
            #print(Da)
            try:
              for z in Da['data']['usersByDevice']:
                registeredUsers =  Da['data']['aggregated']['registeredUsers']
                appOpens =  Da['data']['aggregated']['appOpens']
                brand=z['brand']
                count=z['count']
                percentage=z['percentage']
                colm['registeredUsers'].append(registeredUsers)
                colm['appOpens'].append(appOpens)
                colm['user_brand'].append(brand)
                colm['user_count'].append(count)
                colm['user_percentage'].append(percentage)
                colm['State'].append(i)
                colm['Year'].append(j)
                colm['Quater'].append(int(k.strip('.json')))  
            except:
                pass    
#Succesfully created a dataframe                
Agg_user=pd.DataFrame(colm)
# Exporting the DataFrame to csv file
Agg_user.to_csv('Aggregated_User.csv', sep=',',index=False)    
Agg_user               
------------------------------------------------------------------------------------------------------------------------------------
path = "/content/pulse/data/map/transaction/hover/country/india/state/"
map_state_list = os.listdir(path)
#print(Agg_user_state_list)

colm={'State':[], 'Year':[],'Quater':[],'District_name':[],'Transaction_count':[], 'Transaction_amount':[]}

for i in map_state_list:
  path_i = path+i+'/'
  map_year_list = os.listdir(path_i)
  #print(map_user_year_list)
  for j in map_year_list:
    path_j = path_i +j+'/'
    map_qtr_list= os.listdir(path_j)
    #print(map_qtr_list)
    for k in map_qtr_list:
      path_k = path_j+k
      Data =open(path_k,'r')
      Da=json.load(Data)
      #print(Da)
      for z in Da['data']['hoverDataList']:
        district_name = z['name']
        count = z['metric'][0]['count']
        amount= z['metric'][0]['amount']
        colm['District_name'].append(district_name)
        colm['Transaction_count'].append(count)
        colm['Transaction_amount'].append(amount)
        colm['State'].append(i)
        colm['Year'].append(j)
        colm['Quater'].append(int(k.strip('.json')))

#Succesfully created a dataframe
map_Trans=pd.DataFrame(colm)
# Exporting the DataFrame to csv file
map_Trans.to_csv('Map_Transaction.csv', sep=',',index =False) 
map_Trans     
--------------------------------------------------------------------------------------------------------------------------------
path = "/content/pulse/data/map/user/hover/country/india/state/"
map_state_list = os.listdir(path)
#print(Agg_state_list)

colu={'State':[], 'Year':[],'Quater':[],'District_name':[],'RegisteredUsers':[], 'AppOpens':[]}

for i in map_state_list:
  path_i = path+i+'/'
  map_year_list = os.listdir(path_i)
  #print(map_user_year_list)
  for j in map_year_list:
    path_j = path_i +j+'/'
    map_qtr_list= os.listdir(path_j)
    #print(map_qtr_list)
    for k in map_qtr_list:
      path_k = path_j+k
      Data =open(path_k,'r')
      Da=json.load(Data)
      #print(Da)
      try:
          for z in Da['data']['hoverData']:
            district_name = z
            RegisteredUsers =Da['data']['hoverData'][z]['registeredUsers'] 
            AppOpens = Da['data']['hoverData'][z]['appOpens']
            colu['District_name'].append(district_name)
            colu['RegisteredUsers'].append(RegisteredUsers)
            colu['AppOpens'].append(AppOpens)
            colu['State'].append(i)
            colu['Year'].append(j)
            colu['Quater'].append(int(k.strip('.json')))
      except:
        pass
#Succesfully created a dataframe
map_user=pd.DataFrame(colu)   
# Exporting the DataFrame to csv file
map_user.to_csv('Map_User.csv', sep=',',index =False)
map_user         
------------------------------------------------------------------------------------------------------------------------------------------
path = "/content/pulse/data/top/transaction/country/india/state/"
top_state_list = os.listdir(path)
#print(top_state_list)

colu={'State':[], 'Year':[],'Quater':[],'District_name':[],'Transaction_count':[], 'Transaction_amount':[]}

for i in top_state_list:
  path_i = path+i+'/'
  top_year_list = os.listdir(path_i)
  #print(top_year_list)
  for j in top_year_list:
    path_j = path_i +j+'/'
    top_qtr_list= os.listdir(path_j)
    #print(top_qtr_list)
    for k in top_qtr_list:
      path_k = path_j+k
      Data =open(path_k,'r')
      Da=json.load(Data)
      #print(Da)
      for z in Da['data']['districts']:
        #print(z)
        district_name = z['entityName']
        count = z['metric']['count']
        amount= z['metric']['amount']
        colu['District_name'].append(district_name)
        colu['Transaction_count'].append(count)
        colu['Transaction_amount'].append(amount)
        colu['State'].append(i)
        colu['Year'].append(j)
        colu['Quater'].append(int(k.strip('.json')))

#Succesfully created a dataframe
Top_Dis_Trans=pd.DataFrame(colu)   
# Exporting the DataFrame to csv file
Top_Dis_Trans.to_csv('Top_District_Transaction.csv', sep=',',index =False) 
Top_Dis_Trans  
----------------------------------------------------------------------------------------------------------------------------
path = "/content/pulse/data/top/transaction/country/india/state/"
top_state_list = os.listdir(path)
#print(top_state_list)

colu={'State':[], 'Year':[],'Quater':[],'pincodes':[],'Transaction_count':[], 'Transaction_amount':[]}

for i in top_state_list:
  path_i = path+i+'/'
  top_year_list = os.listdir(path_i)
  #print(top_year_list)
  for j in top_year_list:
    path_j = path_i +j+'/'
    top_qtr_list= os.listdir(path_j)
    #print(top_qtr_list)
    for k in top_qtr_list:
      path_k = path_j+k
      Data =open(path_k,'r')
      Da=json.load(Data)
      #print(Da)
      for z in Da['data']['pincodes']:
        #print(z)
        district_name = z['entityName']
        count = z['metric']['count']
        amount= z['metric']['amount']
        colu['pincodes'].append(district_name)
        colu['Transaction_count'].append(count)
        colu['Transaction_amount'].append(amount)
        colu['State'].append(i)
        colu['Year'].append(j)
        colu['Quater'].append(int(k.strip('.json')))

#Succesfully created a dataframe
top_pin_Trans=pd.DataFrame(colu)  
# Exporting the DataFrame to csv file 
top_pin_Trans.to_csv('Top_Pincodes_Transaction.csv', sep=',',index =False)
top_pin_Trans        
----------------------------------------------------------------------------------------------------------------------------
path = "/content/pulse/data/top/user/country/india/state/"
top_state_list = os.listdir(path)
#print(top_state_list)

colu={'State':[], 'Year':[],'Quater':[],'District_name':[], 'RegisteredUsers':[]}

for i in top_state_list:
  path_i = path+i+'/'
  top_year_list = os.listdir(path_i)
  #print(top_year_list)
  for j in top_year_list:
    path_j = path_i +j+'/'
    top_qtr_list= os.listdir(path_j)
    #print(top_qtr_list)
    for k in top_qtr_list:
      path_k = path_j+k
      Data =open(path_k,'r')
      Da=json.load(Data)
      #print(Da)
      try:
          for z in Da['data']['districts']:
            #print(z)
            district_name = z['name']
            registeredUsers = z['registeredUsers']
            colu['District_name'].append(district_name)
            colu['RegisteredUsers'].append(registeredUsers)
            colu['State'].append(i)
            colu['Year'].append(j)
            colu['Quater'].append(int(k.strip('.json')))
      except:
        pass   
#Succesfully created a dataframe
top_dis_user=pd.DataFrame(colu) 
# Exporting the DataFrame to csv file  
top_dis_user.to_csv('Top_District_User.csv', sep=',',index =False)
top_dis_user     
---------------------------------------------------------------------------------------------------------------------------
path = "/content/pulse/data/top/user/country/india/state/"
top_state_list = os.listdir(path)
#print(top_state_list)

colu={'State':[], 'Year':[],'Quater':[],'pincodes':[], 'RegisteredUsers':[]}

for i in top_state_list:
  path_i = path+i+'/'
  top_year_list = os.listdir(path_i)
  #print(top_year_list)
  for j in top_year_list:
    path_j = path_i +j+'/'
    top_qtr_list= os.listdir(path_j)
    #print(top_qtr_list)
    for k in top_qtr_list:
      path_k = path_j+k
      Data =open(path_k,'r')
      Da=json.load(Data)
      #print(Da)
      try:
          for z in Da['data']['pincodes']:
            #print(z)
            pincodes = z['name']
            registeredUsers = z['registeredUsers']
            colu['pincodes'].append(pincodes)
            colu['RegisteredUsers'].append(registeredUsers)
            colu['State'].append(i)
            colu['Year'].append(j)
            colu['Quater'].append(int(k.strip('.json')))
      except:
        pass   
#Succesfully created a dataframe
top_pin_user=pd.DataFrame(colu) 
# Exporting the DataFrame to csv file
top_pin_user.to_csv('Top_Pincodes_User.csv', sep=',',index =False)
top_pin_user          
----------------------------------------------------------------------------------------------------------------------------------------------
#  Agg_Trans,Agg_user,map_Trans,map_user,Top_Dis_Trans,top_pin_Trans,top_dis_user,top_pin_user
# CHECKING FOR MISSING VALUES,NULL VALUES
Agg_Trans.info()
Agg_user.info()
map_Trans.info()
map_user.info()
Top_Dis_Trans.info()
top_pin_Trans.info()
top_dis_user.info()
top_pin_user.info()

