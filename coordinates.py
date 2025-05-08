import math

def move_coordinates(lat, lon, distance_km, bearing_degrees):
    # Convert latitude, longitude, and bearing to radians
    lat = math.radians(lat)
    lon = math.radians(lon)
    bearing = math.radians(bearing_degrees)

    # Earth's radius in kilometers
    R = 6371.0

    # Calculate the new latitude
    new_lat = math.asin(math.sin(lat) * math.cos(distance_km / R) +
                        math.cos(lat) * math.sin(distance_km / R) * math.cos(bearing))

    # Calculate the new longitude
    new_lon = lon + math.atan2(math.sin(bearing) * math.sin(distance_km / R) * math.cos(lat),
                               math.cos(distance_km / R) - math.sin(lat) * math.sin(new_lat))

    # Convert the new coordinates back to degrees
    new_lat = round(math.degrees(new_lat), 4)
    new_lon = round(math.degrees(new_lon), 4)

    return f"{new_lat},{new_lon}"


