# common-words

This python module extracts the most common 'interesting' words from a series of .txt files and summarises the results.

The statistical techinique used to get the most 'interesting' words is Term Frequency Inverse Document Frequency (TFIDF
), which provides a metric indicating how important a particular word is to a document in the context of a wider
 corpus of documents.

For more information and the mathematical derivation please see this
[page](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).

---------------
### Running the module
This module has been containerised and can be run anywhere with the following steps:

```
docker build -t common-words .
docker run -it common-words bash
python3 app.py 3
```

A set of unit tests will be run as part of the build process. The build will fail if coverage falls below 85%.

The user can specify the number of 'interesting' terms to return per document as a command line argument (3 shown as
 an example above). If left blank, this will default to 5 per document.

The results will be saved as a `.csv` file in the folder `~/common-words/app/results/`.

--------------------

### Future Work
There are a number of extensions to consider if expanding this out to a larger corpus or production environment:
* Serving: if this were being deployed for reuse I would consider wrapping it up as a RESTful API so that
it could be accessed by the client regardless of where it was being hosted.
* Data Storage: the dataset provided is very small and doesn't contain any sensitive information, so
I have stored it in the source code. This is unlikely to be appropriate with production data. For speed and
security improvements I would look at using a persistent storage volume to store the raw data and a
separate volume for the outputs;
* Analysis: to keep this lightweight, I have used scikit-learn for the analysis. We might want to consider more
powerful models / techniques such as using spaCy language models or Latent Dirichlet Allocation;
* Memory Management: If this was a large dataset, memory management would become increasingly important -
especially when copying and manipulating dataframes;
* Model Saving: we may wish to save the model after training so it can be exported. I suggest ONNX as
a file format as it can be deployed into multiple runtimes.
* Logging: If this were to be deployed more detailed logging would be required throughout the module, including extra
 information that would help in debugging, such as the internal IP address of the server running the module (if
  deploying onto a network).
