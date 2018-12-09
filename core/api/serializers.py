from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from atracoes.api.serializers import AtracaoSerializer
from atracoes.models import Atracao
from core.models import PontoTuristico
from enderecos.models import Endereco


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes', 'comentarios', 'avaliacoes', 'endereco'
                  , 'descricao_completa', 'descricao_completa2')
        read_only_files = ('comentarios', 'avaliacoes')

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def get_descricao_completa(self, obj):
        return '%s - %s ' % (obj.nome, obj.descricao)

    def create(self, validated_data):
        """
        permitindo a inserção de objetos aninhados
        :param validated_data:
        :return: um ponto turistico criando atrações, endereço em conjunto
        """
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        #Endreço é um FK
        end = Endereco.objects.create(**endereco)
        ponto.endereco = end

        return ponto
