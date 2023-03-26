from langchain.agents import initialize_agent, load_tools, tool
from langchain import OpenAI
from langchain.utilities import GoogleSearchAPIWrapper
import os
from temp_secrets import *

llm = OpenAI(temperature=0)

#tools = load_tools(['google-search'], llm=llm)
os.environ["GOOGLE_CSE_ID"] = GOOGLE_CSE_ID
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
os.environ["NEWS_API_KEY"] = NEWS_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
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
    
    prompt = f"""
    claim: Exercise is good for mental health.
    context: Research studies have consistently shown that physical exercise can help reduce symptoms of anxiety and depression.
    answer: The found context agrees with the claim, since exercise can help reduce symptoms of anxiety.

    claim: Video games are a waste of time.
    context: Many people enjoy playing video games as a form of entertainment and social interaction. However, videogames are linked to procrastination.
    answer: The found context partially agrees with the claim, since some people enjoy videogames but it might lead to procrastination.

    claim: {query}

    Provide an Answer to the last given claim based as demonstrated in the above examples and based on the context below.
    """
    output = agent.run(prompt)
    print(output)
    print(res)
    return output,res

if __name__ == '__main__':
    print(main("Is it true that nobody has died due to the earthquake in turkey in syria?"))
