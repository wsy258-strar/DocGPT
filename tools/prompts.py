# flake8: noqa
from langchain.prompts import PromptTemplate

## Use a shorter template to reduce the number of tokens in the prompt
template = """Create a final answer to the given questions using the provided document excerpts (given in no particular order) as sources.
ALWAYS include a "SOURCES" section in your answer, citing only the minimum amount of sources required to answer the question. 
The language used in your answer is assumed to be the same as the language used to ask the question.
If the user asks you to translate into a certain language, please strictly follow the instructions to translate the answer.
If you are unable to answer the question, please say "Sorry , l cannot answer the question based on known content" and leave the "SOURCES" section blank. 
Use only the provided files and do not attempt to fabricate answers..

---------

QUESTION: What  is the purpose of ARPA-H?
=========
Content: More support for patients and families. \n\nTo get there, I call on Congress to fund ARPA-H, the Advanced Research Projects Agency for Health. \n\nIt's based on DARPA—the Defense Department project that led to the Internet, GPS, and so much more.  \n\nARPA-H will have a singular purpose—to drive breakthroughs in cancer, Alzheimer's, diabetes, and more.
SOURCES: 1-32
Content: While we're at it, let's make sure every American can get the health care they need. \n\nWe've already made historic investments in health care. \n\nWe've made it easier for Americans to get the care they need, when they need it. \n\nWe've made it easier for Americans to get the treatments they need, when they need them. \n\nWe've made it easier for Americans to get the medications they need, when they need them.
SOURCES: 1-33
Content: The V.A. is pioneering new ways of linking toxic exposures to disease, already helping  veterans get the care they deserve. \n\nWe need to extend that same care to all Americans. \n\nThat's why I'm calling on Congress to pass legislation that would establish a national registry of toxic exposures, and provide health care and financial assistance to those affected.
SOURCES: 1-30
=========
FINAL ANSWER: The purpose of ARPA-H is to drive breakthroughs in cancer, Alzheimer's, diabetes, and more.
SOURCES: 1-32

---------

QUESTION: {question}
=========
{summaries}
=========
FINAL ANSWER:"""

STUFF_PROMPT = PromptTemplate(
    template=template, input_variables=["summaries", "question"]
)
