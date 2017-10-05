# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from snippets.models import Statistics
from snippets.serializers import StatisticsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
import pickle


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        # import numpy as np
        # import pandas as pd
        # from sklearn.ensemble import RandomForestClassifier
        # from sklearn.model_selection import train_test_split
        # df = pd.DataFrame(list(Statistics.objects.all().values()))
        # df_x=df.iloc[:,[0,1,2,3,5,7,8]]
        # df_y=df.iloc[:,5]
        # x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)
        # rf=RandomForestClassifier(n_estimators=100)
        # rf.fit(x_train,y_train)
        # pickle_out=open("data.pkl","wb")
        # pickle.dump(rf, pickle_out)
        # pickle_out.close()

        snippets = Statistics.objects.all()
        serializer = StatisticsSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StatisticsSerializer(data=request.data)
        if serializer.is_valid():
            pickle_in = open('data.pkl', 'rb')
            rf = pickle.load(pickle_in)
            serializer.save()
            print rf.predict([[serializer.data['agentId'],
                               serializer.data['averageDuration'],
                               serializer.data['averageHoldingDuration'],
                               serializer.data['externalId'],
                               serializer.data['isResolved'],
                               serializer.data['numberOfCalls'],
                               serializer.data['numberOfEmails']]])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Statistics.objects.get(pk=pk)
        except Statistics.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = StatisticsSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = StatisticsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Analyze(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        snippets = Statistics.objects.all()
        serializer = StatisticsSerializer(snippets, many=True)
        return Response(serializer.data)
