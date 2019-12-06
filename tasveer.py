def download():
    import os,sys
    class HiddenPrints:
        def __enter__(self):
            self._original_stdout = sys.stdout
            sys.stdout = open(os.devnull, 'w')

        def __exit__(self, exc_type, exc_val, exc_tb):
            sys.stdout.close()
            sys.stdout = self._original_stdout

    query=input("Enter Query: ")
    lim=int(input("Enter number of images: "))
    with HiddenPrints():
        from google_images_download import google_images_download
        #instantiate the class
        response = google_images_download.googleimagesdownload()
        arguments = {"keywords":query,"limit":lim,"print_urls":True}
        paths = response.download(arguments)
        print("Saved at\n___________________\n")
        for i in range(lim):
            print(paths[0][query][i])