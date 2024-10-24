import calendar
from datetime import date

EMA_FECHA_NACIMIENTO = date(1959, 10, 26)
CSVP_FECHA_NACIMIENTO = date(1999, 12, 12)
CSVP_HIJO_FECHA_NACIMIENTO = date(2016, 2, 8)

def diferencia_tiempo(date_inicio, date_final):
    days, months, years = 0, 0, 0

    iday, imonth, iyear = date_inicio.day, date_inicio.month, date_inicio.year
    eday, emonth, eyear = date_final.day, date_final.month, date_final.year

    years = eyear - iyear - 1
    if imonth == emonth:
        months = 11
        if iday == eday:
            months = 0
            years += 1
    elif emonth > imonth:
        years += 1
        months = (emonth - imonth)
    else:
        months = (12- imonth) + emonth

    days = eday - iday
    if eday > iday:
        months += 1
        day_name, dias_del_mes = calendar.monthrange(eyear, emonth)
        days = dias_del_mes - iday + eday
    else:
        days = iday - eday

    return years, months, days

def estimar_tiempo(fecha_final):
    print(EMA_FECHA_NACIMIENTO, " -> ", fecha_final)
    print(diferencia_tiempo(EMA_FECHA_NACIMIENTO, fecha_final))
    print(CSVP_FECHA_NACIMIENTO, " -> ", fecha_final)
    print(diferencia_tiempo(CSVP_FECHA_NACIMIENTO, fecha_final))
    print(CSVP_HIJO_FECHA_NACIMIENTO, " -> ", fecha_final)
    print(diferencia_tiempo(CSVP_HIJO_FECHA_NACIMIENTO, fecha_final))


if __name__ == '__main__':
    hoy = date.today()
    estimar_tiempo(hoy)
    print('====================================================')
    estimar_tiempo(CSVP_HIJO_FECHA_NACIMIENTO)