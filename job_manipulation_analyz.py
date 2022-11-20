from posixpath import split
from statistics import stdev
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
import missingno as msno
import re


df = pd.read_csv("c:/Users/ruzga/Desktop/Veri Bilimi/Python/pandas/job_dataset.csv")

# df.info()

# There are 1583 observations and 8 in the data set. (Veri setinde 1583 gözlem ve 8 adet değişken vardır.)

#(Row (Satır) => 1583)
#(Column (Sütun) => 8)

# Except for job_salary, the other columns do not have null values. (job_salary haricinde diğer kolonlarda kayıp gözlem yoktur.)
    # 1178 Null value. (1178 boş değer.)

# All columns have object data type. (Değişkenlerin hepsi object veri tipine sahiptir.)

# Let's look at the top 5 and last 5 records to get an idea. (Fikir elde etmek için ilk 5 ve son 5 kayıta bakalım.)

result = df.head()
result1 = df.tail()

# print(result)
# print(result1)


# Column names are descriptive and clearly written. (Sütun adları açıklayıcı ve net bir şekilde yazılmıştır.)

# The text looks fine with no typos. (Metin, yazım hatası olmadan düzgün görünüyor.)

# We can see that the values in the job_salary variable are both string and float values. There are also observations with minimum and maximum values. (Job_salary değişkenindeki değerlerin hem string hem de float değerler olduğunu görebiliriz. Minimum ve maksimum değerlere sahip gözlemler de vardır.)


# For layout control. (Düzen kontrolü için.)

result = df.iloc[:20, :2]
result1 = df.iloc[:20, 2:4]
result2 = df.iloc[:20, 4:6]
result3 = df.iloc[:20 ,6:8]

# print(result)
# print(result1)
# print(result2)
# print(result3)


# We checked 20 observations in columns of 2. (2'lik sütunlarda 20 gözlemi kontrol ettik.)

"""
"post_date" değişkeni 2 aynı sütuna bölünecek.
"job_salary" değişkeni düzenlenecek.
"today" değişkeni string'den integer'a dönüşecek.
"job_location" değişkenine bir göz atılacak.
"""


# 1- For "post_date" ("post_date" için)

# We will look at the first 20 lines for "post_date". ("post_date" için ilk 20 satıra bakacağız.)
result = df["post_date"].head(20)
# print(result)


# Let's see how many similar observations there are. (Benzer kaç adet gözlem olduğuna bakacağız.)
result = df["post_date"].nunique() # There are 80 identical observations. (80 adet aynı gözlem bulunmaktadır.)
# print(result)


# We looked at how many observations were in "days ago". (Kaç gözlemde "days ago" geçiyor diye baktık.)
result = df[df.post_date.str.contains("days ago")]["post_date"] # It is mentioned in "days ago" in 1415 observations. (1415 gözlemde "days ago" geçiyor.)
# print(result)


# We looked at how many observations were in "day ago". (Kaç gözlemde "day ago" geçiyor diye baktık.)
result = len(df[df.post_date.str.contains("day ago")]["post_date"]) # It is mentioned in "day ago" in 31 observations. (31 gözlemde "day ago" geçiyor.)
# print(result)


# "days ago" or "day ago" is mentioned in a total of 1446 observations. (Toplam 1446 gözlemde "sadasdas" veya "asdasdas" geçmektedir.)

# Let's look at the column names. (Sütun isimlerine bakacağız.)
# result = df.columns

# We separate the "post_date" column from the space and assign the first index to the new column we created with the name "post_date_days". ("post_date" kolonunu boşluktak itibaren ayırıp, 1. indexini "post_date_days" ismiyle oluşturduğumuz yeni kolona atıyoruz.)
df["post_date_days"] = df["post_date"].str.split(" ").str[1]
result = df["post_date_days"].head() # We got the indexes showing how many days ago it was. (Kaç gün önce olduğunu belirten indexleri aldık.)
# print(result)

# We will look at how many non-repeating observations are in the newly created column. (Yeni oluşturulan sütunda kaç tane tekrarlanmayan gözlem olduğuna bakacağız.)
result = df["post_date_days"].nunique() # There are 34 unrepeatable observations. (34 adet tekrarlanmayan gözlem bulunmaktadır.)
# print(result)


#We deleted the string data "day ago", "days ago" and "+" from the "post_date" variable and created a new variable called "new_post_date". ("post_date" değişkeninden "day ago", "days ago" ve "+" string türündeki verileri silerek "new_post_date" isminde yeni bir değişken oluşturduk.)
df["new_post_date"] = df.post_date.str.replace("day ago","").str.replace("days ago","").str.replace("+","")
df["new_post_date"] = df["new_post_date"].str.strip()
result = df["new_post_date"]
# print(result)


# We looked at how many unique observations there are in the "new_post_date" variable. ("new_post_date" değişkeninde kaç adet benzersiz gözlem olduğuna baktık.)
result = df["new_post_date"].nunique() # TThere are 79 unrepeatable observations. (79 adet tekrarlanmayan gözlem bulunmaktadır.)
# print(result)

# We split the observations in "new_post_date" with a space. ("new_post_date" değişkenindeki her bir gözlemi boşluktan itibaren böldük.)
df["new_post_date"] = df["new_post_date"].str.split()
result = df["new_post_date"].head(50)
# print(result)

# We found 79 different but repetitive observations. (79 adet birbirinden farklı fakat kendi içerisinde tekrar eden gözlemleri buluyoruz.)
result = df["new_post_date"].value_counts()[0:50]
result1 = df["new_post_date"].value_counts()[50:100]
# print(result)
# print(result1)


# By creating a def function, we separate the processed data such as "Posted30" and "Posted6" into separate columns by fixing them as "Posted 30" and "Posted 6". (def fonksiyonu oluşturarak "Posted30" ve "Posted6" gibi işlenmiş verileri, ayrı sütunlara bölmek için "Posted 30" ve "Posted 6" şeklinde düzeltiyoruz.)

def half_counts(val):
    if val == val:
        if "Posted6" in val:
            if "(" in val:
                val = re.sub("\(Posted6\)","Posted 6", val)
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
df["new_post_date"] = df["new_post_date"].str.strip()


result = df["new_post_date"].value_counts()[0:50]
result1 = df["new_post_date"].value_counts()[50:100]
# print(result)
# print(result1)



# We split the "new_post_date" column into 2 different columns. ("post_situation" recruitment status, "post_spread_time" publication date.) [("new_post_date" kolonunu 2 farklı kolona ayırdık. ("post_situation" işe alım durumu, "post_spread_time" yayınlanma tarihi.)]

df["post_situation"] = df["new_post_date"].str.split(" ").str[0]
df["post_spread_time"] = df["new_post_date"].str.split(" ").str[1]

# We deleted the leading and trailing space characters for the generated columns. (Oluşturulan kolonlar için başta ve sondaki boşluk karakterlerini sildik.)
df["post_situation"] = df["post_situation"].str.strip()
df["post_spread_time"] = df["post_spread_time"].str.strip()
result = df[["post_situation","post_spread_time"]].head(10)
# print(result)

# The sum of the observations with empty elements was checked for the 2 different columns created. (Oluşturulan 2 farklı kolon için boş elemanlı gözlemlerin toplamı kontrol edildi.)
result = df[["post_situation","post_spread_time"]].isnull().sum() # 0 empty observations in the "post_situation" variable, 89 blank observations in the "post_spread_time" variable. ("post_situation" değişkeninde 0 boş gözlem, "post_spread_time" değişkeninde 89 boş gözlem.)
# print(result)

## For "post_spread_time". ("post_spread_time" için.)
# We looked at how many different observations there are in the "post_spread_time" variable. ("post_spread_time" değişkeninde kaç farklı gözlem olduğuna baktık.)
result = df["post_spread_time"].nunique() # There are 33 different observations. (33 adet farklı gözlem bulunmaktadır.)
# print(result)

# Removed "posted" and "in progress" values from the "post_spread_time" variable. ("post_spread_time" değişkeninden "posted" ve "ongoing" değerleri silindi.)
df["post_spread_time"] = df.post_spread_time.str.replace("posted", "").str.replace("ongoing", "")
# result = df.info() # There are 89 empty observations for "post_spread_time". ("post_spread_time" için 89 adet boş gözlem var.)
# print(result)

# We deleted the leading and trailing whitespace characters and printed the first 40 observations. (Baştaki ve sondaki boşluk karakterlerini sildik ve ilk 40 gözlemi yazdırdık.)
df["post_spread_time"] = df["post_spread_time"].str.strip()
result = df["post_spread_time"].head(40)
# print(result)


# We deleted the "submitted" and "in progress" values and assigned "np.nan", that is, "NaN", to the blank observations. ("posted" ve "ongoing" değerlerinin silinmesiyle boş kalan gözlemlere "np.nan" yani "NaN" atadık.)
df["post_spread_time"] = df["post_spread_time"].replace("", np.nan)
result = df["post_spread_time"].head(50)
# print(result)


# Different elements were examined for the column and it was observed that 31 different data from 32 remained. (Kolon için farklı elemanlara bakıldı ve 32 'den 31 adet birbirinden farklı veri kaldığı gözlemlendi.)
result = df["post_spread_time"].nunique()
# print(result)


# For str-int we filled in the blanks with "99999". (str-int dönüşümü için boş değerleri "99999" sayısı ile doldurduk.)
df["post_spread_time"] = df["post_spread_time"].replace(np.nan, 99999)

# We changed the observations that read "30+" to "30". ("30+" yazan gözlemleri "30" olarak değiştirdik.)
df["post_spread_time"] = df["post_spread_time"].replace("30+",30)


# => We looked at all the column information and the "post_spread_time" column has 89 blank data and no more blank data. (Bütün kolon bilgilerine baktık ve "post_spread_time" kolonunda 89 tane boş veri varken şimdi boş veri kalmamış.)
# df.info()


# After editing we changed the structure of "post_spread_time" variable from "str" to "int64". (Düzenlemelerden sonra "post_spread_time" değişkeninin yapısını "str"yerine "int64" olara değiştirdik.)
df["post_spread_time"] = df["post_spread_time"].astype("int64")
df["post_spread_time"].dtypes
result = df["post_spread_time"].head(50)
# print(result)


# After the transformation, we change the observations that we changed to 99999 to np.nan again. (Dönüşüm işleminden sonra 99999 olarak değiştirdiğimiz gözlemleri tekrar np.nan olarak değiştiriyoruz.)
df["post_spread_time"] = df["post_spread_time"].replace(99999, np.nan)
result = df["post_spread_time"].head(50)
# print(result)
# df.info()

    ## For "post_situation". ("post_situation" için.) ##
# We look at how many different values are in the "After status" column. ("post_situation" kolonunda kaç farkl değer var ona bakıyoruz.)
result = df["post_situation"].nunique() # There are 7 different observations. (7 adet farklı gözlem var.)
# print(result)

# We will look at how many different observations there are in the first 50 values. (İlk 50 değerde kaç farklı gözlem var ona bakacağız.)
result = df["post_situation"].value_counts()[0:50]
# print(result)

# => The problem is the observations "PostedPosted", "EmployeeActive", "PostedToday" and "PostedJust". (Sorun olan "PostedPosted", "EmployerActive", "PostedToday" ve "PostedJust" gözlemleri bulunmaktadır.)


# We created a def function to fix the "PostedPosted", "EmployeeActive", "PostedToday" and "PostedJust" observations. ("PostedPosted", "EmployeeActive", "PostedToday" ve "PostedJust" gözlemlerini düzeltmek için bir def fonksiyonu oluşturduk.)
def situation_half(val):
    if val == val:
        if "PostedPosted" in val:
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

# We defined the function we created to the "post_situation" variable and got its output. (Oluşturduğumuz fonksiyonu "post_situation" değişkenine tanımladık ve yazdırdık.)
df["post_situation"] = df["post_situation"].apply(situation_half)
df["post_situation"] = df["post_situation"].str.strip()
result = df["post_situation"].value_counts()[0:50]
# print(result)

# We saw what our operations changed by separating the "post_date" variable and printing the "post_situation" and "post_spread_time" variables that we created together. ("post_date" değişkenini ayırarak oluşturduğumuz "post_situation" ve "post_spread_time" değişkenlerini birlikte yazdırarak yaptığımız işlemlerin neler değiştirdiğini gördük.)
result = df[["post_date" ,"post_situation","post_spread_time"]].head(50)
# print(result)

# Abstract (Özet) #
"""
=> We edited the mixed post_date variable and printed it into a new column called new_post_date. Then we split the new_post_date column into 2 separate columns.

=> Named "post_situation" and "post_spread_time".

=> First we deleted the string expressions in the "post_spread_time" column, assigned null values "99999" and converted the entire column to float. Then we replaced all "99999" values with "NaN" values.

=> In the "post_situation" column we have separated the attached characters. For example, we replaced PostedPosted with Posted.

(=> karışık post_date değişkenini düzenleyip new_post_date adında yeni bir kolona yazdırdık. Sonra new_post_date kolonunuda 2 ayrı     kolona ayırdık.

=> "post_situation" ve "post_spread_time" adında. 

=> ilk olarak "post_spread_time" kolonunda, string ifadeleri sildik boş değerlere "99999" atadık ve bütün kolonu floata çevirdik. Daha sonrasında bütün "99999" değerleri "NaN" değerler ile değiştirdik.

=> "post_situation" kolonunda birleşik yazılmış olan karakterleri ayırdık. Örn PostedPosted yazana yerleri Posted ile değiştirdik.)
"""

# Şimdi diğer kolonlara bakalım..

result = df.iloc[:20, :2]
result1 = df.iloc[:20, 2:4]
result2 = df.iloc[:20, 4:6]
result3 = df.iloc[:20 ,6:8]
result4 = df.iloc[:20 ,8:11]
# print(result)
# print(result1)
# print(result2)
# print(result3)
# print(result4)

# We convert the "today" variable to datetime type. ("today" değişkenini datetime tipine çeviriyoruz.)
df["today"] = pd.to_datetime(df["today"])
# df.info()


## "job_salary" değişkenine göz atacağız

result = df["job_salary"].head(50)
result = df["job_salary"].value_counts()[0:50]
# print(result)

# => For better analysis in "job_ary", we first separate the sections that say "year and month" into a separate column, then create 2 columns "min" and "max" and separate them from each other. ("job_salary" değişkeninde daha rahat istatistiksel analiz yapmak için öncelikle "year" ve "month" yazan yerleri ayrı bir kolona ayırıyoruz, ardından "min" ve "max" şeklinde 2 kolon oluşturup ayırıyoruz.)

# With the def function, we replace "year" with "yeer" and "an" with "a". For more convenient separation. (def fonksiyonu ile "year"olan yerleri "yeer" ve "an" olan yerleri "a" ile değiştirdik. Daha rahat ayırmak için.)
def half_counts(val):
    if val == val:
        if "year" in val:
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

# We created a new column named "new_job_salary" with the function we created. (Oluşturduğumuz fonksiyon ile "new_job_salary" adında yeni bir kolon oluşturduk.)
df["new_job_salary"] = df["job_salary"].apply(half_counts)
df["new_job_salary"] = df["new_job_salary"].str.strip()
result = df["new_job_salary"].head(50)
# print(result)

        
# "We deleted the "₹" currency and spaces in the "new_job_salary" column. (new_job_salary" kolonundan "₹" para birimini ve boşlukları sildik.)
df["new_job_salary"] = df.new_job_salary.str.replace("₹", "").str.replace(" ", "")
result = df["new_job_salary"].head(50)
# print(result)


# We replaced the letters "a" in the "new_job_salary" column with a space " ". For easier splitting. ("new_job_salary" kolonundaki "a" harflerini boşluk " " ile değiştirdik. Daha rahat bölebilmek için.)
df["new_job_salary"] = df.new_job_salary.str.replace("a", " ")
df["new_job_salary"] = df["new_job_salary"].str.strip()
result = df["new_job_salary"].head(50)
# print(result)


# We created and assigned the zeroth string([0]) of the "new_job_salary" column to the "new_salary_column" column. ("new_job_salary" kolonunun, sıfırıncı dizesini([0]) "new_salary_column" kolonu oluşturup oraya atadık.)
df["new_salary_column"] = df["new_job_salary"].str.split(" ").str[0]
df["new_salary_column"] = df["new_salary_column"].str.strip()
result = df["new_salary_column"].head(50)
# print(result)

# In the newly created "new_salary_column" column, we replaced the "-" character with a space. (Yeni oluşturduğumuz "new_salary_column" kolonunda "-" karakterini boşluk ile değiştirdik.)
df["new_salary_column"] = df.new_salary_column.str.replace("-", " ")
result = df["new_salary_column"].head(50)
# print(result)


# We put the zero ([0]) index of the "new_salary_column" column in the "min_salary" column we created. ("new_salary_column" kolonunun sıfırıncı ([0]) indexini oluşturduğumuz "min_salary" kolonuna attık.)
df["min_salary"] = df["new_salary_column"].str.split(" ").str[0]
df["min_salary"] = df["min_salary"].str.strip()
result = df["min_salary"].head(50)
# print(result)


# We put the first ([1]) index of the "new_salary_column" column in the "max_salary" column we created. ("new_salary_column" kolonunun birinci ([1]) indexini oluşturduğumuz "max_salary" kolonuna attık.)
df["max_salary"] = df["new_salary_column"].str.split(" ").str[1]
df["max_salary"] = df["max_salary"].str.strip()
result = df["max_salary"].head(50)
# print(result)


# We check if there is a problem with the columns we created. (Oluşturduğumuz kolonlarda sorun var mı diye kontrol ediyoruz.)
result = df[["min_salary", "max_salary"]].head(50) # The ","'s need to be deleted. ("," lerin silinmesi gerekiyor.)
# print(result)


# We deleted "," the in the "min_salary" variable and then converted the object data type to float.("min_salary" değişkenindeki "," işareti sildik daha sonrasında object olan veri tipini float'a çevirdik.)
df["min_salary"] = df.min_salary.str.replace(",", "")
df["min_salary"] = df["min_salary"].astype("float")
result = df["min_salary"].head(50)
# print(result)


# We deleted "," the in the "max_salary" variable and then converted the object data type to float.("max_salary" değişkenindeki "," işareti sildik daha sonrasında object olan veri tipini float'a çevirdik.)
df["max_salary"] = df.max_salary.str.replace(",", "")
df["max_salary"] = df["max_salary"].astype("float")
result = df["max_salary"].head(50)
# print(result)



# We created the "payment_schedule" column in "new_job_salary" and added the timed indexes. ("new_job_salary"de zaman bildiren indexleri "payment_schedule" kolonunu oluşturup içine attık.)
df["payment_schedule"] = df["new_job_salary"].str.split(" ").str[1]
df["payment_schedule"] = df["payment_schedule"].str.strip()
result = df["payment_schedule"].value_counts()[:50] # "yeer" 242, "month" 160, "hour" 3
# print(result)


# With the def function, we changed "yeer" observations to "Yearly", "month" observations to "Monthly" and "hour" to "Hourly". (def fonkisyonu ile "yeer" olan gözlemleri "Yearly", "month" olan gözlemleri "Monthly" ve "hour" olan gözlemleri "Hourly" olarak değiştirdik.)
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
result = df["payment_schedule"].head(50)
print(result)


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