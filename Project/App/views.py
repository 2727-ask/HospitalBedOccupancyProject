from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Hospital,HospitalFacilities
from .serializers import HospitalSerializer,HospitalFacilitiesSerializer

class HospitalAPIView(APIView):
    def get(self, request,pk=None):
        if(pk):
            query = Hospital.objects.filter(id=pk)
            serialized_data = HospitalSerializer(query, many=True)
            return Response({"hospitals": serialized_data.data})
        query = Hospital.objects.all()
        serialized_data = HospitalSerializer(query, many=True)
        return Response({"hospitals":serialized_data.data})

    def post(self, request):
        query = request.data.get("hospitals")
        serializer = HospitalSerializer(data=query)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"status":True})

    def put(self, request, pk):
        saved_hospital = get_object_or_404(Hospital.objects.all(), pk=pk)
        query = request.data.get('hospitals')
        serializer = HospitalSerializer(instance=saved_hospital, data=query, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"success": f"Hospital {saved_hospital.name} updated successfully"})

    def delete(self,request,pk):
        saved_hospital = get_object_or_404(Hospital.objects.all(), pk=pk)
        query = request.data.get('hospitals')
        serializer = HospitalSerializer(instance=saved_hospital, data=query, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"success": f"Hospital {saved_hospital.name} deleted successfully"})



class HospitalFacilitiesAPIView(APIView):
    def get(self,request,pk=None):
        if (pk):
            query = HospitalFacilities.objects.filter(id = pk)
            serialize_data = HospitalFacilitiesSerializer(query, many=True)
            return Response({"facilities": serialize_data.data})
        query = HospitalFacilities.objects.all()
        serialize_data = HospitalFacilitiesSerializer(query,many=True)
        return Response({"facilities":serialize_data.data})

    def post(self,request):
        query = request.data.get("facility")
        serialize = HospitalFacilitiesSerializer(data = query)
        if serialize.is_valid(raise_exception=True):
            serialize.save()
        return Response({"status":True})




