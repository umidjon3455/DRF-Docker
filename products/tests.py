from django.test import SimpleTestCase

from products.serializers import ProductSerializer


class ProductSerializerFieldsTests(SimpleTestCase):
    def test_product_serializer_exposes_price_and_category(self):
        self.assertIn('price', ProductSerializer.Meta.fields)
        self.assertIn('category', ProductSerializer.Meta.fields)
