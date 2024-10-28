from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['created_by'] = request.user.username
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, client_id):
        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return Response({'detail': 'Client not found.'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['client'] = client.id
        data['created_by'] = request.user.username

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        output = serializer.data
        output['client'] = client.client_name
        output['users'] = [{'id': user.id, 'name': user.username} for user in serializer.instance.users.all()]
        output['created_by'] = request.user.username 
        
        return Response(output, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)

def update(self, request, pk=None):
        try:
            client = self.get_object()
            serializer = self.get_serializer(client, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Client.DoesNotExist:
            return Response({'detail': 'Client not found.'}, status=status.HTTP_404_NOT_FOUND)

def destroy(self, request, pk=None):
        try:
            client = self.get_object()
            client.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Client.DoesNotExist:
            return Response({'detail': 'Client not found.'}, status=status.HTTP_404_NOT_FOUND)