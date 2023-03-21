from langchain.agents import initialize_agent, load_tools, tool
from langchain import OpenAI
from langchain.utilities import GoogleSearchAPIWrapper
import os

llm = OpenAI( temperature=0)

#tools = load_tools(['google-search'], llm=llm)
os.environ["GOOGLE_CSE_ID"] = "045ce996aee984559"
os.environ["GOOGLE_API_KEY"] = "AIzaSyCt3rg2zFsnK9e_O0LUE1I_IQbvBTojD_U"
os.environ["NEWS_API_KEY"] = "a715f9012c85492fa24958731f5b9c39"
res = []

@tool
def search_w_source(query: str) -> str:
    """Searches the API for the query."""
    pureResults = GoogleSearchAPIWrapper()._google_search_results(query)
    sources = [entry['link'] for entry in pureResults]
    res.append(sources[1:])
    clean = GoogleSearchAPIWrapper().run(query)
    return clean[1:]

def main(query: str) -> str:
    #print([entry['pagemap']['metatags'][0] for entry in search_w_source("The Queen is not dead.")])
    agent = initialize_agent([search_w_source], llm, agent="zero-shot-react-description", verbose=False)
    output = agent.run(query)
    print(output)
    print(res)
    return output,res

if __name__ == '__main__':
    print(main("Is it true that nobody has died due to the earthquake in turkey in syria?"))