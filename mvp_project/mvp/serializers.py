from rest_framework import serializers
from .models import Player, Team

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        read_only=True
    )

    player_url = serializers.ModelSerializer.serializer_url_field(
        view_name='player_detail'
    )

    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        source='team'
    )

    class Meta:
        model = Player
        fields = ('id', 'player_url', 'name', 'team', 'team_id', 'position', 'age', 'is_injured')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    players = serializers.HyperlinkedRelatedField(
        view_name='player_detail',
        many=True,
        read_only=True
    )

    team_url = serializers.ModelSerializer.serializer_url_field(
        view_name='team_detail'
    )

    class Meta:
        model = Team
        fields = ('id', 'team_url', 'name', 'location', 'division', 'wins', 'losses', 'players',)