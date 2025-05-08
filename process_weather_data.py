from get_data import *
import math

# Replace 'your_api_key' with your actual API key
# api_key = '663a5a2db78b45e7aa3140130240608'
# location = '52.2370,21.017'
# future_jump = 3  #2 or 3
#
#
#
# #getting_forecast
# hourly_forecast = get_hourly_forecast(api_key, location, future_jump)[4:22]

class CheckLocation:
    def __init__(self, hourly_forecast):

        self.forecast = hourly_forecast

    def show_forecast(self):
    #Printing forecast
        for hour in self.forecast:

            time = hour['time']
            temp_c = hour['temp_c']
            wind_kph = hour['wind_kph']
            wind_degree = hour['wind_degree']
            chance_of_rain = hour['chance_of_rain']
            precip_mm = hour['precip_mm']
            print(f"Time: {time}, Temp (C): {temp_c}, Wind: {wind_kph}, Dir: {wind_degree}, Rain: {chance_of_rain}%, Rain_mm: {precip_mm}mm")
        print("\n\n")
    def not_rainy(self):


        total_rain = 0

        for hour in self.forecast:

            if hour['chance_of_rain'] > 10 and hour['precip_mm'] > 0.5:
                indicator = 0
                print("chance: " + str(hour['chance_of_rain']) + "% \t" + "height:" + str(hour['precip_mm']))
                return False

            total_rain += hour['precip_mm']
            if total_rain > 1.5:
                indicator = 0
                print("Total mm: " + str(total_rain))
                return False

        return [total_rain, 1]

    def hour_vectors(self):

        w = [[h['wind_kph'] * math.sin(math.radians(h['wind_degree'])), h['wind_kph'] * math.cos(math.radians(h['wind_degree']))] for h in self.forecast]

        return w



    def sum_vector(self):

        w = self.hour_vectors()

        v = [sum(vec[0] for vec in w)/len(w), sum(vec[1] for vec in w)/len(w)]
        return v


    def vec_len(self, w):
        len = math.sqrt(w[0] * w[0] + w[1] * w[1])
        return len

    def stably_windy(self):

        summary_vector = self.sum_vector()
        summary_len = self.vec_len(summary_vector)

        #Getting summary vector angle
        cosinus = summary_vector[1]/summary_len
        sinus = summary_vector[0] / summary_len
        summary_degree = math.degrees(math.asin(sinus))

        if cosinus < 0:
            summary_degree = 180 - summary_degree

        if summary_degree < 0:
            summary_degree += 360


        #Getting descending list of modules of vector differences
        vectors = self.hour_vectors()
        difference_vectors = [[summary_vector[0] - vector[0], summary_vector[1] - vector[1]] for vector in vectors]
        difference_modules = sorted([self.vec_len(vec) for vec in difference_vectors], reverse=True)


        #For Debuging
        # print("Vectors: " + str(vectors))
        # print("Difference vectors: " + str(difference_vectors))
        # print("Difference modules: " + str(difference_modules))
        # print("4th difference: " + str(difference_modules[3]))
        # print("Average wind speed coordinates: " + str(summary_vector))
        # print("Average wind speed km/h: " + str(summary_len))
        # print("Average wind angle: " + str(summary_degree))


        #Checking if summary wind is sufficient and if wind isn't changing too much
        if summary_len < 8:
            print("Słaby potencjał wiatru")
            return False

        if difference_modules[3] > 1.4 * summary_len:
            print("Wiatr zbytnio kręci")
            return False

        return [summary_len, summary_degree]

    def check(self):

        indicator = 1

        self.show_forecast()
        wind = self.stably_windy()
        rain = self.not_rainy()

        if not rain:
            indicator = 0

        if not wind:
            indicator = 0

        if indicator == 1:

            return 1, round(wind[0], 1), round(wind[1], 0), round(rain[0], 2)
        else:
            print("Jest źle!")
            return 0












