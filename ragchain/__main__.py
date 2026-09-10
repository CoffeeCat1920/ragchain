from .embedding_models import text_embedding_model_base 

def main():
    hf_text_em_base = text_embedding_model_base.HFTextEMBase("sentence-transformers/all-MiniLM-L6-v2")
    hf_text_em_base.GetEmbeddingModel()
    hf_text_em_base.PrintModelName()


if __name__ == "__main__":
    main()
