def day_of_week(day):
    day = day.lower()
    week = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]
    if day in week:
        return week.index(day) + 1
    return 0


t = int(input("Podaj liczbę przypadków"))
while t:
    day_to_check = input("Podaj dzień do sprawdzenia")
    result = day_of_week(day_to_check)
    if result:
        print(result)
    else:
        print("Taki dzień jeszcze nie istnieje :)")
    t -= 1
