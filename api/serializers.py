from rest_framework import serializers
from rest_framework.exceptions import ParseError, ValidationError
from .models import PackageRelease, Project
import requests


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageRelease
        fields = ['name', 'version']
        extra_kwargs = {'version': {'required': False}}

    version = serializers.SerializerMethodField() # falo que o campo version e um metodo personalisado

    def get_version(self, instance): #função para obter a versão
        r = requests.get(f"https://pypi.org/pypi/{instance.name}/json") # busca na api do pypi

        if r.status_code != 200: # verifica o status code
            raise serializers.ValidationError(f"Package {instance.name} not found on PyPI") # caso nao encontre o pacote

        data_json = r.json() # pega o json


        if data_json['info']['version'] != instance.version: # verifica se a versão e diferente
            instance.version = data_json['info']['version'] # atualiza a versão

            instance.save() # salva no banco de dados

        return instance.version # retorna a versão


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'packages']

    packages = PackageSerializer(many=True)

    def create(self, validated_data):
        
        # TODO
        # - Processar os pacotes recebidos
        # - Persistir informações no banco
        packages_data = validated_data['packages'] # lista de pacotes
        projeto = Project.objects.create(name=validated_data['name']) # cria o projeto
        
        for package in packages_data:                           # percorro todos os pacoters
            _package = package["name"]                                 # pego o nome do pacote
            r = requests.get(f"https://pypi.org/pypi/{_package}/json") # busca na api do pypi


            if r.status_code != 200: # verifica o status code
                projeto.delete() # caso nao encontre o pacote

                raise ParseError("One or more packages doesn't exist") # caso nao encontre o pacote

            PackageRelease.objects.create(project=projeto ,**package) # cria o pacote

        return projeto # retorna o projeto
        
        
        #packages = validated_data['packages']
        #return Project(name=validated_data['name'])
