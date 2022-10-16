from posixpath import split
from statistics import stdev
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
import missingno as msno
import re



df = pd.read_csv("c:/Users/ruzga/Desktop/Veri Bilimi/Python/pandas/job_dataset.csv")
# print(df.to_string())


# df.info()

# Veri setinde 1583 gözlem ve 8 adet değişken vardır.
#(Satır => 1583)
#(Sütun => 8)

# Sadece job_salary değişkeninde kayıt değer bulunmaktadır.

# Değişkenlerin hepsi (8 adet) object veri tipine sahiptir.

# Fikir elde etmek için ilk 5 ve son 5 kayıta bakalım.

result = df.head()
result1 = df.tail()

# Sütun yani değişken isimleri açıklayıcı ve net bir şekilde yazılmış

# Kayıp verilerin bulunduğu job_salary kolonu işaretlenmiş.

# Metin düzgün, typo hatası olmadan yazılmış olarak görülüyor.

# job_salary değişkeninde bulunan değerlerin hem string hem float değerler olduğunu görebiliyoruz. Ayrıca minimum ve maxsimum değerlere sahip gözlemlerde var. 


# Yapısal düzenin kontrolü için

result = df.iloc[:20, :2]
result1 = df.iloc[:20, 2:4]
result2 = df.iloc[:20, 4:6]
result3 = df.iloc[:20 ,6:8]

result = df[["job_location","post_date","job_salary"]][0:20]


"""

"post_date" değişkeni 2 aynı sütuna bölünecek.
"job_salary" değişkeni düzenlenecek.
"today" değişkeni string'den integer'a dönüşecek.
"job_location" değişkenine bir göz atılacak.

"""

result = df.dtypes




# 1- "post_date" için:

result = df["post_date"].head(20)
# result = df["post_date"].nunique()

# print(df["post_date_conditions"].dtype)

# result = df[df.post_date.str.contains("days ago")]["post_date"]

# # sadece 1415 kayıtta days ago geçiyor.

# result = len(df[df.post_date.str.contains("day ago")]["post_date"])

# 31 kayıtta da day ago geçiyor.
# 1446 kayıtta geçenleri bulduk. ("days ago", "day ago")


result = df.columns # kolon isimlerine bakmak için

# df["post_date_days"] = df["post_date"].str.split(" ").str[1]
# result = df["post_date_days"]

# result = df["post_date_days"].nunique()

# result = df[df.post_date.str.contains("posted")]["post_date"]
# result = df[df.post_date_days.str.contains("posted")]["post_date_days"]


# "post_date" değişkeninden "day ago", "days ago" ve "+" string türündeki verileri silerek "new_post_date" isminde yeni bir değişken oluşturduk

# df["new_post_date"] = df.post_date.str.replace("day ago","").str.replace("days ago","").str.replace("+","")
# df["new_post_date"] = df["new_post_date"].str.strip()
# result = df["new_post_date"]

df["post_date"] = df.post_date.str.replace("day ago","").str.replace("days ago","").str.replace("+","")
df["post_date"] = df["post_date"].str.strip()

# result = df["new_post_date"].nunique()


# df["new_post_date"] = df["new_post_date"].str.split()
# result = df["new_post_date"].head(50)

# result = df["new_post_date"].value_counts()[0:50]
# result1 = df["new_post_date"].value_counts()[50:100]

## def fonksiyonu ile Posted30, Posted6 gibi verileri ayrı kolonlarda yazmak için Posted 30 ve Posted 6 şeklinde düzeltiyoruz.

def half_counts(val):
    if val == val:
        if "former" in val:
            val = re.sub("\(former\)", "", val)

        elif "Posted6" in val:
            if "(" in val:
                val = re.sub("\(Posted6\)","Posted 6", val )
            else:
                val = re.sub("Posted6", "Posted 6", val)

        elif "Posted4" in val:
            if "(" in val:
                val = re.sub("\(Posted4\)","Posted 4", val )
            else:
                val = re.sub("Posted4", "Posted 4", val)
        
        elif "Posted30" in val:
            if "(" in val:
                val = re.sub("\(Posted30\)" ,"Posted 30", val)
            else:
                val = re.sub("Posted30", "Posted 30", val)
        
        elif "Posted5" in val:
            if "(" in val:
                val = re.sub("\(Posted5\)", "Posted 5", val)
            else:
                val = re.sub("Posted5", "Posted 5", val)
        
        elif "Posted3" in val:
            if "(" in val:
                val = re.sub("\(Posted3\)", "Posted 3", val)
            else:
                val = re.sub("Posted3", "Posted 3", val)

        elif "Posted10" in val:
            if "(" in val:
                val = re.sub("\(Posted10\)", "Posted 10", val)
            else:
                val = re.sub("Posted10", "Posted 10", val)

        elif "Posted13" in val:
            if "(" in val:
                val = re.sub("\(Posted13\)", "Posted 13", val)
            else:
                val = re.sub("Posted13", "Posted 13", val)
        
        elif "Posted12" in val:
            if "(" in val:
                val = re.sub("\(Posted12\)" , "Posted 12", val)
            else:
                val = re.sub("Posted12", "Posted 12", val)
        
        elif "Posted7" in val:
            if "(" in val:
                val = re.sub("\(Posted7\)", "Posted 7", val)
            else:
                val = re.sub("Posted7", "Posted 7", val)
        
        elif "Posted19" in val:
            if "(" in val:
                val = re.sub("\(Posted19\)", "Posted 19", val)
            else:
                val = re.sub("Posted19", "Posted 19", val)

        elif "Posted11" in val:
            if "(" in val:
                val = re.sub("\(Posted11\)", "Posted 11", val)
            else:
                val = re.sub("Posted11", "Posted 11", val)

        elif "Posted1" in val:
            if "(" in val:
                val = re.sub("\(Posted1\)", "Posted 1", val)
            else:
                val = re.sub("Posted1", "Posted 1", val)

        elif "Posted14" in val:
            if "(" in val:
                val = re.sub("\(Posted14\)", "Posted 14", val)
            else:
                val = re.sub("Posted14", "Posted 14", val)

        elif "Posted25" in val:
            if "(" in val:
                val = re.sub("\(Posted25\)", "Posted 25", val)
            else:
                val = re.sub("Posted25", "Posted 25", val)

        elif "Posted24" in val:
            if "(" in val:
                val = re.sub("\(Posted24\)", "Posted 24", val)
            else:
                val = re.sub("Posted24", "Posted 24", val)

        elif "Posted20" in val:
            if "(" in val:
                val = re.sub("\(Posted20\)", "Posted 20", val)
            else:
                val = re.sub("Posted20", "Posted 20", val)

        elif "Posted2" in val:
            if "(" in val:
                val = re.sub("\(Posted2\)", "Posted 2", val)
            else:
                val = re.sub("Posted2", "Posted 2", val)

        elif "Posted17" in val:
            if "(" in val:
                val = re.sub("\(Posted17\)", "Posted 17", val)
            else:
                val = re.sub("Posted17", "Posted 17", val)

        elif "Posted26" in val:
            if "(" in val:
                val = re.sub("\(Posted26\)", "Posted 26", val)
            else:
                val = re.sub("Posted26", "Posted 26", val)

        elif "Posted27" in val:
            if "(" in val:
                val = re.sub("\(Posted27\)", "Posted 27", val)
            else:
                val = re.sub("Posted27", "Posted 27", val)

        elif "Posted8" in val:
            if "(" in val:
                val = re.sub("\(Posted8\)", "Posted 8", val)
            else:
                val = re.sub("Posted8", "Posted 8", val)
        
        elif "Posted18" in val:
            if "(" in val:
                val = re.sub("\(Posted18\)", "Posted 18", val)
            else:
                val = re.sub("Posted18", "Posted 18", val)

        elif "Posted28" in val:
            if "(" in val:
                val = re.sub("\(Posted28\)", "Posted 28", val)
            else:
                val = re.sub("Posted28", "Posted 28", val)

        elif "Posted21" in val:
            if "(" in val:
                val = re.sub("\(Posted21\)", "Posted 21", val)
            else:
                val = re.sub("Posted21", "Posted 21", val)

        elif "Posted23" in val:
            if "(" in val:
                val = re.sub("\(Posted23\)", "Posted 23", val)
            else:
                val = re.sub("Posted23", "Posted 23", val)

        elif "Posted9" in val:
            if "(" in val:
                val = re.sub("\(Posted9\)", "Posted 9", val)
            else:
                val = re.sub("Posted9", "Posted 9", val)

        elif "Posted15" in val:
            if "(" in val:
                val = re.sub("\(Posted15\)", "Posted 15", val)
            else:
                val = re.sub("Posted15", "Posted 15", val)

        elif "Posted22" in val:
            if "(" in val:
                val = re.sub("\(Posted22\)", "Posted 22", val)
            else:
                val = re.sub("Posted22", "Posted 22", val)

        elif "Employer30" in val:
            if "(" in val:
                val = re.sub("\(Employer30\)", "Employer 30", val)
            else:
                val = re.sub("Employer30", "Employer 30", val)
            

        else:
            val == val
    else:
        val = np.nan
    return val




df["new_post_date"] = df["post_date"].apply(half_counts)


result = df["new_post_date"].value_counts()[0:50]
result1 = df["new_post_date"].value_counts()[50:100]







# # "new_post_date" kolonunu 2 farklı kolona ayırdık. ("post_situation" işe alım durumu, "post_spread_time" yayınlanma tarihi)

df["post_situation"] = df["new_post_date"].str.split(" ").str[0]
df["post_spread_time"] = df["new_post_date"].str.split(" ").str[1]

# ## oluşturulan kolonlar için başta ve sondaki boşluk karakterlerini sildik. ve yukarıda replace metodu ile değiştirdiğimiz "" konlonlarınıda sildik.
df["post_situation"] = df["post_situation"].str.strip()
df["post_spread_time"] = df["post_spread_time"].str.strip()

result = df[["post_situation","post_spread_time"]].head(10)


# # # Oluşturulan 2 kolon için boş eleman sayılarının toplamına bakıldı.
result = df[["post_situation","post_spread_time"]].isnull().sum()
result = df["post_spread_time"].nunique()

# # # "post_spread_time" değişkeninden "posted" ve "ongoing" değerleri silindi.
df["post_spread_time"] = df.post_spread_time.str.replace("posted", "").str.replace("ongoing", "")

# # Baştaki ve sondaki boşluk karakterlerini sildik
df["post_spread_time"] = df["post_spread_time"].str.strip()
result = df["post_spread_time"].head(40)

# # "posted" ve "ongoing" değerlerinin silinmesiyle boş kalan dizilere np.nan yani NaN atadık.
df["post_spread_time"] = df["post_spread_time"].replace("", np.nan)
result = df["post_spread_time"].head(50)



# # # kolon için farklı elemanlara bakıldı ve 32 'den 31 adet birbirinden farklı veri kaldığı gözlemlendi.
result = df["post_spread_time"].nunique()



# # # str-int dönüşümü için boş değerleri 99999 sayısı ile doldurduk.
df["post_spread_time"] = df["post_spread_time"].replace(np.nan, 99999)

# # bütün kolonların bilgilerine baktık ve hazılardığımız kolonda 504 tane dolu veri varken şimdi boş veri kalmamış.
# result = df.info()
result = df["post_spread_time"].head(50)


# # Dönüşüm işlemi tamamlandı.
df["post_spread_time"] = df["post_spread_time"].astype("int")
df["post_spread_time"].dtypes
result = df["post_spread_time"].head(50)



# # Dönüşüm işlemi bittikden sonra 99999 atadığımız değerleri tekrar np.nan moduna geçiriyoruz.
df["post_spread_time"] = df["post_spread_time"].replace(99999, np.nan)
result = df["post_spread_time"].head(50)
result = df["post_spread_time"].isnull().sum()

# result = df.info()


# # kolonda kaç farkl değer var ona bakıyoruz.
result = df["post_situation"].head(50)
result = df["post_situation"].nunique()

# # ilk 50 değerde kaç farklı veri var ona bakıcaz
result = df["post_situation"].value_counts()[0:50]

def situation_half(val):
    if val == val:
        if "former" in val:
            val = re.sub("\(former\)", "", val)

        elif "PostedPosted" in val:
            if "(" in val:
                val = re.sub("\(PostedPosted\)", "Posted", val)
            else:
                val = re.sub("PostedPosted", "Posted", val)
        
        elif "EmployerActive" in val:
            if "(" in val:
                val = re.sub("\(EmployerActive\)", "Employer Active", val)
            else:
                val = re.sub("EmployerActive", "Employer Active", val)

        elif "PostedToday" in val:
            if "(" in val:
                val = re.sub("\(PostedToday\)", "Posted Today", val)
            else:
                val = re.sub("PostedToday", "Posted Today", val)
            
        elif "PostedJust" in val:
            if "(" in val:
                val = re.sub("\(PostedJust\)", "Posted Just", val)
            else:
                val = re.sub("PostedJust", "Posted Just", val)

        elif "Hiring" in val:
            if "(" in val:
                val = re.sub("\(Hiring\)", "Hiring On Going", val)
            else:
                val = re.sub("Hiring", "Hiring On Going", val)

        else:
            val == val
    
    else:
        val = np.nan

    return val

df["post_situation"] = df["post_situation"].apply(situation_half)
df["post_situation"] = df["post_situation"].str.strip()
result = df["post_situation"].value_counts()[0:50]


result = df[["post_date" ,"post_situation","post_spread_time"]].head(50)

## karışık post_date değişkenini düzenleyip new_post_date adında yeni bir kolona yazdırdık. Sonra new_post_date kolonunuda 2 ayrı kolona ayırdık.
#   post_situation ve post_spread_time adında. 
#   ilk olarak post_spread_time kolonunda, string ifadeleri sildik boş değerlere 99999 atadık ve bütün kolonu floata çevirdik. Daha sonrasında bütün 9999 değerleri nan değerler ile değiştirdik.
#   post_situation kolonunda birleşik yazılmış olan karakterleri ayırdık. Örn PostedPosted yazana yerleri Posted ile değiştirdik.

# Şimdi diğer kolonlara bakalım..

# result = df.iloc[:20, :2]
# result1 = df.iloc[:20, 2:4]
# result2 = df.iloc[:20, 4:6]
# result3 = df.iloc[:20 ,6:8]


# "today" değişkenini datetime tipine çeviriyoruz.
df["today"] = pd.to_datetime(df["today"])
# df.info()


result = df.iloc[:20, :2]
result1 = df.iloc[:20, 2:4]
result2 = df.iloc[:20, 4:6]
result3 = df.iloc[:20, 6:8]
result4 = df.iloc[:20, 8:11]

## "job_salary" değişkenine göz atacağız

result = df["job_salary"].head(50)
result = df["job_salary"].value_counts()[0:50]


## def fonksiyonu ile "year"ı "yeer" ve "an"i "a" olarak değiştirdik. Daha rahat ayırmak için.


def half_counts(val):
    if val == val:
        if "former" in val:
            val = re.sub("\(former\)", "", val)
        
        elif "year" in val:
            if "(" in val:
                val = re.sub("\(year\)", "yeer", val)
            else:
                val = re.sub("year", "yeer", val)
            
        elif "an" in val:
            if "(" in val:
                val = re.sub("\(an\)", "a", val)
            else:
                val = re.sub("an", "a", val)

        else:
            val == val
    
    else:
        val = np.nan

    return val

df["new_job_salary"] = df["job_salary"].apply(half_counts)
df["new_job_salary"] = df["new_job_salary"].str.strip()
result = df["new_job_salary"].head(50)

        
# ₹ para birimini ve boşlukları " ", tüm "new_job_salary" kolonundan sildik.
df["new_job_salary"] = df.new_job_salary.str.replace("₹", "").str.replace(" ", "")
result = df["new_job_salary"].head(50)


# kolondaki "a" harflerini boşluk " " ile değiştirdik. Daha rahat split yapabilmek için.
df["new_job_salary"] = df.new_job_salary.str.replace("a", " ")
result = df["new_job_salary"].head(50)
df["new_job_salary"] = df["new_job_salary"].str.strip()


# "new_job_salary" kolonunun [0]. indexini df["new_salary_column"] kolonuna atadık.
df["new_salary_column"] = df["new_job_salary"].str.split(" ").str[0]
df["new_salary_column"] = df["new_salary_column"].str.strip()
result = df["new_salary_column"].head(50)

# yeni oluşturduğumuz "new_job_salary" kolonunda "-" karakterini boşluk " " ile değiştirdik.
df["new_salary_column"] = df.new_salary_column.str.replace("-", " ")
result = df["new_salary_column"].head(50)

result = df["new_salary_column"].head(50)

result = df["new_salary_column"].value_counts()[:50]


## "new_salary_column"un [0]. indexini oluşturduğumuz "min_salary" kolonuna attık.
df["min_salary"] = df["new_salary_column"].str.split(" ").str[0]
df["min_salary"] = df["min_salary"].str.strip()
result = df["min_salary"].head(50)

## "new_salary_column"'un [1]. indexini oluşturduğumuz "max_salary" kolonuna attık.
df["max_salary"] = df["new_salary_column"].str.split(" ").str[1]
df["max_salary"] = df["max_salary"].str.strip()
result = df["max_salary"].head(50)

result = df[["job_title", "min_salary", "max_salary"]].head(50)

result = df["min_salary"].head(50)



## "min_salary" değişkenindeki "," leri sildik "" daha sonrasında object olan veri tipini float'a çevirdik.
df["min_salary"] = df.min_salary.str.replace(",", "")

df["min_salary"] = df["min_salary"].astype("float")
result = df["min_salary"].head(50)


## "max_salary" değişkenindeki "," leri sildik "" daha sonrasında object olan veri tipini float'a çevirdik.
df["max_salary"] = df.max_salary.str.replace(",", "")

df["max_salary"] = df["max_salary"].astype("float")
result = df["max_salary"].head(50)





# "new_job_salary"de zaman bildiren indexleri "payment_schedule" kolonunu oluşturup içine attık.
df["payment_schedule"] = df["new_job_salary"].str.split(" ").str[1]
df["payment_schedule"] = df["payment_schedule"].str.strip()
result = df["payment_schedule"].head(50)

result = df["payment_schedule"].value_counts()[:50]



# def fonkisyonu ile "yeer" olan yerleri "Yearly", "month" olan yerleri "Monthly" ve "hour" olan yerleri "Hourly" olarak değiştirdik.
def change_paid(val):
    if val == val:
        if "yeer" in val:
            if "(" in val:
                val = re.sub("\(yeer\)", "Yearly", val)
            else:
                val = re.sub("yeer", "Yearly", val)

        elif "month" in val:
            if "(" in val:
                val = re.sub("\(month\)", "Mounthly", val)
            else:
                val = re.sub("month", "Mounthly", val)

        elif "hour" in val:
            if "(" in val:
                val = re.sub("\(hour\)", "Hourly", val)
            else:
                val = re.sub("hour", "Hourly", val)
    else:
        val = np.nan

    return val

df["payment_schedule"] = df["payment_schedule"].apply(change_paid)
df["payment_schedule"] = df["payment_schedule"].str.strip()

result20 = df["payment_schedule"].head(50)

print(result20)

result = df.columns



## Son olarak veri setimizin daha düzenli görülmesi için, "post_date", "job_salary" gibi işlem yaptığımız kolonları ve işlemlerin tamamlanması
#    için oluşturduğumuz "new_post_date", "new_job_salary" ve "new_salary_column" kolonlarını sileceğiz.


# df = df.drop(["post_date", "job_salary", "new_post_date", "new_job_salary", "new_salary_column"], axis = 1)


# result = df.columns

# ## Veri setinin yeni halinin nasıl göründüğüne bakmak için.
# result = df.iloc[:20, :2]
# result1 = df.iloc[:20, 2:5]
# result2 = df.iloc[:20, 5:8]
# result3 = df.iloc[:20, 8:11]


# df.info()
    
# ## csv dosyasını excele dönüştürüp kopyasını kaydetmek için.

# import openpyxl

# wb = openpyxl.Workbook()
# sayfa = wb.active

# a2 = len(df)
# a3 = len(df.columns)

# for x in range(a3):
#     c = x + 1
#     sayfa.cell(row = 1, column = c).value = df.columns[x]

# for x in range(a2):
#     for y in range(a3):
#         r = x + 2
#         c = y + 1
#         sayfa.cell(row = r, column = c).value = df.iat[x,y]

# wb.save("c:/Users/ruzga/Desktop/job_dataset_new.xlsx")


## dönüşüm işlemi için https://www.youtube.com/watch?v=pftVK72KH4Y




# print(result)
# print(result1)
# print(result2)
# print(result3)
# print(result4)




## DÜZENLENEN VERİNİN ANALİZ KISMI ##

## "min_salary" ve "max_salary" değişkenlerinde aykırı değer olup olmadığına bakıyoruz.

result = df[["max_salary","min_salary"]].describe()
not_null_salary = df[df[["max_salary","min_salary"]].isnull() == False][["max_salary","min_salary"]]
plt.boxplot(not_null_salary)
# plt.show()
# Aykırı değer yokmuş.



import statistics

# Veri setinde kaç tane satır olduğuna bakmak için.
result = len(df.index) 

"""

## "max_salary" üzerinde yapılacak istatistiksel işlemler için öncelikle NaN değerleri kolondan siliyoruz.

result = df["max_salary"].isnull().sum()

# DataFrame'de "max_salary" ve "payment_schedule" kolonlarında NaN değerlerlere eşit olan satıları silmek için
# df = df.dropna(subset=("max_salary", "payment_schedule"), axis=0)
result1 = df[["max_salary","payment_schedule"]].isnull().sum()
result = df[["max_salary","payment_schedule"]]

## "max_salary" MOUNTHLY ##

## "max_salary"de aylık olarak en fazla maaşı buluyoruz.
result = df.groupby("payment_schedule")["max_salary"].max()["Mounthly"]

## yukarıda bulduğumuz "max_salary"deki en yüksek maaşın diğer kolon bilgilerine erişiyoruz. 
result = df[(df["max_salary"] == 650000.0)]

## Yorum: "max_salary"de aya göre en yüksek maaşı veren şirket 2 tane işe alım ilanı yayımlamış.
# En Yüksek Maaş:   En yüksek maaş 650000.0 rupi
# Şirket İsmi:      Tech Opportunity
# İş Başlığı:       Machine Learning Developer
# Yayın Tarihi:     1 gün önce



## "max_salary"de aylık olarak en az maaşı buluyoruz
result = df.groupby("payment_schedule")["max_salary"].min()["Mounthly"]

## yukarıda bulduğumuz "max_salary"deki en düşük maaşın diğer kolon bilgilerine erişiyoruz. 
result = df[(df["max_salary"] == 6000.0)]

## Yorum: "max_salary"de aya göre en düşük maaş bilgileri.
# En Düşük Maaş:    6000.0 rupi
# Şirket İsmi:      Sri Renga Global
# İş Başlığı:       Data Analyst
# Yayın Tarihi:     4 gün önce


## "max_salary"nin aylık maaşının ortalamasını bulmak için. => 53543.65 rupi
result = df.groupby("payment_schedule")["max_salary"].mean()["Mounthly"]

## Veri setinde aylık maaş ile verilen iş ilanı 134 adet.
result = df.groupby("payment_schedule")["max_salary"].count()["Mounthly"]



## "max_salary" YEARLY  ###

## "max_salary" de yıllık olarak en az maaşı buluyoruz. => 150000.0 rupi
result = df.groupby("payment_schedule")["max_salary"].min()["Yearly"]

## Yukarıda bulduğumuz minimum değeri veren diğer kolon isimlerine bakıyoruz.
result = df[df["max_salary"] == 150000.0]

# yayın tarihi çıkmadığı için bu işlemi yaptık
# result = df["post_spread_time"][1561]


## Yorum: "max_salary"de yıla göre en düşük maaş bilgileri;
# En Düşük Maaş:    150000.0 rupi
# Şirket İsmi:      K D Groups
# İş Başlığı:       Urjent Hiring for Data Analyst
# Yayın Tarihi:     30 gün önce


## "max_salary" de yıllık olarak en fazla maaşı buluyoruz. => 6000000.0 ruoi
result = df.groupby("payment_schedule")["max_salary"].max()["Yearly"]

## Yukarıda bulduğumuz yıllık en fazla maaş işe diğer bilgilere erişiyoruz.
result = df[df["max_salary"] == 6000000.0]

## Yorum: "max_salary" de yılar göre en fazla maaşı veren 3 tane iş ilanı çıkıyor. Bunların 2 si aynı şirket fakat farklı özellikler istiyor.
# En Fazla Maaş:    6000000.0 rupi
# Şirket İsmleri:   BEIING , Strategic Talent Partner
# İş Başlıkları:    Data Scientist, Head Data Scientist         
# Yayın Tarihleri:  sırasıyla 26 ve 30 gün önce

## "max_salary"nin yıllık maaş ortalaması. => 1477679.93
result = df.groupby("payment_schedule")["max_salary"].mean()["Yearly"]

# Veri setinde yıllık olarak verilen iş ilanı 201 adettir.
result = df.groupby("payment_schedule")["max_salary"].count()["Yearly"]




### "min_salary" ye göre bilgiler alınacak

result = df["min_salary"].isnull().sum() # => 1178 adet kayıp değer bulunmaktadır.

df = df.dropna(subset = ("min_salary", "payment_schedule"), axis=0 )
result = df["min_salary"].isnull().sum() # => "min_salary" deki kayıp değerlerin hepsini sildik. Şimdi rahatça istenilen bilgilere ulaşılabilir.

## "min_salary" MOUNTHLY ##

## "min_salary"de iş ilanlarından aylık en fazla maaş vereni buluyoruz. => 900000.0 rupi
result = df.groupby("payment_schedule")["min_salary"].max()["Mounthly"] 

## aylık olarak en fazla maaş veren iş ilanlarının bilgilerine ulaşıyoruz.
result = df[df["min_salary"] == 900000.0]

# result = df["post_spread_time"][846] # => 3 gün önce

## Yorum: "min_salary"de aylık olarak en fazla maaş veren iş ilanlarının bilgisi:
# En Fazla Maaş:    900000.0 rupi
# Şirket İsmi:      Knowledgehut solutions pvt ltd
# İş Başlığı:       Data Analyst
# Yayın Tarihi:     3 gün önce


## "min_salary"de aylık en az maaşı buluyoruz. => 3000.0 rupi
result = df.groupby("payment_schedule")["min_salary"].min()["Mounthly"]

## aylık en az maaşı veren iş ilanları bilgisi için
result = df[df["min_salary"] == 3000.0]

## Yorum: "min_salary"de aylık olarak en az maaş veren iş ilanları bilgisi;
# En Düşük Maaş:    3000.0 rupi
# Şirket İsmi:      NPPD CARE
# İş Başlığı:       Market Research Analyst
# Yayın Tarihi:     1 gün önce


## "min_salary"nin aylık ortalama maaş bilgisi. => 35181.57 rupi
result = df.groupby("payment_schedule")["min_salary"].mean()["Mounthly"]

## "min_salary"nin aylık maaş ile iş ilanı sayısı. => 160
result = df.groupby("payment_schedule")["min_salary"].count()["Mounthly"]


## "min_salary" YEARLY ##

## "min_salary"nin yıllık olarak en fazla maaşı: => 5000000.0 rupi
result = df.groupby("payment_schedule")["min_salary"].max()["Yearly"]

## yıllık en fazla maaş veren iş ilanı bilgileri
result = df[df["min_salary"] == 5000000.0]

## Yorum: "min_salary"de yıllık en fazla maaş veren, aynı isimde fakat farklı niteliklerde 2 ilan yayınlamış 1 şirket var
# En Fazla Maaş:    5000000.0
# Şirket İsmi:      BEIING
# İş Başlıkları:    Data Scientis, Data Scientis
# Yayın Tarihleri:  İkiside 26 gün önce


## "min_salary"nin yıllık olarak en düşük maaşı: => 60000.0 rupi
result = df.groupby("payment_schedule")["min_salary"].min()["Yearly"]

## yıllık en düşük maaş veren iş ilanları bilgisi için
result = df[df["min_salary"] == 60000.0]

## Yorum: Tek bir şirket 2 farklı pozisyon için aynı ücretle tek iş ilanı açmış
# En Düşük Maaş:    60000.0 rupi
# Şirket İsmi:      itechnolabs india pvt ltd
# İş Başlıkları:    Machine Learning, Data Scientist
# Yayın Tarihi:     3 gün önce


## "min_salary"nin yıllık ortalama maaş bilgisi => 854296.07 rupi
result = df.groupby("payment_schedule")["min_salary"].mean()["Yearly"]



## "min_salary"nin yıllık maaş ile iş ilanı sayısı. => 242
result = df.groupby("payment_schedule")["min_salary"].count()["Yearly"]


## bu veri setinde standart sapma hesaplamanın bir yolunu bul !!!!



# df["min_mounthly"] = df.groupby("payment_schedule")["min_salary"].value_counts()["Mounthly"]

# result = df["min_mounthly"].head(20)

# def min_mounthly(val):
#     if val == val:


# result = statistics.stdev(df["max_salary"])
"""

result = df["new_job_salary"].head(40)


## month yazan yerleri bulup yeni bir kolona atamasını yapmak için bir fonksiyon.
def choice_count_month(val):
    if val == val:
        if "month" in val:
            if val == "month":
                val = val
            else:
                val = val
        else:
            val = np.nan
    else:
        val = np.nan
    return val


df["month_salary"] = df["new_job_salary"].apply(choice_count_month)
result = df["month_salary"].head(40)

## yeer yazan yerleri bulup yeni bir kolona atamasını yapmak için bir fonkisyon.

def choice_count_year(val):
    if val == val:
        if "yeer" in val:
            if val == "yeer":
                val = val
            else:
                val = val
        else:
            val = np.nan
    else:
        val = np.nan
    return val

df["year_salary"] = df["new_job_salary"].apply(choice_count_year)
result = df["year_salary"].head(20)

def choice_count_hour(val):
    if val == val:
        if "hour" in val:
            if val == "hour":
                val = val
            else:
                val = val
        else:
            val = np.nan
    else:
        val = np.nan
    return val

df["hour_salary"] = df["new_job_salary"].apply(choice_count_hour)
result = df["hour_salary"].head(40)

## "year_salary" değişkeni için düzenleme yapılacak

df["year_salary_column"] = df.year_salary.str.replace("yeer","").str.replace(",","").str.replace(" ","")
df["year_salary_column"] = df["year_salary_column"].str.strip()
result = df["year_salary_column"].head(20)


df["min_year_salary"] = df["year_salary_column"].str.split("-").str[0]
df["min_year_salary"] = df["min_year_salary"].str.strip()
result = df["min_year_salary"].head(20)

df["max_year_salary"] = df["year_salary_column"].str.split("-").str[1]
df["max_year_salary"] = df["max_year_salary"].str.strip()
result = df["max_year_salary"].head(50)


## "month_salary" değişkeni için düzenleme

df["month_salary_column"] = df.month_salary.str.replace("month","").str.replace(",","").str.replace(" ","")
df["month_salary_column"] = df["month_salary_column"].str.strip()
result = df["month_salary_column"].head(20)

df["min_month_salary"] = df["month_salary_column"].str.split("-").str[0]
df["min_month_salary"] = df["min_month_salary"].str.strip()
result = df["min_month_salary"].head(20)

df["max_month_salary"] = df["month_salary_column"].str.split("-").str[1]
df["max_month_salary"] = df["max_month_salary"].str.strip()
result = df["max_month_salary"].head(20)



## "hour_salary" değişkeni için düzenleme
result = df["hour_salary"].value_counts()
df["hour_salary"] = df.hour_salary.str.replace("hour", "").str.replace(" ","").str.replace(",","")
df["hour_salary"] = df["hour_salary"].str.strip()
result = df["hour_salary"].head(40)




result = df[["min_year_salary","max_year_salary"]].head(50)
result1 = df[["min_month_salary","max_month_salary"]].head(50)
result2 = df["hour_salary"].head(50)


## job_salary değişkenini 5 farklı kolona ayırdık. 1. min_year_salary, 2. max_year_salary, 3. min_month_salary, 4.max_month_salary, 5. hour_salary

# df.info()


## oluşturduğumuz 5 kolon içinde veri tipi object olarak görünüyor. Bunları int veri türüne çevireceğiz.


result = df[["job_salary","min_year_salary","max_year_salary","min_month_salary","max_month_salary","hour_salary"]].head(50)

# result = len(df["min_month_salary"])

# df = df.dropna(subset="hour_salary", axis=0)

# result = len(df["hour_salary"])

# "min_year_salary" değişkeninde, satır doluluk sayısı 242,

# "max_year_salary", değişkeninde, satır doluluk sayısı 201,

# "min_month_salary" değişkeninde, satır doluluk sayısı 160, 

# "max_month_salary" değişkeninde, satır doluluk sayısı 134,

# "hour_salary" değişkeninde satır doluluk sayısı 3'tür.


## oluşturduğumuz 5 değişkeni str den int e çevirme işlemi

# df["min_year_salary"].info() 

df[["min_year_salary","max_year_salary","min_month_salary","max_month_salary","hour_salary"]] = df[["min_year_salary","max_year_salary","min_month_salary","max_month_salary","hour_salary"]].replace(np.nan, 999999999)

result = df["min_year_salary"].head(50)

df[["min_year_salary", "max_year_salary","min_month_salary","max_month_salary","hour_salary"]] = df[["min_year_salary", "max_year_salary","min_month_salary","max_month_salary","hour_salary"]].astype("int64")
result = df[["min_year_salary","max_year_salary","min_month_salary","max_month_salary","hour_salary"]].head(50)

# df[["min_year_salary","max_year_salary","min_month_salary","max_month_salary","hour_salary"]].info()


df[["min_year_salary", "max_year_salary","min_month_salary","max_month_salary","hour_salary"]] = df[["min_year_salary","max_year_salary","min_month_salary","max_month_salary","hour_salary"]].replace(999999999, np.nan)
result = df[["min_year_salary","max_year_salary","min_month_salary","max_month_salary","hour_salary"]].head(50)

# df[["min_year_salary","max_year_salary","min_month_salary","max_month_salary","hour_salary"]].info()


# sayısal işlem yapacağımız 5 değişkende str'den int'e çevrildi.

## ANALİZ ##

# "min_month_salary" değişkeni için

# "min_month_salary"i baz alarak, bütün NaN değerleri siliyoruz.

import statistics

df = df.dropna(subset = ("min_month_salary"), axis=0)
result = df["min_month_salary"].head(50)

result = df["min_month_salary"].mean() # 35181.56875 rupi
result = df["min_month_salary"].max() # 900000.0 rupi
result = df["min_month_salary"].min() # 3000.0 rupi

# standart sapma => 75908.3896614549
result = statistics.pstdev(df["min_month_salary"])

## harmonik(merkezi ortalama) => 17688.612284433988
result = statistics.harmonic_mean(df["min_month_salary"])

## median(orta değerimiz) => 20000.0  (bu değeri bulabilmek için önce sort_value ile birlikte küçükten büyüğe sıralıyoruz.)
# df["min_month_salary"] = df.sort_values("min_month_salary")["min_month_salary"]
result = statistics.median(df["min_month_salary"])



## Gruplandırılmış Medyan => 20000.342105263157
result = statistics.median_grouped(df["min_month_salary"])


## statistics.median_high() hesaplanacakkk !!!!!

## büyük ortanca değer => 20000.0
result = statistics.median_high(df["min_month_salary"])

## küçük ortanca değer => 20000.0
result = statistics.median_low(df["min_month_salary"])


## mode => 25000.0
result = statistics.mode(df["min_month_salary"])

## tüm popülasyonda standart sapma => 75908.3896614549 
result = statistics.pstdev(df["min_month_salary"])

## örneklemde standart sapma => 76146.72114164979
result = statistics.stdev(df["min_month_salary"])

## tüm popülasyonda varyans => 5762083620.995274
result = statistics.pvariance(df["min_month_salary"])

## veri örneğinde varyans => 5798323140.624174
result = statistics.variance(df["min_month_salary"])



















# result = df.iloc[:20, :2]
# result1 = df.iloc[:20, 2:4]
# result2 = df.iloc[:20, 4:6]
# result3 = df.iloc[:20, 6:8]
# result4 = df.iloc[:20, 8:10]
# result5 = df.iloc[:20, 10:12]
# result6 = df.iloc[:20, 12:14]
# result7 = df.iloc[:20, 14:16]





# print(result)
# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)
# print(result6)
# print(result7)