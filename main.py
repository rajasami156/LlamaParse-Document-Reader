import os 
import nest_asyncio
from dotenv import load_dotenv
from llama_parse import LlamaParse

load_dotenv()

nest_asyncio.apply()
LLAMA_CLOUD_API_KEY = os.getenv("LLAMA_CLOUD_API_KEY")

document = LlamaParse(result_type="markdown").load_data("dummy_resume.pdf") 
print(document[0].text[:1000])