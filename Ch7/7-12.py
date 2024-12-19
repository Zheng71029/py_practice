# 定義 Year 類別
class Year:
    def __init__(self, y):  # 初始化函數
        self.__year = y  # 私有屬性 __year

    def isleap(self):  # 判斷是否為閏年的函數
        # 閏年的條件：年份能被 4 整除，且不能被 100 整除，或者能被 400 整除
        return (self.__year % 4 == 0 and self.__year % 100 != 0) or (self.__year % 400 == 0)

    @property
    def year(self):  # Getter，取得 __year 的值
        return self.__year

    @year.setter
    def year(self, y):  # Setter，設定 __year 的值
        self.__year = y


# 測試程式
y0 = Year(2022)  # 創建 Year 類別的物件，年份為 2022
print(y0.year)  # 印出年份，結果應為 2022
print(y0.isleap())  # 判斷是否為閏年，結果應為 False

y0.year = 2020  # 將年份設為 2020
print(y0.year)  # 印出年份，結果應為 2020
print(y0.isleap())  # 判斷是否為閏年，結果應為 True
