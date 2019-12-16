from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

#rest_framework

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework  import status

from ScrapApp.models import BrowseItems
from ScrapApp.serializers import BrowseItemSerializer

import json


class BrowseItemView(viewsets.ModelViewSet):
    queryset=BrowseItems.objects.all()
    serializer_class=BrowseItemSerializer

    @action(methods=['GET'],detail=False,url_path="Find_Product_By_name")
    def Find_Product_By_name(self,request):
        name=str(request.GET.get('q',''))

        datas=[]
        ans=[]
        for i in range(0,len(name)+1):
            for j in range(0,i):
                # print(st[j:i])    
                good_student=BrowseItems.objects.filter(name=name[j:i])
                serlzr=BrowseItemSerializer(good_student,many=True)
                datas.append(serlzr.data)
        for i in range(0,len(datas)):
            if(len(datas[i])>=1):
                ans.append(datas[i])

        # good_student=BrowseItems.objects.filter(name=name)
        # serlzr=BrowseItemSerializer(good_student,many=True)
        # ans.append(serlzr.data)
        return Response(ans, status.HTTP_200_OK)

    @action(methods=['POST'], detail=False, url_path="enter_product")
    def enter_product(self, request):
        serializer = BrowseItemSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            BrowseItems.objects.create(
                name=validated_data['name'],
                price=validated_data['price'],
                description=validated_data['description'],
                image_link=validated_data['image_link'],
            )
            return Response(validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    # @action(methods=['PUT'], detail=True, url_path="Update_Student_percentage")
    # def Update_Student_percentage(self, request, *args, **kwargs):
    #     filter_kwargs = {self.lookup_field : self.kwargs[self.lookup_field]}
    #     serializer = BrowseItemSerializer(data=request.data)
    #     if serializer.is_valid():
    #         validated_data = serializer.validated_data
    #         To_update = BrowseItems.objects.get(**filter_kwargs)
    #         a=To_update
    #         a.percentage = validated_data['percentage']
    #         a.save()
    #         return Response(validated_data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
