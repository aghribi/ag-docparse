# ag-docparse

LLM-based structured extraction from documents.

Loads PDF or text documents and extracts typed fields with an LLM, using built-in schemas (invoice, loan application, W-2, NDA, contract) or a custom JSON schema.

## Install

```sh
pip install "ag-docparse[all]"
npm install ag-docparse
```

Extras: `openai`, `anthropic`, `pdf` (pdfplumber), `all`.

## Usage

```python
from ag_docparse import INVOICE_SCHEMA, LLMExtractor, from_text

layout = from_text("Invoice INV-001, total due 1,250.00 EUR by 2026-11-30.")
result = LLMExtractor(model="gpt-4o-mini").extract(layout, INVOICE_SCHEMA)  # needs OPENAI_API_KEY
print(result)
```

Command line: `ag-docparse extract -f invoice.pdf -s invoice` and `ag-docparse schemas`.

The TypeScript package `ag-docparse` is a port of the core classes.

## Self-hosted API

`AsyncJobClient` submits large documents as asynchronous jobs to a self-run [ag-platform](https://github.com/aghribi/ag-platform) deployment: `AsyncJobClient(api_key=..., base_url=...)` (TypeScript: `baseUrl`). There is no default endpoint.

## Development

```sh
cd packages/python && pip install -e ".[all]" && pytest
cd packages/typescript && npm ci && npm test
```

## License

MIT, Copyright (c) 2026 Adnan Ghribi.
