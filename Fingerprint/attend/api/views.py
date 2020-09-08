from rest_framework import generics, mixins
from ..models import Workers, Posts, Register, suggestions, EventsDates, SmsModel, RealAtendance, RealSignOut, UploadNotes
from .serializers import WorkersSerializer, PostsSerializer, SmsSerializer, RealAtendanceSerializer, RegisterSerializer, SuggestionsSerializer, UploadNoteSerializer, EventSerializer, UserSerializer, UserLoginSerializer, RealSignOutSerializer
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


class AttendancePostCreate( mixins.CreateModelMixin ,generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = WorkersSerializer
    permission_classes = [AllowAny]


    def get_queryset(self):
        return Workers.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    def filter_queryset(self, queryset):
        queryset = super(AttendancePostCreate, self).filter_queryset(queryset)
        return queryset.order_by('-time_arrived')

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def patch(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)



class AttendancePostView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = WorkersSerializer
    permission_classes = [IsAuthenticated]



    def get_queryset(self):
        return Workers.objects.all()



class PostsCreate(generics.CreateAPIView ,generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PostsSerializer
    permission_classes = [IsOwnerOrReadOnly]


    def get_queryset(self):
        return Posts.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(author_name=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        queryset = super(PostsCreate, self).filter_queryset(queryset)
        return queryset.order_by('-date')

class PostsView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


    def get_queryset(self):
        return Posts.objects.all()





class RegisterCreate(generics.CreateAPIView ,generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


    def get_queryset(self):
        return Register.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




class UploadNotesView(generics.CreateAPIView ,generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = UploadNoteSerializer
    permission_classes = [AllowAny]


    def get_queryset(self):
        return UploadNotes.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class RegisterView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = PostsSerializer


    def get_queryset(self):
        return Register.objects.all()






class SuggestionCreate(generics.CreateAPIView ,generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = SuggestionsSerializer
    permission_classes = [IsOwnerOrReadOnly]


    def get_queryset(self):
        return suggestions.objects.all()

    def perform_create(self, serializer):
        serializer.save(name=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SuggestionView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = SuggestionsSerializer
    permission_classes = [AllowAny]


    def get_queryset(self):
        return suggestions.objects.all()










class EventCreate(generics.CreateAPIView ,generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]


    def get_queryset(self):
        return EventsDates.objects.all()

    def filter_queryset(self, queryset):
        queryset = super(EventCreate, self).filter_queryset(queryset)
        return queryset.order_by('-Date')

    # def perform_create(self, serializer):
    #     serializer.save(name=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class EventView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]


    def get_queryset(self):
        return EventsDates.objects.all()




class CreateUserView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer


    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)




class RealAtendanceCreate(mixins.CreateModelMixin ,generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = RealAtendanceSerializer
    lookup_field = 'pk'


    def get_queryset(self):
        return RealAtendance.objects.all()

    def filter_queryset(self, queryset):
        queryset = super(RealAtendanceCreate, self).filter_queryset(queryset)
        return queryset.order_by('-time')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class RealSignOutCreate(mixins.CreateModelMixin ,generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = RealSignOutSerializer
    lookup_field = 'pk'


    def get_queryset(self):
        return RealSignOut.objects.all()


    def filter_queryset(self, queryset):
        queryset = super(RealSignOutCreate, self).filter_queryset(queryset)
        return queryset.order_by('-time')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




class SmsUpdate(generics.RetrieveUpdateDestroyAPIView, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = SmsSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return SmsModel.objects.all()