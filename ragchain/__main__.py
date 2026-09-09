from .embedding_models import embedding_model_base

def main():
    embedding_model = embedding_model_base.EmbeddingModalBase()
    embedding_model.PrintCurrentModel()

if __name__ == "__main__":
    main()
