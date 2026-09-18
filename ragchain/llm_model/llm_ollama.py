from .llm_base import LLMBase 
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from pydantic import BaseModel

class LLMBaseOllama(LLMBase):
    def __init__(self, model_name : str) -> None:
        super().__init__(model_name)
        self.model_name = model_name 
        self.llm = ChatOllama(
            model=self.model_name,
            temperature=0
            )

    def invoke(self, query : str) -> str | None:
        response = self.llm.invoke(query)
        if isinstance(response.content, str):
            return response.content


    def invoke_json(self, query: str, format: type[BaseModel]):
        prompt = ChatPromptTemplate.from_template("""
                                                  {query}
                                                  {format_instruction}""")
        parser = JsonOutputParser(pydantic_object=format)

        chain = prompt | self.llm | parser 

        result = chain.invoke({"query": query, 
                               "format_instruction": parser.get_format_instructions()})

        return result
