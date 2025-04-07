# Portrait Generator

Portrait Generator is a Flask-based web application that uses OpenAI's DALL-E model to generate portraits based on user input.

## Features

- Accepts user input for gender, hair style, hair color, expression, emotion, and era.
- Generates a portrait using OpenAI's DALL-E model.
- Displays the generated portrait on the web interface.

## Requirements

- Python 3.8 or higher
- Flask
- OpenAI Python SDK
- python-dotenv

## Installation

1. Clone the repository:

   ```bash
   git clone git remote add origin https://github.com/NizamiSevindi/image_generate_with_dall-e.git
   cd portrait_generator
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. Fill out the form on the homepage with the following details:
   - Gender
   - Hair Style
   - Hair Color
   - Expression
   - Emotion
   - Era

2. Submit the form to generate a portrait.

3. View the generated portrait on the same page.

## File Structure

```
Portrait_Generator/
├── templates/
│   └── index.html         # HTML template for the web interface
├── static/
│   ├── css/
│   │   └── styles.css      # Optional CSS for styling
│   └── images/             # Directory for static images
├── app.py                  # Main Flask application
├── .env                    # Environment variables (e.g., OpenAI API key)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Dependencies

The required Python packages are listed in `requirements.txt`. Install them using:

```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.