import pytest

from main import Category, Product


@pytest.fixture
def sample_category():
    return Category("Electronics", "Electronic gadgets")


@pytest.fixture
def sample_product():
    return Product("Laptop", "High performance laptop", 1500.00, 10)


def test_category_initialization(sample_category):
    assert sample_category.name == "Electronics"
    assert sample_category.description == "Electronic gadgets"


def test_product_initialization(sample_product):
    assert sample_product.name == "Laptop"
    assert sample_product.description == "High performance laptop"
    assert sample_product.price == 1500.00
    assert sample_product.quantity == 10


def test_total_categories(sample_category):
    assert Category.total_categories == 1


def test_total_unique_products(sample_product):
    assert Category.total_unique_products == 1
