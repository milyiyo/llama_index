from llama_index.core.llms.base import BaseLLM
from llama_index.llms.xinference import Xinference


def test_embedding_class():
    names_of_base_classes = [b.__name__ for b in Xinference.__mro__]
    assert BaseLLM.__name__ in names_of_base_classes
