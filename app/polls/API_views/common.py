class CommonMixin():
    def getIDfromUrl(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )
        # filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]} # ==> {"pk" : '4'}
        searched_ID = self.kwargs[lookup_url_kwarg]
        return searched_ID

ENDL = '\n'
def saveprint(x):
    print(ENDL, x, ENDL)