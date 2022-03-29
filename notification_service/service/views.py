from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from service.models import MailingList
from service.serializers import *


class ClientAPIView(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get(self, request):
        clients = Client.objects.all()
        return Response({'clients': ClientSerializer(clients, many=True).data})

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'client': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("id", None)
        if not pk:
            return Response({"error": 'Method DELETE not allowed'})

        try:
            instance = Client.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = ClientSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            Client.objects.get(pk=pk).delete()
            return Response({"complete": "delete client " + str(pk)})
        except:
            return Response({"error": "Deletion failed"})


class MailinglistAPIView(ModelViewSet):
    queryset = MailingList.objects.all()
    serializer_class = MailingListSerializer

    def get(self, request):
        mailinglists = MailingList.objects.all()
        return Response({'mailinglists': MailingListSerializer(mailinglists, many=True).data})

    def post(self, request):
        serializer = MailingListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'mailinglists': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("id", None)
        if not pk:
            return Response({"error": 'Method DELETE not allowed'})
        try:
            instance = MailingList.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = MailingListSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        print(kwargs.get("id"))
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        try:
            MailingList.objects.get(pk=pk).delete()
            return Response({"complete": "delete mailinglist " + str(pk)})
        except:
            return Response({"error": "Deletion failed"})

