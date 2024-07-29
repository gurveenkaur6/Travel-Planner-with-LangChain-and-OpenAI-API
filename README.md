# AI Travel Planner

Welcome to the AI Travel Planner! This application leverages the power of OpenAI's language model to help you plan your trips with personalized itineraries and local recommendations. With a user-friendly interface built using Streamlit, you can easily input your travel destination and preferences to receive a tailored travel plan.

## Features

- **Personalized Itineraries**: Get custom travel plans based on your interests, budget, and trip duration.
- **Local Recommendations**: Discover local attractions, restaurants, and hidden gems at your destination.
- **User-Friendly Interface**: Input your travel details and preferences with ease using Streamlit's interactive components.

## Setup Instructions

### Prerequisites

- Python 3.10 or later
- An OpenAI API key
- A Langchain API key

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/ai-travel-planner.git
   cd ai-travel-planner
   
2. **Create a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate
```


3. **Install the required packages**:
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**: Create a .env file in the project root directory and add your OpenAI API key and Langchain API key:
```bash
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
```
### Running the Application

Run the Streamlit app:

```bash
streamlit run app.py
```
Open the Streamlit app in your browser (usually at http://localhost:8501).

## Usage
- Enter your travel destination in the "Enter your travel destination" field.
- Provide your travel preferences (e.g., interests, budget, duration) in the "Enter your travel preferences" field.
- Click the "Generate Itinerary" button to receive a personalized travel plan.
- Review the generated itinerary and enjoy your trip!

## Code Overview
- Language Model Setup: Uses ChatOpenAI from langchain_openai to interact with OpenAI's GPT-3.5-turbo model.
- Prompt Template: Utilizes ChatPromptTemplate to create a structured prompt for the language model.
- Streamlit Interface: Provides a simple and interactive UI for inputting travel details and displaying the itinerary.
- Output Parsing: Uses StrOutputParser to process the response from the language model.

## App Usage Screenshots

<img width="630" alt="Screenshot 2024-07-29 at 4:52:55 PM" src="https://github.com/user-attachments/assets/18854d4e-363d-4072-b234-631bb780b8d8">

## App Tracing in LangSmith Screenshots

<img width="1361" alt="Screenshot 2024-07-29 at 4 58 37 PM" src="https://github.com/user-attachments/assets/df90958a-acc6-445e-9021-745ad9d16538">





