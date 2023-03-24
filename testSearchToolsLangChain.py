from langchain.agents import initialize_agent, load_tools, tool
from langchain.chat_models import ChatOpenAI
from langchain.utilities import GoogleSearchAPIWrapper
import os
from temp_secrets import *
import time

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

#tools = load_tools(['google-search'], llm=llm)
os.environ["GOOGLE_CSE_ID"] = GOOGLE_CSE_ID
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
os.environ["NEWS_API_KEY"] = NEWS_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def timed_task(task_func):
    """Decorator to time a task.

    Args:
        task_func (func): The function to time.

    Returns:
        wrapper (func): The wrapper function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = task_func(*args, **kwargs)
        end_time = time.time()
        print(f"{task_func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@tool
def search_w_source(query: str) -> str:
    """Searches the API for the query.
    
    Args: 
        query (str): The query to search for.
    
    Returns:
        clean (list): The list of results.
    """
    global res
    res = []
    sources = [entry['link'] for entry in GoogleSearchAPIWrapper()._google_search_results(query)]
    res.append(sources[1:])
    clean = GoogleSearchAPIWrapper().run(query)
    return clean[1:]

@timed_task
def main(query: str) -> str: #TODO: Make faster 
    """Main function to run the tool.

    Args:
        query (str): The query to search for.

    Returns:
        str: The answer to the query. By the model.
    """
    agent = initialize_agent([search_w_source], llm, agent="zero-shot-react-description", verbose=False)
    output = agent.run(query)
    return output, res

if __name__ == '__main__':
    print(main("Is it true that nobody has died due to the earthquake in turkey in syria?"))