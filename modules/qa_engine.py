from transformers import pipeline

def get_answer(question, context):
    """Uses a Hugging Face model for Q&A on the dataset."""
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
    response = qa_pipeline(question=question, context=context)
    return response['answer']