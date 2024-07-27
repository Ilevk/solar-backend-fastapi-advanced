from enum import Enum

class EmbeddingModel(Enum):
    QUERY = "solar-embedding-1-large-query"
    PASSAGE = "solar-embedding-1-large-passage"

class ChatModel(Enum):
    MINI = "solar-1-mini-chat"
