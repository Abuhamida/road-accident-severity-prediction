import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"

class TestModelDeployment(unittest.TestCase):

    def test_home_page_status_code(self):
        """Test if the home page returns 200 OK."""
        response = requests.get(BASE_URL + "/")
        print("HOME PAGE RESPONSE:", response.text)
        self.assertEqual(response.status_code, 200)

    def test_prediction_valid_data(self):
        """Test prediction endpoint with valid data."""
        form_data = {
            "num_vehicles": 2,
            "time": 14,
            "road_class": "A",
            "road_surface": "Wet / Damp",
            "lighting": "Darkness: street lights present and lit",
            "weather": "Fine without high winds",
            "casualty_severity": "Slight",
            "sex_of_casualty": "Male",
            "age_of_casualty": 35,
            "type_of_vehicle": "Car",
            "age_group": "60-69",
            "vehicle_group": "Two-Wheeled Vehicle"
        }
        response = requests.post(BASE_URL + "/", data=form_data)
        print("VALID PREDICTION RESPONSE:", response.text)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Prediction", response.text)  # Adjust based on actual HTML output

    def test_prediction_invalid_data(self):
        """Test prediction endpoint with invalid data (e.g., invalid number of vehicles)."""
        form_data = {
            "num_vehicles": "InvalidNumber",
            "time": "14",
            "road_class": "A",
            "road_surface": "Dry",
            "lighting": "Daylight",
            "weather": "Clear",
            "casualty_severity": "Fatal",
            "sex_of_casualty": "Male",
            "age_of_casualty": "30",
            "type_of_vehicle": "Car",
            "age_group": "60-69",
            "vehicle_group": "Two-Wheeled Vehicle"
        }
        response = requests.post(BASE_URL + "/", data=form_data)
        print("INVALID PREDICTION RESPONSE:", response.text)
        self.assertEqual(response.status_code, 200)
        self.assertIn("error", response.text.lower())

if __name__ == '__main__':
    unittest.main()
