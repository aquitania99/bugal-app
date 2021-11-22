"""Contact Serializers"""

# Django REST Frameworks
from rest_framework import serializers

# Model
from bugal.base.models import Contact, Guardian

# Serializers
# from bugal.users.serializers import UserModelSerializer
from .guardians import GuardianModelSerializer


class ContactModelSerializer(serializers.ModelSerializer):
    """Contact model serializer"""
    guardian = GuardianModelSerializer(required=False)

    class Meta:
        """Meta class."""
        model = Contact

        fields = (
            "uuid",
            "type",
            "user",
            "guardian",
            "relationship",
            "email",
            "last_name",
            "first_name",
            "org_name",
            "gender",
            "NDISID",
            "dob",
            "date_created",
            "last_updated",
            "phone_number",
            "address_unit",
            "address_number",
            "address_street",
            "address_suburb",
            "address_state_id",
            "address_country_id",
            "address_postcode",
            "address_lat",
            "address_lon",
            "timezone",
            "address_line",
            "soft_deleted"
        )
        read_only_fields = ('user',)
    
    def create(self, validated_data):
        if validated_data.__contains__('guardian'):
            guardian_data = validated_data.pop('guardian')
            Guardian.objects.update_or_create(**guardian_data)
            qry_guardian = Guardian.objects.get(email=guardian_data['email'])
            validated_data['guardian_id'] = qry_guardian.id
            validated_data['has_guardian'] = True
            contact = Contact.objects.create(**validated_data)
        else:
            contact = Contact.objects.create(**validated_data)
        return contact
    
    def update(self, instance, validated_data, partial=True):
        if validated_data.__contains__('guardian'):
            guardian_data = validated_data.pop('guardian')
            Guardian.objects.update_or_create(**guardian_data)
            qry_guardian = Guardian.objects.get(email=guardian_data['email'])
            guardian = GuardianModelSerializer(qry_guardian, data=guardian_data)
            guardian.is_valid(raise_exception=False)
            guardian.save()
            validated_data['guardian_id'] = guardian.data['id']
            validated_data['has_guardian'] = True
            
        return super().update(instance, validated_data)
    
    def destroy(self, instance, validated_data, partial=True):
        import pdb; pdb.set_trace()    
        get_contact = Contact.objects.get(user=self.request.user, soft_deleted=False)
    #     get_contact.soft_deleted = True
    #     serializer = ContactModelSerializer(get_contact).data
    #     import pdb; pdb.set_trace()
        # Contact.objects.update(**serializer)
        return super().update(instance, validated_data)

    def get_guardian(self, email):
        try:
            get_guardian = Guardian.objects.filter(email=email)
            return get_guardian
        except Exception as e:
            raise e
class ContactInfoSerializer(serializers.ModelSerializer):
    """Client basic information serializer"""
    
    class Meta:
        """Meta class."""
        model = Contact

        fields = ('uuid',
                  'user',
                  'first_name', 
                  'last_name', 
                  'email',
                  'guardian')

