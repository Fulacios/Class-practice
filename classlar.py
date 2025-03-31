class User:
    def __init__(self,ism,foydalanuvchi_ismi,email,t_yil):
        self.name = ism
        self.nickname = foydalanuvchi_ismi
        self.gmail = email
        self.year = t_yil
    
    
    def get_age(self,this_year):
        return this_year - self.year
    
    def __repr__(self):
        info = f"Name: {self.name} Nickname: {self.nickname} "
        info += f"Email: {self.gmail} Year: {self.year}" 
        return info
    

user1 = User('Name', 'nickname', 'example.gmail.com', 2000)
