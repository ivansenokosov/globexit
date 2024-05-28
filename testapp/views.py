from rest_framework import viewsets, permissions
from testapp.serializers import GlobexUsersSerializer
from testapp.models import GlobexUsers


class GlobexUsersViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = GlobexUsers.objects.all()
    serializer_class = GlobexUsersSerializer
    
    def get_queryset(self):
        qs = GlobexUsers.objects.all()
        term = self.request.query_params.get('term')
        if term is not None:
            qs = qs.filter(name__icontains=term)
        return qs
    

