from langchain.llms import GooglePalm



from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate

# from langchain import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter

api_key = 'AIzaSyDoi9dYBVNne75DD4P-pce6Pf3i-Ol7Cbo' # get this free api key from https://makersuite.google.com/

llm = GooglePalm(google_api_key=api_key, temperature=0.1)

paul_graham_essay = 'emails.txt'

with open(paul_graham_essay, 'r',encoding='utf-8') as file:
    essay = file.read()

text_splitter = RecursiveCharacterTextSplitter( chunk_size=1000, chunk_overlap=100, separators=["------------------------------"])
docs = text_splitter.create_documents([essay])


# Summarize prompt

map_prompt_template = """
                      Write a summary of this chunk of text that includes the main points and any important details.
                      {text}
                      """

map_prompt = PromptTemplate(template=map_prompt_template, input_variables=["text"])

combine_prompt_template = """
Write a concise summary of the following text.
```{text}```
while text is the mails retrived from my mail account. each new mail is separeted by '---------------' symbol.
Return your response in the following format.
            From: \n
            Subject: subject should be as it is \n
            content summary:\n

"""
combine_prompt = PromptTemplate(
    template=combine_prompt_template, input_variables=["text"]
)



map_reduce_chain = load_summarize_chain(
    llm=llm,
    chain_type="map_reduce",
    map_prompt=map_prompt,
    combine_prompt=combine_prompt,
    # verbose=True,
)

# def summary(num):
#     output = map_reduce_chain.run([docs[1]])
#     return output


def summary(num):
    output = map_reduce_chain.run(docs[num-1:num])
    return output




