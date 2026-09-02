# Artitechture 
## Injustor
A class that takes any form of data, i.e text, image, etc and has an ability to create a vector store out of it.
### Embedding Model Base
Abstracts embedding models. Loads one up based on the config. The data is given to it for embedding and it uses the correct model to imbedded it.
#### Embedding Model Dictionary & Router
Storing the embedding models from config. And router routing the correct one. 
## Vector Store Base
A class that abstaracts and loads a vector store, provides api for similarity search and gives results back. 
### Vector Store Dictionary 
Stores multiple vector stores, along with a description. 
### Vector Store Router
Routing a query through same vector store. 
## Query Translator
Can translate a query into multiple kinds based on configured method.
## LLM-Model Base 
Abstaracts an AI model. Can accept a query along with a context set.
### LLM-Dictionary
Loads the llm-models based on the config file. 
### LLM-Router
Loads the query to the right LLM
