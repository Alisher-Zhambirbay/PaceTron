# PaceTron

PaceTron is a Python-based application designed to track and display your speed in real-time using GPS coordinates. It calculates speed based on the distance between two points and the time interval between them. The application is particularly useful for tracking movement and speed, using your device's location services.

## Features

- Real-time speed tracking using GPS coordinates
- Calculates speed in kilometers per hour (km/h)
- Lightweight and easy to use
- Supports Windows and Linux environments
- Requires an internet connection for location retrieval

## Installation

To get started with PaceTron, you need to install the required dependencies. The installation process is automated for both Windows and Linux environments.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Alisher-Zhambirbay/PaceTron.git
   cd pacetrons
   ```

2. **Install dependencies:**

   For Windows:

   ```bash
   py -m pip install -r requirements.txt
   ```

   For Linux/macOS:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

   Alternatively, you can run the `pacetron.py` script which will automatically install the required modules.

   ```bash
   python pacetron.py
   ```

3. **Run the application:**

   After installation, simply run the `pacetron.py` script to start tracking your speed:

   ```bash
   python pacetron.py
   ```

   The program will start tracking your real-time speed and display it in kilometers per hour.

## Requirements

- Python 3.x
- `geocoder` library for location retrieval
- `geopy` library for distance calculation

You can install the required libraries by running:

```bash
pip install -r requirements.txt
```

## How it Works

- The application uses the `geocoder` library to get the current location based on your device's IP address.
- It then calculates the speed between the current and previous location using the `geopy.distance.geodesic` function.
- The calculated speed is displayed every second in kilometers per hour.

## Troubleshooting

- If you see the message `Unable to get current location.`, ensure your device has an active internet connection as the application uses an online service to fetch the location.
- If the program fails to import or run correctly, ensure all dependencies are properly installed by checking the `requirements.txt` file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note:** This application works best when connected to the internet, as it relies on online services for location tracking.