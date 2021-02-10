import sys
sys.path.append('.')

from backend.models.pool import Pool
import pytest


class TestPool:
    def test_create_instance(self):
        pool = Pool(1, 1, 1, False)
        assert isinstance(pool, Pool)

    @pytest.mark.parametrize("fk_product", ['a', '3.14', ['1', '2']])
    def test_fk_product_not_valid(self, fk_product):
        with pytest.raises(TypeError):
            Pool(fk_product, 1, 1, False)

    @pytest.mark.parametrize("fk_seller", ['a', '3.14', ['1', '2']])
    def test_fk_seller_not_valid(self, fk_seller):
        with pytest.raises(TypeError):
            Pool(1, fk_seller, 1, False)

    @pytest.mark.parametrize("fk_category", ['a', '3.14', ['1', '2']])
    def test_fk_category_not_valid(self, fk_category):
        with pytest.raises(TypeError):
            Pool(1, 1, fk_category, False)

    @pytest.mark.parametrize("approved", [None, 1, 'bla'])
    def test_approved_not_valid(self, approved):
        with pytest.raises(TypeError):
            Pool(1, 1, 1, approved)
