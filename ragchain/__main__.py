from .embedding_models import embedding_models_registry as emr 

def main():
    em_registry = emr.EmbeddingRegistry() 
    em_registry.print_current_text_model()


if __name__ == "__main__":
    main()
