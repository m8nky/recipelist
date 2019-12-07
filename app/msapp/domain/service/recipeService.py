class RecipeService:
    '''
      RecipeService.serve is called by the HTTP server, when a new browser request comes in.

      Serve the browser with some recipe content.

      Parameters:
        request (str): The path of the requested URL (e.g. '/' or '/recipelist').

      Returns:
        str: The content (text or html), that is replied to the browser.
    '''
    def serve(self, request: str) -> str:
        pass
