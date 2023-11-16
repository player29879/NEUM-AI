from typing import List, Generator
from neumai.Shared.NeumDocument import NeumDocument
from neumai.Shared.LocalFile import LocalFile
from neumai.Loaders.Loader import Loader
from langchain.document_loaders import UnstructuredHTMLLoader

class HTMLLoader(Loader):
    """" HTML Loader \n loader_information requires: [ ]"""

    @property
    def loader_name(self) -> str:
        return "HTMLLoader"
    
    @property
    def required_properties(self) -> List[str]:
        return []

    @property
    def optional_properties(self) -> List[str]:
        return []
    
    @property
    def available_metadata(self) -> List[str]:
        return []

    @property
    def available_content(self) -> List[str]:
        return []

    def load(self, file:LocalFile) -> Generator[NeumDocument, None, None]:
        """Load data into Document objects."""
        loader = UnstructuredHTMLLoader(file_path=file.file_path)
        documents = loader.load()
        # join the file and document metadata objects
        for doc in documents:
            yield NeumDocument(id=file.id, content=doc.page_content, metadata=file.metadata)
    
    def validate(self) -> bool:
        return True   