from tastypie.authorization import Authorization
from tastypie.authorization import ModelResource
from notes.models import Note

class NotesResourc(ModelResource):
    class Meta: 
        queryset = Note.objects.all()
        resource_name = 'note'
        authorization = Authorization()
        list_allowed_methods = ['get', 'post', 'put', 'delete']