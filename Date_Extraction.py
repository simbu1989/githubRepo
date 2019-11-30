
###############################################################################################################
####                                            Required Packages                                          ####
###############################################################################################################
import pytesseract
import cv2
import re
import datetime
import glob
import pandas as pd
import sys
import os

###############################################################################################################
####                                  Location of .jpeg files                                              ####
###############################################################################################################

path =sys.argv[1]
pytes_path = sys.argv[2]
pytess_path = os.path.join(pytes_path)
img_path = os.path.join(path,'*.jpeg')
filelist = glob.glob(img_path)
pytesseract.pytesseract.tesseract_cmd = pytess_path 

################################################################################################################
####                                    Date Extract Part                                                   ####
################################################################################################################

for i in  range(len(filelist)):   
    img= cv2.imread(filelist[i],0)
    img_s = cv2.resize(img, None, fx=2.5, fy=2.5, interpolation=cv2.INTER_LINEAR)  
    text = pytesseract.image_to_string(img_s, lang='eng')
    text = text.lower()
    Expense_date1 = re.findall("\d{1,2}/\d{1,2}/\d{2,4}|\d{1,2}-\d{1,2}-\d{2,4}|\d{4}-\d{1,2}-\d{1,2}|[jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec]{3}\.[\d]{1,2}\’[\d]{2,4}|[\d]{1,2}-[jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec]{3}-[\d]{2,4}|[\d]{1,2}/[jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec]{3}/[\d]{2,4}|[\d]{1,2}[jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec]{3}\"[\d]{2,4}|[\d]{1,2} [jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec]{3}\’[\d]{2,4}",text)   
    if len(Expense_date1)>=1:
        if len(Expense_date1)>=2:
            Expense_date1 = Expense_date1[0]
        Expense_date1= Expense_date1    
        Expense_date2 = ''.join(Expense_date1)    
        Expense_date3 = re.sub('[^A-Za-z0-9-/.]+', ' ', Expense_date2)
        Expense_date4 = pd.to_datetime(Expense_date3,errors='coerce')
        if pd.isnull(Expense_date4)==True:
           Expense_date = "null"
        else:
            Expense_date = Expense_date4.strftime('%Y-%m-%d')
        Expense_date = dict(date=Expense_date)
        print(Expense_date)
    else:
        Expense_date = dict(date='null')
        print(Expense_date)

##############################################################################################################
####                                      END                                                             ####
##############################################################################################################       
        
