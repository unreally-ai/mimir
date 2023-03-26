"""
To what extend does the internet context agree to the given claim(s) below?
Claim(s):
"""
from langchain import PromptTemplate, FewShotPromptTemplate

examples = [
    {
        "claim": "Exercise is good for mental health.",
        "context": "Research studies have consistently shown that physical exercise can help reduce symptoms of anxiety and depression.",
        "answer": "The found context agrees with the claim, since exercise can help reduce symptoms of anxiety."
    },
    {
        "claim": "Video games are a waste of time.", 
        "context": "Many people enjoy playing video games as a form of entertainment and social interaction. However, videogames are linked to procrastination.",
        "answer": "The found context partially agrees with the claim, since some people enjoy videogames but it might lead to procrastination."
    }
]

example_format_template = """
Claim: {claim}
Context: {context}
Answer: {answer}
"""

template = """
Task: To what extend does the claim and context agree and why?

"""
prompt = PromptTemplate(
    input_variables=["product"],
    template=template,
)