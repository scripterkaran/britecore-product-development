from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from risk_management.risk_type.serializers import RiskTypeDetailSerializer, RiskTypeListSerializer
from .models import RiskType


class AccountTests(APITestCase):
    fixtures = ['risk_management/risk_type/fixtures/initial.json', ]

    def test_list_api(self):
        url = reverse('risktype-list')
        response = self.client.get(url,format='json')
        serializer = RiskTypeListSerializer(instance=RiskType.objects.all(), many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


    def test_retrieve_api(self):
        url = reverse('risktype-detail', kwargs={'pk': 1})
        serializer = RiskTypeDetailSerializer(instance=RiskType.objects.get(id=1))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

