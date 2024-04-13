from rest_framework import generics, views
from rest_framework.response import Response

from api.models import Program
from api.modules.program.serializers import ProgramSerializer
from api.modules.services.gpt import get_structured_program_from_gpt_api


class ProgramWithFAQAPIView(views.APIView):
    def post(self, request):
        content = request.data.get("content")
        print(content)
        program_data = get_structured_program_from_gpt_api(content)
        print(program_data)
        programs = self.create_program_with_faq(program_data.get("programs"))
        print(programs)
        return Response(data={"programs": programs})

    def create_program_with_faq(self, json_data):
        program_serializer = ProgramSerializer(data=json_data, many=True)

        program_serializer.is_valid(raise_exception=True)

        program_serializer.save()

        return program_serializer.data
