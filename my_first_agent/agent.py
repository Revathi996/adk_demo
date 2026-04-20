from google.adk.agents import Agent
from google.adk.tools import google_search

def morning_greeting():
    return "Good morning! How can I assist you with your Google Cloud queries today?"

def evening_greeting():
    return "Good evening! How can I assist you with your Google Cloud queries today?"

root_agent = Agent(name="my_first_agent", description="This is my first agent which will answer query on google cloud.",
                   model="gemini-2.5-flash", instruction=" First ask user name and greet them based on users" \
                   "grreet, if user says Goodmorning use morning_greeting tool, if user says Good evening use evening_greeting() tool. You are an AI that helps users to answer query on google cloud use google search. You will be given a question and you need to answer " \
                   "it based on your knowledge of google cloud. If you don't know the answer, you can say 'I don't know'." \
                   " Always try to give the best answer based on your knowledge. " \
                   "", tools=[morning_greeting, evening_greeting])


