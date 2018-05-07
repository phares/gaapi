from rest_framework import serializers


class PolicySerializer(serializers.Serializer):

    policy_no = serializers.CharField(read_only=False, max_length=30, required=False)
    assr_code = serializers.CharField(read_only=True, max_length=99, required=False)
    assr_name = serializers.CharField(read_only=True, max_length=99, required=False)
    email_id = serializers.CharField(read_only=True, max_length=99, required=False)
    telephone_no = serializers.CharField(read_only=True, max_length=99, required=False)
    from_date = serializers.CharField(read_only=True, max_length=99, required=False)
    to_date = serializers.CharField(read_only=True, max_length=99, required=False)
    flex = serializers.CharField(read_only=True, max_length=99, required=False)
    detail = serializers.CharField(read_only=True, max_length=499, required=False)
    result = serializers.CharField(read_only=True, max_length=99, required=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
