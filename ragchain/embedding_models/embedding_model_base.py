from ragchain.config import embedding_models_config

class EmbeddingModalBase:
    def __init__(self):
        self.config = embedding_models_config.LoadEmbeddingModelConfig()
    def PrintCurrentModel(self):
        print(self.config.current_text_embedding_model)
        print(self.config.text_embedding_models_list.get(self.config.current_text_embedding_model))
