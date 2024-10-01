#Using unstructured url loader

nltk.download('punkt')
url = "https://www.apple.com/newsroom/2024/08/apple-reports-third-quarter-results/"  
loader = UnstructuredURLLoader(urls=[url])
documents = loader.load()

#Splitting text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,   
    chunk_overlap=100    
