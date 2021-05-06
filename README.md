# Documentation Uploader for Client Libraries

This tool uploads documentation for publishing to googleapis.dev
and cloud.google.com (see
[`doc-templates`](https://github.com/googleapis/doc-templates) and
[`doc-pipeline`](https://github.com/googleapis/doc-pipeline) for more info).

## Installation

You can install `docuploader` with:

```
pip install gcp-docuploader
```

## Usage

There are two steps for uploading docs:
1. Create a metadata file. See [`metadata.proto`](./docuploader/protos/metadata.proto)
   for the format.
   * You can use `docuploader create-metadata` to create a `docs.metadata` file.
   * Alternatively, you can create a `docs.metadata.json` file independently.
1. Upload the docs with `docuploader upload`.

`docuploader` can use ADC or a given service account.

For an example of using `docuploader`, see
[example usage in googleapis/google-cloud-go](https://github.com/googleapis/google-cloud-go/blob/master/internal/kokoro/publish_docs.sh).