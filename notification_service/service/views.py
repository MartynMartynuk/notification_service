import datetime

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

    def list(self, request, *args, **kwargs):
        referer = request.headers['Referer'].split('?')
        mailinglists = MailingList.objects.all()
        if len(referer) == 2:
            param_args = {}
            params = referer[1].split('&')
            for param in params:
                param_args[param.split('=')[0]] = param.split('=')[1]

            if param_args.get('maillist_stat') is not None:
                return Response(self.get_maillist_stat(mailinglists))
            elif param_args.get('message_stat') is not None:
                return Response(self.get_message_stat(param_args.get('message_stat')))
        return Response({'mailinglists': MailingListSerializer(mailinglists, many=True).data})

    def create(self, request, *args, **kwargs):
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

    @staticmethod
    def get_maillist_stat(maillists):
        ml_tot_number = len(maillists)
        stats = {'total mailings': ml_tot_number}
        for maillist in maillists:
            sent = 0
            not_sent = 0
            messages = Message.objects.filter(mailinglist_id=maillist.id)
            for message in messages:
                if message.sending_status:
                    sent += 1
                else:
                    not_sent += 1
            stats['maillist '+str(maillist.id)] = {'messages sent': sent, 'messages not sent': not_sent}
        return stats

    @staticmethod
    def get_message_stat(maillist_id):
        messages = Message.objects.filter(mailinglist_id=maillist_id)
        maillist = MailingList.objects.get(id=maillist_id)
        stats = {'maillist client filter': maillist.client_filter,
                 'total messages': len(messages)}
        sent = 0
        not_sent = 0
        for message in messages:
            print(message.id)
            if message.sending_status:
                sent += 1
            else:
                not_sent += 1
            stats['messages sent'] =  sent
            stats['messages not sent'] = not_sent
        print(stats)
        return stats


class MessageAPIView(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get(self, request):
        messages = Message.objects.all()
        return Response({'messages': MessageSerializer(messages, many=True).data})

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'messages': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("id", None)
        if not pk:
            return Response({"error": 'Method DELETE not allowed'})
        try:
            instance = Message.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = MessageSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        print(kwargs.get("id"))
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        try:
            Message.objects.get(pk=pk).delete()
            return Response({"complete": "delete message " + str(pk)})
        except:
            return Response({"error": "Deletion failed"})
