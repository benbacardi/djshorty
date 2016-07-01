from tastypie.resources import ModelResource
from tastypie.validation import FormValidation
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import BasicAuthentication, SessionAuthentication, MultiAuthentication


from ....models import ShortURL
from ....forms import ShortURLForm


class ShortURLResource(ModelResource):

    class Meta:
        authentication = MultiAuthentication(SessionAuthentication(), BasicAuthentication())
        authorization = DjangoAuthorization()

        queryset = ShortURL.objects.all()
        fields = [
            'path',
            'redirect',
            'external',
        ]

        validation = FormValidation(form_class=ShortURLForm)

    def obj_create(self, bundle, **kwargs):
        return super(ShortURLResource, self).obj_create(bundle, user=bundle.request.user)

    def authorized_read_list(self, object_list, bundle):
        return object_list.filter(user=bundle.request.user)
