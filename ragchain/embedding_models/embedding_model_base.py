from ragchain.config import embedding_models_config

class EmbeddingModalBase:
    def __init__(self):
        self.config = embedding_models_config.LoadEmbeddingModelConfig()
    def PrintCurrentModel(self):
        print(self.config.current_text_embedding_model)
