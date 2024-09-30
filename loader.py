#Using unstructured url loader

nltk.download('punkt')
url = "https://www.apple.com/newsroom/2024/08/apple-reports-third-quarter-results/"  
loader = UnstructuredURLLoader(urls=[url])
documents = loader.load()
