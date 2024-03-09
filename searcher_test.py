import unittest
from unittest.mock import patch, MagicMock
from restaurant_search import get_restaurant_info

class TestRestaurantSearch(unittest.TestCase):

    @patch('restaurant_search.googlemaps.Client')
    def test_get_restaurant_info(self, mock_client):
        # Mocking the Google Maps API client
        mock_places_result = {
            'results': [
                {'place_id': 'mock_place_id'}
            ]
        }
        mock_place_details = {
            'result': {
                'name': 'Mock Restaurant',
                'opening_hours': {
                    'weekday_text': ['Monday: 9:00 AM - 5:00 PM', 'Tuesday: Closed', 'Wednesday: 9:00 AM - 5:00 PM']
                }
            }
        }

        mock_gmaps = MagicMock()
        mock_gmaps.places.return_value = mock_places_result
        mock_gmaps.place.return_value = mock_place_details
        mock_client.return_value = mock_gmaps

        # Call the function with mocked data
        result = get_restaurant_info(api_key='mock_api_key', location='Mock City')

        # Assertions
        expected_name = 'Mock Restaurant'
        expected_hours = ['Monday: 9:00 AM - 5:00 PM', 'Tuesday: Closed', 'Wednesday: 9:00 AM - 5:00 PM']

        self.assertEqual(result, None)  # The function currently returns None, modify as needed
        mock_gmaps.places.assert_called_once_with(query='restaurant in Mock City', type='restaurant')
        mock_gmaps.place.assert_called_once_with(place_id='mock_place_id', fields=['name', 'opening_hours'])

        # Check the printed output
        captured_output = self.capsys.readouterr()
        self.assertIn(f"Restaurant Name: {expected_name}", captured_output.out)
        for expected_hour in expected_hours:
            self.assertIn(expected_hour, captured_output.out)

if __name__ == '__main__':
    unittest.main()
