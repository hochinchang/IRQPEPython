## IRQPEPython專案說明
本專案的目的是為IRQPE設計一套校驗及畫圖的python程式集，從一組資料和由其他軟體所畫的範例圖，撰寫一個python程式讀取資料並畫出跟範例一樣水準或更漂亮的圖，最後把程式碼包裝成一個物件，以方便其他人使用。目前正在起步階段，檔名\*v1.py表示是最簡略版本，用最少的行數讀資料及畫圖；檔名\*v2.py表示是進階的版本，仿照範例圖的樣式，調整座標軸、線條顏色與型式、添加上一些說明文字；檔名\*v3.py表示已經完成物件的設計，但是本人還在學習中，所以短期內還不會進行到這步驟。

### CMTmon_M8xm
範例資料
+ CMTmon_M8xm.txt：一筆8欄x12列以空隔做間隔的陣列資料，其中12列代表12個月份，8欄則是表示8種不同的降雨估計方法。
+ CMTmon_M8xm_ex.png：範例圖。

程式
+ CMTmon_M8xm_v1.py：用numpy讀資料，用matplotlib畫圖。
+ CMTmon_M8xm_v2.py：參考範列修改座標軸、顏色、圖例(lengend)等。
+ CMTmon_M8xm_v2-1.py：用seaborn套件加以美化輸出的結果。

### QPESUMS_GAUGE.10M
範例資料
+ 202205270000.QPESUMS_GAUGE.10M.mdf：降雨量資料，有兩行檔頭標註日期時間，資料包含18個案位'STID','STNM','TIME','LAT','LON','ELEV','RAIN','MIN_10','HOUR_3'     ,'HOUR_6','HOUR_12','HOUR_24','NOW','CITY','CITY_SN','TOWN','TOWN_SN','ATTRIBUTE'。讀它處理會遇到幾個問題。
  - 檔頭要刪掉比較方便後續的處理。
  - 檔案編碼是cp950，一般windows用utf-8。
  - 資料欄位之間的空隔不一致。

程式
+ CQPESUMS_GAUGE.10m_v1.py：把資料讀進來轉換成csv格式存在tempfile.csv，供後續處理，例如用pands去清洗資料及排序。函式mdf2csv中解決了前述資料內容的問題。
