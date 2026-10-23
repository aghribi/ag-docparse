export {
  FieldType,
  FieldSpec,
  ExtractionSchema,
  ExtractionResult,
  FieldValue,
  PageContent,
  DocumentLayout,
  makeField,
  fieldNames,
  promptLines,
  clampedFieldValue,
  getValue,
  getConfidence,
  missingRequired,
  makeLayout,
  pageCount,
  textForPages,
  allTables,
} from "./models";

export { fromText, load } from "./loader";
export { LLMExtractor, LLMExtractorOptions } from "./extractor";
export {
  INVOICE_SCHEMA,
  LOAN_APPLICATION_SCHEMA,
  W2_SCHEMA,
  NDA_SCHEMA,
  CONTRACT_SCHEMA,
  REGISTRY,
} from "./schemas";

export { AsyncJobClient } from "./async_client";
export type { AsyncJobClientOptions, DocparseJob } from "./async_client";

// Read at runtime so the exported version always matches the published package.
export const VERSION: string = require("../package.json").version;
