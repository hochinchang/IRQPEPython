### QPESUMS_GAUGE.10M
範例資料
+ 202205270000.QPESUMS_GAUGE.10M.mdf：降雨量資料，有兩行檔頭標註日期時間，資料包含18個案位（STID, STNM, TIME, LAT, LON, LEV, RAIN, MIN_10, HOUR_3, HOUR_6, HOUR_12, HOUR_24, NOW,CITY, CITY_SN, TOWN, TOWN_SN, ATTRIBUTE）。處理它會遇到以下幾個問題。
  - 檔頭要刪掉比較方便後續的處理。
  - 檔案編碼是cp950，一般windows用utf-8。
  - 資料欄位之間的空隔不一致。

程式
+ CQPESUMS_GAUGE.10m_v1.py：把資料讀進來轉換成csv格式存在tempfile.csv，供後續處理，例如用pands去清洗資料及排序。函式mdf2csv中解決了前述資料內容的問題。
