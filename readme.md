# Email Classifier with AI Integration

This project is a web-based email classification tool designed for the finance sector. It allows users to quickly classify emails as either **productive** or **unproductive**, and automatically suggests responses using AI. If the AI is unavailable or returns an error, a manual fallback system ensures continuous functionality.

Deploy URL: https://devdantas.pythonanywhere.com/
---

## Features

- **User Authentication**: Simple login screen with static credentials to access the dashboard.
- **AI-Powered Classification**: Uses Google Gemini (gemini-2.0-flash-exp) to classify emails and generate suggested responses.
- **Manual Fallback**: A keyword-based system that generates responses if the AI is unavailable.
- **File and Text Input**: Supports both direct text input and file uploads (TXT or PDF).
- **Interactive Dashboard**: Real-time processing with status indicators and results display.
- **Responsive Design**: Styled with TailwindCSS for a clean and modern interface.

---

## Usage

1. **Login**: Access the web application with pre-defined credentials.
2. **Submit Email**: Paste the email content in the textarea or upload a `.txt` or `.pdf` file.
3. **Process**: Click the "Process" button. A spinner indicates that the system is working.
4. **View Results**: The system displays the classification category and a suggested response. It also indicates whether the response was generated manually or by the AI.

---

## Technologies

- **Backend**: Python 3.13, Flask
- **AI Integration**: Google Gemini API
- **PDF Handling**: PyPDF2
- **Natural Language Processing**: NLTK
- **Frontend**: HTML, JavaScript, TailwindCSS

---

## Setup Instructions (Local Development)

1. Clone the repository.

2. Install all dependencies:
    pip install flask PyPDF2 nltk python-dotenv google-generativeai

3. Configure your AI API key and credentials in a `.env` file:
    GEMINI_API_KEY=your_api_key_here\
    LOGIN:your_login\
    PASSWORD:your_password

4. Run the Flask application:
    python app.py

5. Open your browser at `http://localhost:5000`.

---

## Notes

- The AI key is required for full functionality. Without it, the system will fallback to the manual response mechanism.
- Authentication is simple and meant for demonstration purposes. In a production environment, more secure user management should be implemented.

---

## Author

**Lucas Dantas** – [LinkedIn](https://www.linkedin.com/in/lucas-de-sousa-dantas/)
