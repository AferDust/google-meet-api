from rest_framework import serializers

from api.models import Program, ProgramFAQ


class ProgramFAQSerializer(serializers.ModelSerializer):
    link = serializers.URLField(allow_null=True, required=False)

    class Meta:
        model = ProgramFAQ
        fields = ("question", "answer", "link")


class ProgramSerializer(serializers.ModelSerializer):
    link = serializers.URLField(allow_null=True, required=False)
    faqs = ProgramFAQSerializer(many=True)

    class Meta:
        model = Program
        fields = ("name", "description", "link", "faqs")

    def create(self, validated_data):
        faqs_data = validated_data.pop('faqs', None)
        program = Program.objects.create(**validated_data)
        for faq_data in faqs_data:
            ProgramFAQ.objects.create(program=program, **faq_data)
        return program
