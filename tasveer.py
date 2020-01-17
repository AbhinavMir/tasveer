def download(**kwargs):
    """
    Downloads images based on query and count. 
    If you do not include both a query and count, it will prompt utilizing input() 
    Downloaded to <PWD>/downloads
    
    Keyword arguments:
        query -- image query string
        count -- number of images to download
    """
    import os,sys
    class HiddenPrints:
        def __enter__(self):
            self._original_stdout = sys.stdout
            sys.stdout = open(os.devnull, 'w')

        def __exit__(self, exc_type, exc_val, exc_tb):
            sys.stdout.close()
            sys.stdout = self._original_stdout
    
    #check for query and count
    if not 'query' in kwargs:
    	query=input("Enter Query: ")
    else:
        query = kwargs['query']
    
    if not 'count' in kwargs:
        lim=int(input("Enter number of images: "))
    else:
        lim=int(kwargs['count'])

    if not 'width' in kwargs:
        img_width=input("Enter the width of images: ")
    else:
        img_width=kwargs['width']

    if not 'height' in kwargs:
        img_height=input("Enter the height of images: ")
    else:
        img_height=kwargs['height']
    
    with HiddenPrints():
        from google_images_download import google_images_download
        #instantiate the class
        response = google_images_download.googleimagesdownload()
        sizes = img_width + "," + img_height
        arguments = {"keywords":query,"limit":lim,"exact_size":sizes,"print_urls":True}
        paths = response.download(arguments)
        print("Saved at\n___________________\n")
        for i in range(lim):
            print(paths[0][query][i])
