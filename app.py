from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Enables the tracing for Langsmith globally.
## Langchain automatically traces all interactions without needing to decorate individual functions by integrating LangSmith
os.environ["LANGCHAIN_TRACING_V2"]="true"

## API key for Langchain to use the Langsmith service
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert travel assistant. Please help the user plan their trip."),
        ("user", "Travel Preferences based on Destination in a table UI: {preferences}, {destination}")
    ]
)

# streamlit framework
st.title('AI Travel Planner') ## title
st.write('Plan your trip with personalized itineraries and local recommendations!')

# Input fields for travel preferences
destination = st.text_input("Enter your travel destination")
preferences = st.text_area("Enter your travel preferences (e.g., interests, budget, duration)")


## instance of the ChatOpenAI model
llm=ChatOpenAI(model="gpt-3.5-turbo")

## an output parser setup to get string responses
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

# give the input as a question/prompt to the llm model
##  If the user provides input, the chain is invoked with the input and the response is displayed.
if st.button("Generate Itinerary"):
    if destination and preferences:
        response= chain.invoke({'preferences': preferences, 'destination': destination})
        st.write(response)
    else:
        st.write("Please enter both destination and preferences.")



