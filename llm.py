from groq import Groq
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(Path(__file__).parent.parent / ".env")

client = Groq(
    api_key=  os.getenv("GROQ_API_KEY"))


def analyze_data(question, df):
    data_sample = df.head(10).to_string()

    prompt = f"""
    you are a professional data analyst.

    dataset preview

    {data_sample}

    columns:
    {list(df.columns)}

    Answer the following question using the dataset. 

    question:
    {question}
    """


    response  = client.chat.completions.create(
        model  = "llama-3.3-70b-versatile",
        messages= [
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature= 0 

    )

    return response.choices[0].message.content





