import googlemaps
from datetime import datetime

def get_restaurant_info(api_key, location, keyword='restaurant'):
    # create a Google Maps API client
    gmaps = googlemaps.Client(key=api_key)

    # Perform a Places API text search for restaurants in the specified location
    places_result = gmaps.places(query=f'{keyword} in {location}', type='restaurant')

    # Check if any results were found
    if not places_result['results']:
        print(f"No {keyword}s found in {location}.")
        return

    # Get the details of the first restaurant
    place_id = places_result['results'][0]['place_id']
    place_details = gmaps.place(place_id=place_id, fields=['name', 'opening_hours'])

    # Display restaurant information
    restaurant_name = place_details['result']['name']
    opening_hours = place_details['result']['opening_hours']['weekday_text']

    print(f"Restaurant Name: {restaurant_name}")
    print("Opening Hours:")
    for hours in opening_hours:
        print(hours)

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual Google Maps API key
    api_key = 'YOUR_API_KEY'

    # Specify the location (e.g., city or coordinates)
    location = 'Nairobi.'

    get_restaurant_info(api_key, location)
