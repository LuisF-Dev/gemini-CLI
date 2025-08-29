import typer
import os
from google import genai
import logging
from dotenv import load_dotenv
from methods import save_to_dotenv, clean_terminal
from rich.console import Console
from rich.markdown import Markdown
#load the enviroment variables
load_dotenv()

#logging config
logging.basicConfig(
    level=logging.INFO,
)
#instance console to render markdown on console
console = Console()

app = typer.Typer()


@app.command()
def chat(message: str):
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=message,
        )
    except ValueError:
        logging.error(
            "The gemini api key isn't defined, define it with 'geminicli config [username] [api key]'"
        )
        exit(1)
    if response.text:
        clean_terminal()
        md = Markdown(response.text)
        console.print(md)



@app.command()
def config(username: str, apikey: str):
    save_to_dotenv("GEMINI_API_KEY", apikey)


if __name__ == "__main__":
    app()
