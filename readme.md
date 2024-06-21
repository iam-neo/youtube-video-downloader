# YouTube Video Downloader

A simple web application to download YouTube videos in different resolutions. Built with Python, Flask, and `pytube`.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Input a YouTube video URL to get available download options.
- Display the video's thumbnail.
- Choose from different video resolutions to download.

## Requirements

- Python 3.x
- Flask
- pytube

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/iam-neo/youtube-video-downloader.git
    cd youtube-video-downloader
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install flask pytube
    ```

## Usage

1. Run the Flask application:

    ```sh
    python app.py
    ```

2. Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. Enter a YouTube video URL and submit the form.

4. View the video's thumbnail and select a video resolution to download.

## File Structure

```
youtube-video-downloader/
│
├── app.py
├── templates/
│ └── index.html
└── README.md
```

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML template for the web interface.
- `README.md`: This file.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.
