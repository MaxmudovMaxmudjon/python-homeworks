import datetime as dt
def tugilgan_kun(birth_date):
    today = dt.date.today()
    age = today - birth_date
    years = age.days//365 
    months = (age.days % 365)//30 
    days = (age.days % 365) % 30 
    return years,months,days
birth_date_str = input("Tugilgan kuningizni (yil-oy-kun formatida) kiriting: ")
birth_date = dt.datetime.strptime(birth_date_str,"%Y-%m-%d").date()
years,months,days = tugilgan_kun(birth_date)
print("Siz", years, "yil,", months,"oy,", days, "kun oldin tug'ilgansiz")
print(f"siz {years} yil, {months} oy, {days} kun oldin tugilgansiz")
