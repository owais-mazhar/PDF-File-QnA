# PDF Q&A Streamlit App

This Streamlit app allows you to upload PDF documents, create an index of their contents, and query them for responses using a vector-based search engine.

## Features

- Upload multiple PDF files for indexing.
- Query the indexed documents to get responses.
- Simple and intuitive user interface.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/owais-mazhar/pdf-qna-streamlit.git
   cd pdf-qna-streamlit
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the root directory with your Google API key:
     ```
     GOOGLE_KEY=your_google_api_key_here
     ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

5. Open your web browser and go to `http://localhost:8501` to view and interact with the app.

## Usage

- Upload PDF files using the file uploader.
- Enter your query in the text input and click "Enter" to get a response.

## Contributing

Contributions are welcome! If you have any ideas for improvements, feel free to fork the repository and submit a pull request.