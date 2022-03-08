class Sources:
    """
    sources class to define sources Objects
    """
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country

class Articles:
    """
    articles class to define articles Objects
    """
    def __init__(self,title, author, description, urlToImage, url, publishedAt):
        self.title = title
        self.author = author
        self.description = description
        self.urlToImage = urlToImage
        self.url = url
        self.publishedAt = publishedAt
