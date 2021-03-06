from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from notes.models import Note

class NoteResource(ModelResource):
    class Meta: 
        queryset = Note.objects.all()
        resource_name = 'note'
        authorization = Authorization()
        list_allowed_methods = ['get', 'post', 'put', 'delete']