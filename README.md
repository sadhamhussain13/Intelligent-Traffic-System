# Intelligent Traffic System for Urban Conditions Using Real-Time Vehicle Tracking

## Project Overview

This project aims to develop an intelligent traffic management system for urban conditions using real-time vehicle tracking. The system leverages YOLO (You Only Look Once) for object detection and tracking vehicles. The traffic signals are adjusted dynamically based on the number of vehicles detected by YOLO, ensuring efficient traffic flow. A GUI created with Tkinter allows for easy interaction and monitoring of the system.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)



## Features

- Real-time vehicle detection and tracking using YOLO.
- Dynamic adjustment of traffic signals based on vehicle count.
- User-friendly GUI for monitoring and controlling the traffic system.
- Support for video input to simulate real-world traffic scenarios.

## Technologies Used

- Python
- YOLO for object detection
- OpenCV for video processing
- Tkinter for GUI


## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/intelligent-traffic-system.git
    cd intelligent-traffic-system
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Download YOLO weights:**
   
   Download the pre-trained YOLO weights from the official YOLO website or any other source and place them in the `yolo` directory.

## Usage

1. **Run the application:**

    ```sh
    python main.py
    ```

2. **Load a video for processing:**
   
   Load a video file as Input that will be used for vehicle detection and traffic signal management.

3. **Monitor and control traffic signals:**
   
   The GUI will display real-time vehicle counts and allow you to see how traffic signals are adjusted based on the detected traffic.


