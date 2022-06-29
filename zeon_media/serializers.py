from rest_framework import serializers
from .models import * 

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = SliderImageSerializer(instance.images.all(), many=True, context=self.context).data
        return representation

class SliderImageSerializer(serializers.ModelSerializer):
    class Meta:
        models = SliderImage
        fields = '__all__'

class AboutUsImageSerializer(serializers.ModelSerializer):
    class Meta:
        models = AboutUsImage
        fields = '__all__'

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = AboutUsImageSerializer(instance.images.all(), many=True, context=self.context).data
        return representation

class PublicOffertSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicOffert
        fields = '__all__'

class CallBackSerializer(serializers.ModelSerializer):
    phone_num = serializers.CharField(required=True,)
    name = serializers.CharField(required=True,)

    class Meta:
        model = CallBack
        fields = ('name', 'phone_num', 'callback_type')


class HelpersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Helpers
        fields = '__all__'

class HelpImageSerializer(serializers.ModelSerializer):
    help = HelpersSerializer(many=True)

    class Meta:
        model = HelpImage
        fields = '__all__'


class OurAdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurAdvantages
        fields = '__all__'

class FuterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Futer
        fields = '__all__'

class FuterLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuterLink
        fields = '__all__'

