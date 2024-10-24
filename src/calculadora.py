import calendar
from datetime import date

EMA_FECHA_NACIMIENTO = date(1959, 10, 26)
CSVP_FECHA_NACIMIENTO = date(1999, 12, 12)
CSVP_HIJO_FECHA_NACIMIENTO = date(2016, 2, 8)

def determinar_edad(fecha_inicio, fecha_final):
    years, months, days = calcular_tiempo_transcurrido(fecha_inicio, fecha_final)
    _, dias_en_mes = calendar.monthrange(fecha_final.year, fecha_final.month)
    final_days = days % dias_en_mes
    temp = days // dias_en_mes
    months = months + temp
    final_months = months % 12
    temp = months // 12
    final_years = years + temp

    return final_years, final_months, final_days


def calcular_tiempo_transcurrido(date_inicio, date_final):
    fecha_intermedia_1 = date(date_final.year - 1, date_final.month, date_final.day)
    fecha_intermedia_2 = date(date_final.year - 1, 12, 31)
    fecha_intermedia_3 = date(date_final.year, 1, 1)
    ayear, amonth, aday = diferencia_tiempo(date_inicio, fecha_intermedia_1)
    byear, bmonth, bday = diferencia_tiempo(fecha_intermedia_1, fecha_intermedia_2)
    cyear, cmonth, cday = diferencia_tiempo(fecha_intermedia_3, date_final)

    days = aday + bday + cday + 1
    months = amonth + bmonth + cmonth
    years = ayear + byear + cyear
    
    return years, months, days 

def diferencia_tiempo(date_inicio, date_final):
    days, months, years = 0, 0, 0

    iday, imonth, iyear = date_inicio.day, date_inicio.month, date_inicio.year
    eday, emonth, eyear = date_final.day, date_final.month, date_final.year

    years = eyear - iyear
    months = emonth - imonth
    days = eday - iday

    return years, months, days

def print_resultados(fecha):
    print(f"{fecha[0]} años, {fecha[1]} meses, {fecha[2]} dias")

def estimar_tiempo(fecha_final):
    print(EMA_FECHA_NACIMIENTO, " -> ", fecha_final)
    print_resultados(determinar_edad(EMA_FECHA_NACIMIENTO, fecha_final))
    print('====================================================')

    print(CSVP_FECHA_NACIMIENTO, " -> ", fecha_final)
    print_resultados(determinar_edad(CSVP_FECHA_NACIMIENTO, fecha_final))
    print('====================================================')

    print(CSVP_HIJO_FECHA_NACIMIENTO, " -> ", fecha_final)
    print_resultados(determinar_edad(CSVP_HIJO_FECHA_NACIMIENTO, fecha_final))
    print('====================================================')


if __name__ == '__main__':
    hoy = date(2024, 10, 26)
    estimar_tiempo(hoy)
    print('**************************************************************')
    print('**************************************************************')
    estimar_tiempo(CSVP_HIJO_FECHA_NACIMIENTO)