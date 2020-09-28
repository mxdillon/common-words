# common-words

This python module extracts the most common 'interesting' words from a series of .txt files and summarises results.

The statistical techinique used to get the most 'interesting' words is Term Frequency Inverse Document Frequency (TFIDF
), which provides a metric ............

This module has been containerised and can be run with the following steps:

```
docker build -t common-words .
docker run
```

The results will be saved as a `.csv` file in the folder `~/common-words/app/results/`.


### Future Work
There are a number of extensions I would consider if expanding this out to a larger corpus or client environment:
* Serving: if this were being deployed to a client I would consider wrapping it up as a RESTful API so that
it could be accessed by the client regardless of where it was being hosted.
* Data Storage: the dataset provided was very small and did not contain any sensitive information, so
I have stored it in the source code. This is unlikely to be appropriate with client data. For speed and
security improvements I would look at using a persistent storage volume to store the raw data and a
separate volume for the outputs;
* Analysis: to keep this lightweight, I have used scikit-learn for the analysis. We might want to consider more
powerful models / techniques such as using spaCy language models or Latent Dirichlet Allocation;
* Memory Management: If this was a large dataset, memory management would become increasingly important -
especially when copying and manipulating dataframes;
* Model Saving: we may wish to save the model after training so it can be exported. I suggest ONNX as
a file format as it can be deployed into multiple runtimes.
* Logging:
