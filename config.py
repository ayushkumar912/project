import os

# Paths
DATASET_PATH = os.getenv("DATASET_PATH", "assets/titanic.csv")

# Hugging Face Models
QA_MODEL = os.getenv("QA_MODEL", "deepset/roberta-base-squad2")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

# LangSmith Configuration
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY", "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")
LANGSMITH_API_URL = os.getenv("LANGSMITH_API_URL", "https://api.langsmith.com")