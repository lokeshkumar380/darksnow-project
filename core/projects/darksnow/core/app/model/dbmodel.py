from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, JSONAttribute, MapAttribute, ListAttribute, NumberAttribute


class DesignerModelIndex(GlobalSecondaryIndex):
    class Meta:
        index_name = 'designer-index'
        read_capacity_units = 1
        write_capacity_units = 1
        # All attributes are projected
        projection = AllProjection()

    timestamp = NumberAttribute(hash_key=True)


class DesignerImageMap(MapAttribute):
    timestamp = UnicodeAttribute()
    image_url = UnicodeAttribute()
    image_name = UnicodeAttribute()


class DesignerModel(Model):
    """
        A DynamoDB Designer
        """

    class Meta:
        table_name = 'designer'
        read_capacity_units = 1
        write_capacity_units = 1
        region = 'us-east-1'

        # host = "http://localhost:8095"

    designer_id = UnicodeAttribute(hash_key=True)
    timestamp = NumberAttribute(null=False)
    first_name = UnicodeAttribute(null=True)
    last_name = UnicodeAttribute(null=True)
    password = JSONAttribute(null=False)
    data = ListAttribute(of=DesignerImageMap)
    designer_index = DesignerModelIndex()
