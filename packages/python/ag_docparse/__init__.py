"""docparse — LLM-powered document extraction."""

from importlib.metadata import version as _version

from .models    import (
    FieldSpec, ExtractionSchema, FieldValue, ExtractionResult,
    PageContent, DocumentLayout,
)
from .loader    import from_text, load
from .extractor import LLMExtractor
from .async_client import AsyncJobClient, QuotaExceededError
from .schemas   import REGISTRY, INVOICE_SCHEMA, LOAN_APPLICATION_SCHEMA, W2_SCHEMA, NDA_SCHEMA, CONTRACT_SCHEMA

__version__ = _version("ag-docparse")

__all__ = [
    "FieldSpec", "ExtractionSchema", "FieldValue", "ExtractionResult",
    "PageContent", "DocumentLayout",
    "from_text", "load",
    "LLMExtractor", "AsyncJobClient", "QuotaExceededError",
    "REGISTRY", "INVOICE_SCHEMA", "LOAN_APPLICATION_SCHEMA",
    "W2_SCHEMA", "NDA_SCHEMA", "CONTRACT_SCHEMA",
]
