#SHARTLARI
#Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)

#Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
#get_info() metodi avti haqida to'liq ma'lumotni matn ko'rinishida qaytarsin
#Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
#update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin
#Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)
#Avtosalonga yangi avtomobillar qo'shish uchun metod yozing
#Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing

class Avto:
    def __init__(self,model,rang,karobka,narh):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narh = narh
        self.km = 0
        
    def get_info(self):
        "Bul metod mashin haqqinda magliwmat qaytaradi"
        info = f"model: {self.model} rang: {self.rang}."
        info += f"karobka: {self.karobka} narh: {self.narh}"
        return info
    
    def update_km(self,new_km):
        yangi = self.km + new_km
        self.km = yangi
        return self.km

class Avtosalon:
    def __init__(self,salon_nomi,manzili,sotuvdagi_avtomobil):
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.sotuvdagi_avtomobillar = []
        
    def add_car(self,*car):
        self.sotuvdagi_avtomobillar.append(car)
        return self.sotuvdagi_avtomobillar
        
    def avtomobillar(self):
        return self.sotuvdagi_avtomobillar
    

birinchi = Avtosalon('UzAvto', 'Xojeli rayoni', 'malibu')
