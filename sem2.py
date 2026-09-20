def status(n: float)->str:
    """ Выводит состояние датчика и коровки

    Args:
        n: дробное число-значение датчика
    Return:
        string, текстовая диагностика датчика и коровы
    """
    StatusDatch = "исправен"
    if type(n)!=float:
        return "некорректный тип"
    if n<0:
        return "Отрицательное значение сигнала: " + str(n) + "mA"
    if n==0:
        StatusDatch = "отключен"
        return "Получен сигнал датчика " + str(n)+ "mA, датчик " + StatusDatch
    if (0<n<=3.9 or n>=20.1):
        StatusDatch = "не исправен"
        return "Получен сигнал датчика " + str(n)+ "mA, датчик " + StatusDatch

    temp_cow = (n-4)*75/(20-4)

    if 37.5<=temp_cow<=39:
        cow_status = " с коровкой все хорошо "
    if 35<=temp_cow<37.4:
        cow_status = " коровка замерзла, требуется обогрев "
    if 39.1<=temp_cow<=39.5:
        cow_status = " коровка перегрелась, требуется охлаждение "
    if temp_cow>39.6:
        cow_status = " коровка заболела "
    if temp_cow < 34.9:
        cow_status = " коровка плохо себя чувствует или проблемы с датчиком"
    return (f"Получен сигнал датчика {n}mA, датчик {StatusDatch}, температура {temp_cow} градусов, {cow_status}")

for c in range(-100,250):
    print(status(c/10))
