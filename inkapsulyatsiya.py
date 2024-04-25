class Shaxs:
    def __init__(self, ism, yosh,  millat, manzil):
        self.ism = ism
        self.yosh = yosh
        self.millat = millat
        self.manzil = manzil

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        return f"{self.ism}, {self.yosh} yosh, {self.millat}, {self.manzil}"

class Talaba(Shaxs):
    def __init__(self, ism, yosh, millat, manzil, student_id, kurs, yonalishi, oqituvchi):
        super().__init__(ism, yosh, millat, manzil)
        self.student_id = student_id
        self.kurs = kurs
        self.yonalishi = yonalishi
        self.oqituvchi = oqituvchi

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def e(self):
        return f"{self.ism}, {self.yosh} yosh, {self.millat}, {self.manzil}, ID: {self.student_id}, \
            Kurs: {self.kurs}, Yo'nalishi: {self.yonalishi}, \
             O'qituvchi: {self.oqituvchi}"

class Foydalanuvchi:
    def __init__(self, username, email):
        self.username = username

        self.email = email

    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

class Admin(Foydalanuvchi):
    def ban_user(self, user):
        print(f"{user.username} bloklandi")

