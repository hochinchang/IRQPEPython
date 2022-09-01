# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 07:49:00 2022

@author: Hochin

目的：
讀入雨量資料(QPESUMS_GAUGE.10M.mdf)，並且針對雨量做排序(ranking)。
"""
import pandas as pd

def mdf2csv(filename, head):
    """
    Parameters
    ----------
    filename : string
        雨量資料(QPESUMS_GAUGE.10M.mdf)(編碼cp950)
    head : int
        欲刪除的檔頭資料行數。
    Returns
        輸出一個暫存的csv檔(tempfile.csv)（編碼utf-8)
    -------
    """
    fin = open(filename, 'r')
    print(fin)
    lin = fin.readlines()
    fout = open('tempfile.csv', 'w',encoding='utf-8')
    # a[head:]表示只處理檔頭之外的行數
    for ll in lin[head:]:
        #以空隔為分隔符號，把一行的資料切分成數個欄位，存成list。
        lis=ll.split(sep=' ')
        #把list中空白的原素去除。
        lis=[x.strip() for x in lis if x.strip()!='']
        #把list轉成字串，並用逗點分隔。
        st=','.join(lis)
        fout.write(st+'\n')     

if __name__=='__main__':
    file='202205270000.QPESUMS_GAUGE.10M.mdf'
    #column_names=['STID','STNM','TIME','LAT','LON','ELEV','RAIN','MIN_10','HOUR_3'\
    #             ,'HOUR_6','HOUR_12','HOUR_24','NOW','CITY','CITY_SN' \
    #             ,'TOWN','TOWN_SN','ATTRIBUTE']
    mdf2csv(file,2)
    df=pd.read_csv('tempfile.csv')
    print(df.info())

