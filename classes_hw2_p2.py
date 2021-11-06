import json
import keyword
from typing import Dict


class AdvertAttributes:

    def __init__(self, attributes_dict: Dict[str, str]):
        def unpack_attributes(parent_object, attributes) -> None:
            for attribute in attributes:
                attribute_value = attributes[attribute]
                if keyword.iskeyword(attribute) or attribute == 'price':
                    attribute = f'{attribute}_'
                if not isinstance(attribute_value, dict):
                    setattr(parent_object, attribute, attribute_value)
                else:
                    setattr(parent_object, attribute, AdvertAttributes(
                        attribute_value
                    ))
            return None
        unpack_attributes(self, attributes_dict)

    @property
    def price(self) -> float:
        if hasattr(self, 'price_'):
            if self.price_ < 0:
                raise ValueError('Price must be >= 0')
            else:
                return self.price_
        else:
            return 0

    def __str__(self) -> str:
        return str(self.__dict__)


class ColorizeMixin:

    def __repr__(self) -> str:
        if hasattr(self, 'repr_color_code'):
            return f'\033[0;{self.repr_color_code}m{self.contents.title} | \
{self.contents.price} ₽\033[0;0m'
        else:
            return f'{self.contents.title} | {self.contents.price} ₽'


class BaseAdvert:

    def __init__(self, ad_json: str):
        ad_dict = json.loads(ad_json)
        self.contents = AdvertAttributes(ad_dict)

    def __repr__(self) -> str:
        return f'{self.contents.title} | {self.contents.price} ₽'


class Advert(ColorizeMixin, BaseAdvert):
    repr_color_code = 32

    def __init__(self, ad_json: str):
        super().__init__(ad_json)


if __name__ == '__main__':
    pass
