# 🎙️ Video Transcription with Whisper and Gradio

A simple web application to transcribe audio from video files into text. It uses the **OpenAI Whisper API** for high-accuracy transcription and the **Gradio** library to create an interactive and user-friendly interface.

![Interface Demo](https://i.imgur.com/8aV4WJ1.png)

## ✨ Features

-   **Easy Upload:** Upload video files directly through the web interface (MP4, MOV, AVI, etc.).
-   **Automatic Audio Extraction:** The video's audio is extracted and converted into the ideal format for processing.
-   **Multi-language Transcription:** Support for several languages, including Portuguese, English, Spanish, and others.
-   **Clean Interface:** An intuitive user interface built with Gradio, accessible from any web browser.
-   **Resource Management:** Automatic cleanup of temporary files to save disk space.

## 🚀 Technologies Used

-   **Backend:** [Python 3](https://www.python.org/)
-   **Transcription API:** [OpenAI Whisper](https://platform.openai.com/docs/models/whisper)
-   **Web Interface:** [Gradio](https://www.gradio.app/)
-   **Video Processing:** [MoviePy](https://zulko.github.io/moviepy/)
-   **Key Management:** [python-dotenv](https://github.com/theskumar/python-dotenv)

## 🔧 Prerequisites and Installation

To run this project, you will need Python 3.8+ installed on your machine and an OpenAI API key.

**1. Clone the Repository**
```bash
git clone [https://github.com/your-username/your-repository.git](https://github.com/your-username/your-repository.git)
cd your-repository
