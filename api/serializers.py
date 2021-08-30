from rest_framework import serializers
from rest_framework.exceptions import ParseError
from .models import PackageRelease, Project
import requests


error = {"error": "One or more packages doesn't exist"}
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageRelease
        fields = ['name', 'version']
        extra_kwargs = {'version': {'required': False}}

    version = serializers.SerializerMethodField() 

    def get_version(self, instance): #função para obter a versão
        r = requests.get(f"https://pypi.org/pypi/{instance.name}/json") # busca na api do pypi

        if r.status_code != 200: # verifica o status code
            raise serializers.ValidationError(f"Package {instance.name} not found on PyPI") 

        data_json = r.json()

        if data_json['info']['version'] != instance.version: # verifica se a versão e diferente
            instance.version = data_json['info']['version']

            instance.save() # salva no banco de dados

        return instance.version # retorna a versão 


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'packages']

    packages = PackageSerializer(many=True)

    def create(self, validated_data):
        
        packages_data = validated_data['packages'] # lista de pacotes
        projeto = Project.objects.create(name=validated_data['name']) # cria o projeto
        
        for package in packages_data:                           
            package_name = package["name"]                                 
            r = requests.get(f"https://pypi.org/pypi/{package_name}/json") # busca na api do pypi


            if r.status_code != 200: 
                projeto.delete() 
                raise ParseError(error) # caso nao encontre o pacote

            PackageRelease.objects.create(project=projeto ,**package) # cria o pacote

        return projeto # retorna o projeto
        
    