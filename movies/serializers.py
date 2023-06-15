from rest_framework import serializers

from movies.models import Movie, Rated


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False)
    rating = serializers.ChoiceField(choices=Rated.choices, required=False)
    synopsis = serializers.CharField(required=False)

    added_by = serializers.ReadOnlyField(source="user.email")

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)
