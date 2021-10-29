from django.db.models import fields
from rest_framework import serializers
# from watchlist_app.models import WatchList
# from watchmate.watchlist_app.models import WatchList,StreamPlatformSerailzer
from watchlist_app.models import WatchList,StreamPlatform,Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"


class WatchListSerializer(serializers.ModelSerializer):
    reviews=ReviewSerializer(many=True,read_only=True)
    class Meta:
        model=WatchList
        fields="__all__"

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True,read_only=True)
    
    class Meta:
        model=StreamPlatform
        fields="__all__"        

    


    # def validate(self,data):
    #     if data['name']== data['discription']:
    #        raise serializers.ValidationError("Title and discription should be different")
    #     else:
    #         return data   
    # def validate_name(self,value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("name is to short")
    #     else:
    #         return value    





# def name_length(value):
#     if len(value)<2:
#             raise serializers.ValidationError("name is to short")


# class MovieSerailzer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     discription = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)


#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.discription = validated_data.get('discription',instance.discription)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    

#     def validate(self,data):
#         if data['name']== data['discription']:
#            raise serializers.ValidationError("Title and discription should be different")
#         else:
#             return data   
#     # def validate_name(self,value):
#     #     if len(value)<2:
#     #         raise serializers.ValidationError("name is to short")
#     #     else:
#     #         return value    
