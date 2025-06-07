# PersonaAI

PersonaAI is an AI-powered chatbot application designed to simulate personalized conversations. It leverages state-of-the-art language models and a simple interface to allow users to interact with custom personas in a chat-based environment.

---

## Features

- Custom persona-based conversations
- Streamlit-powered user interface
- Modular architecture for easy expansion
- Static asset support (images, avatars, etc.)
- Lightweight and easy to deploy

---

## Project Structure
```
PersonaAI/
├── assets/ # Static assets (images, etc.)
├── app.py # Main application (Streamlit)
├── bot.py # Core bot logic and responses
├── requirements.txt # Python dependencies
└── .gitignore # Files to ignore in Git versioning
```
---

## File Descriptions
* **`app.py`**: Presumably the main entry point of the application. Without access to the code, specific functionalities cannot be detailed.
* **`bot.py`**: Likely contains the implementation of the AI bot or chatbot functionalities. Details are unavailable without code access.
* **`requirements.txt`**: Lists the Python packages required to run the project. The specific dependencies are not provided in the available information.
* **`assets/`**: Intended for storing static assets such as images, configuration files, or other resources. The contents are unspecified.

---
## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/parasmunoli/PersonaAI.git
cd PersonaAI
```
2. Create and Activate Virtual Environment 
```bash
python -m venv venv
source venv/bin/activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
## Usage
Run the Application
```bash
streamlit run app.py
```
This will launch the web application in your browser.

## Requirements
All dependencies are listed in requirements.txt. If you are using Streamlit, you might see packages like:

```nginx
streamlit
openai
pillow
```
Ensure the API keys or environment variables (if needed) are properly configured.

## Assets
The `assets/` folder may contain:
Avatar images
