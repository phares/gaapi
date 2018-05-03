from rest_framework import serializers


class PolicySerializer(serializers.Serializer):

    policy_no = serializers.CharField(max_length=254, required=False)
    assr_code = serializers.CharField(max_length=254, required=False)
    assr_name = serializers.CharField(max_length=254, required=False)
    email_id = serializers.CharField(max_length=254, required=False)
    telephone_no = serializers.CharField(max_length=254, required=False)
    from_date = serializers.CharField(max_length=254, required=False)
    to_date = serializers.CharField(max_length=254, required=False)
    flex = serializers.CharField(max_length=254, required=False)
    detail = serializers.CharField(max_length=254, required=False)
    result = serializers.CharField(max_length=254, required=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
