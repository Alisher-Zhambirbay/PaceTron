import time
import geocoder
from geopy.distance import geodesic


WAIT_TIME = 1
E_WAIT_TIME = 2

def __clear__(): print("\033c", end="")

def calculate_speed(coord1, coord2, time_interval):
    """
    Calculates the speed between two points.
    :param coord1: Coordinates of the first point (latitude, longitude)
    :param coord2: Coordinates of the second point (latitude, longitude)
    :param time_interval: Time interval in seconds
    :return: Speed in km/h
    """
    distance = geodesic(coord1, coord2).kilometers
    speed = distance / (time_interval / 3600)
    return speed

def get_current_location():
    """
    Get the current location using the geocoder library (online service).
    :return: tuple with latitude and longitude
    """
    try:
        g = geocoder.ip('me')
        return g.latlng if g.latlng else (None, None)
    except Exception as e:
        print(f"Error fetching location: {e}")
        return (None, None)

def run_pacetron():
    print("Welcome to PaceTron.")
    print("Tracking your speed in real-time based on GPS coordinates.")
    
    previous_coords = None
    previous_time = None
    
    while True:
        try:
            current_coords = get_current_location()
            
            if current_coords == (None, None):
                print("Unable to get current location.")
                time.sleep(E_WAIT_TIME)
                continue
            
            current_time = time.time()
            
            if previous_coords and previous_time:
                time_interval = current_time - previous_time
                speed = calculate_speed(previous_coords, current_coords, time_interval)
                print(f"Current location: {current_coords}")
                print(f"Previous location: {previous_coords}")
                print(f"Time interval: {time_interval:.2f} seconds")
                print(f"Current speed: {speed:.2f} km/h")
            else:
                print(f"Current location: {current_coords}")
                print("Waiting for next coordinates...")
            
            previous_coords = current_coords
            previous_time = current_time
            
            time.sleep(WAIT_TIME)
            __clear__() # clear after timer. !Fix

        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(E_WAIT_TIME)

if __name__ == "__main__":
    print("Cannot run from here!... Please run pacetron.py")
    exit(-1)
