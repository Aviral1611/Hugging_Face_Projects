# NSFW Image Detection Web Application

This project is a web application that uses the Hugging Face API to detect Not Safe For Work (NSFW) content in images. Users can upload an image, and the application will return predictions about the content's safety rating.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Configuration](#api-configuration)
- [Contributing](#contributing)
- [License](#license)

## Features
- Web interface for image upload
- Integration with Hugging Face's NSFW image detection model
- Display of prediction results with labels and confidence scores

## Prerequisites
- Python 3.x
- Flask
- `requests` library
- `python-dotenv` library

## Installation

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the project directory:**
    ```bash
    cd <project-directory>
    ```

3. **Install the required packages:**
    ```bash
    pip install flask requests python-dotenv
    ```

4. **Create a `.env` file** in the root directory and add your Hugging Face API key:
    ```env
    HUGGING_FACE_API_KEY=your_api_key_here
    ```

## Usage

1. **Run the Flask application:**
    ```bash
    python web.py
    ```

2. **Open a web browser** and navigate to:
    ```
    http://localhost:81
    ```

3. **Upload an image** using the provided form.

4. **View the NSFW prediction results** displayed on the page.

## API Configuration

This project uses the Hugging Face API for NSFW image detection. The specific model used is `Falconsai/nsfw_image_detection`. Make sure you have a valid API key from Hugging Face to use this service.

## Contributing

Contributions to improve the project are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push to your fork and submit a pull request.

