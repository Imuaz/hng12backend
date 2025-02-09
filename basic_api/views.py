from rest_framework import generics
from .models import User
from .serializers import UserSerializer

class UserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        """
        Return the first user object or create one if it doesn't exist
        """
        obj, created = User.objects.get_or_create(
            email="imuazyakub@gmail.com",
            github_url="https://github.com/imuaz/hng12backend"

        )
        return obj
