from django.http import Http404


class IsMyProduct:
    """ Check if user task is request user """
    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        if not product.user == self.request.user:
            raise Http404
        return product