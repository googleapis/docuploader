# Documentation Uploader for Client Libraries

This tool uploads documentation for publishing to googleapis.dev
and cloud.google.com (see
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
1. Upload the docs with `docuploader upload`:
   ```
   Usage: docuploader upload [OPTIONS] DOCUMENTATION_PATH

   Options:
   --staging-bucket TEXT      The bucket to upload the staged documentation to.
   --credentials TEXT         Path to the credentials file to use for Google
                              Cloud Storage.

   --metadata-file TEXT       Path to the docs.metadata file. The path must be
                              relative to the CWD.

   --destination-prefix TEXT  Prefix to include when uploading tar file. A -
                              will be added after the prefix, if there is one.

   --help                     Show this message and exit.
   ```

   docuploader will take the documentation in `DOCUMENTATION_PATH`,
   `docs.metadata` or `docs.metadata.json` and create a tarball (`tgz`), then
   send the tarball to the bucket specified in `--staging-bucket` option with a
   prefix specified in `--destination-prefix`.

`docuploader` can use ADC (Application Default Credentials) or a given service account. To use ADC, run `gcloud auth application-default login` prior to upload to gain credentials.

For an example of using `docuploader`, see
[example usage in googleapis/google-cloud-go](https://github.com/googleapis/google-cloud-go/blob/main/internal/kokoro/publish_docs.sh).

## Requirements for DocFX YAML tarballs

The tarballs containing DocFX YAML files must adhere to the following requirements:

1. The tarball must contain metadata in the form of the `Metadata` message from
   [`metadata.proto`](./docuploader/protos/metadata.proto). This can be
   represented in protobuf text format in a file called `docs.metadata`, or in
   protobuf JSON format in a file called `docs.metadata.json`.
    * [`docs.metadata` example](https://github.com/googleapis/doc-pipeline/blob/main/testdata/python/docs.metadata)
    * [`docs.metadata.json` example](https://github.com/googleapis/doc-pipeline/blob/main/testdata/dotnet/docs.metadata.json)
1. `docs.metadata` or `docs.metadata.json` must have
    * `name`
    * `version`
    * `language`

   See [`metadata.proto`](./docuploader/protos/metadata.proto) for other
   supported fields.
1. `toc.yml` or `toc.html` file exists at the root directory or in special
   subdirectories (`./api/toc.yml`).
1. documentation files may either be in
    * Root directory (`./page1.yml`, `./page2.yml`)
    * Subdirectories (`./product/page1.yml`, `./product/page2.yml`)
    * Special subdirectories (`./api`, `./examples`)

   **Note:** If you use special subdirectories, only use special subdirectories
   and do not place documentation in the root or other subdirectories.

(1) and (2) will be checked and enforced if you use `docuploader upload`.
