
from process_weather_data import *
from coordinates import *
from notification_manager import *
import datetime


today = datetime.date.today()
weekday = today.weekday()






start_lat = 52.2370
start_lon = 21.0175
distance_km = 200   # Distance to check weather



def do_the_check(day_jump):


    check = CheckLocation(get_hourly_forecast('78d8bc785339415f882171812240808', f"{start_lat},{start_lon}", day_jump)[4:21])
    start_loc_check = check.check()


    if start_loc_check:
        new_coordinates = move_coordinates(start_lat, start_lon, distance_km, start_loc_check[2])
        print(new_coordinates)

        check_second = CheckLocation(get_hourly_forecast('78d8bc785339415f882171812240808', new_coordinates, day_jump)[4:21])
        end_loc_check = check_second.check()

        if end_loc_check:

            print("Jest dobrze!")
            print(f"Gdzie: {new_coordinates}")
            print(f"Potencjał wiatru w tym miejscu: {end_loc_check[1]}km/h, kierunek wiatru w tym miejscu: {end_loc_check[2]}st.")
            print(f"Potencjał wiatru w Warszawie: {start_loc_check[1]}km/h, kierunek wiatru w Warszawie: {start_loc_check[2]}st.")
            print(f"Suma opadów: {end_loc_check[3]}mm")
            text = f"Gdzie:\nhttps://www.google.com/maps/place/{new_coordinates}/@{new_coordinates},9z\n\nPotencjał wiatru w tym miejscu: {end_loc_check[1]}km/h,\nkierunek wiatru w tym miejscu: {end_loc_check[2]}st.\nPotencjał wiatru w Warszawie: {start_loc_check[1]}km/h,\nkierunek wiatru w Warszawie: {start_loc_check[2]}st.\nSuma opadów: {end_loc_check[3]}mm\n"


            print(text)
            return text
        else:
            return False

    else:
        return False


if (weekday == 4):


    jutro = do_the_check(2)
    pojutrze = do_the_check(3)
    text = "Rower! :)\n\n"


    if jutro:
        text += "- Sobota\n" + jutro
    if pojutrze:
        text += "- Niedziela\n" + pojutrze

    if len(text) > 10:
        sms = NotificationManager()
        sms.send_sms(text)
else:
    print("to nie dzisiaj")