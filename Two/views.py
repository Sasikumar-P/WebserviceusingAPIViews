# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from serializers import ProfileSerializer
from models import  Profile
from rest_framework import generics


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView): 
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer




# Create your views here.
