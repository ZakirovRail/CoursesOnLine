# class ShippingContainer:
#     next_serial = 1337
#
#     def __init__(self, owner_code, contents):
#         self.owner_code = owner_code
#         self.contents = contents
#         self.serial = ShippingContainer.next_serial
#         ShippingContainer.next_serial += 1

# c1 = ShippingContainer("YML", "books")
# print(c1.owner_code)
# print(c1.contents)
# ==================================================================================================================
# another implementation with staticmethod
# class ShippingContainer:
#     next_serial = 1337
#
#     @staticmethod
#     def _get_next_serial():
#         result = ShippingContainer.next_serial
#         ShippingContainer.next_serial += 1
#         return result
#
#     def __init__(self, owner_code, contents):
#         self.owner_code = owner_code
#         self.contents = contents
#         self.serial = ShippingContainer._get_next_serial()

# ==================================================================================================================
# another implementation with class method

# class ShippingContainer:
#     next_serial = 1337
#
#     @classmethod
#     def _get_next_serial(cls):
#         result = cls.next_serial
#         cls.next_serial += 1
#         return result
#
#     def __init__(self, owner_code, contents):
#         self.owner_code = owner_code
#         self.contents = contents
#         self.serial = ShippingContainer._get_next_serial()

# ==================================================================================================================
# another implementation with class method

# class ShippingContainer:
#     next_serial = 1337
#
#     @classmethod
#     def _get_next_serial(cls):
#         result = cls.next_serial
#         cls.next_serial += 1
#         return result
#
#     @classmethod
#     def create_empty(cls, owner_code):
#         return cls(owner_code, contents=None)
#
#     @classmethod
#     def create_with_items(cls, owner_code, items):
#         return cls(owner_code, contents=list(items))
#
#     def __init__(self, owner_code, contents):
#         self.owner_code = owner_code
#         self.contents = contents
#         self.serial = ShippingContainer._get_next_serial()
# ==================================================================================================================
import iso6346


# class ShippingContainer:
#     next_serial = 1337
#
#     @staticmethod
#     def _make_bic_code(owner_code, serial):
#         return iso6346.create(owner_code=owner_code,
#                               serial=str(serial).zfill(6))
#
#     @classmethod
#     def _get_next_serial(cls):
#         result = cls.next_serial
#         cls.next_serial += 1
#         return result
#
#     @classmethod
#     def create_empty(cls, owner_code):
#         return cls(owner_code, contents=None)
#
#     @classmethod
#     def create_with_items(cls, owner_code, items):
#         return cls(owner_code, contents=list(items))
#
#     def __init__(self, owner_code, contents):
#         self.contents = contents
#         self.bic = ShippingContainer._make_bic_code(
#             owner_code=owner_code,
#             serial=ShippingContainer._get_next_serial())


#from shipping import *
# c = ShippingContainer.create_empty('YML')
#c.bic -> 'YMLU0013374'


# ==================================================================================================================
import iso6346
# class ShippingContainer:
#     next_serial = 1337
#
#     @staticmethod
#     def _make_bic_code(owner_code, serial):
#         return iso6346.create(owner_code=owner_code,
#                               serial=str(serial).zfill(6))
#
#     @classmethod
#     def _get_next_serial(cls):
#         result = cls.next_serial
#         cls.next_serial += 1
#         return result
#
#     @classmethod
#     def create_empty(cls, owner_code):
#         return cls(owner_code, contents=None)
#
#     @classmethod
#     def create_with_items(cls, owner_code, items):
#         return cls(owner_code, contents=list(items))
#
#     def __init__(self, owner_code, contents):
#         self.contents = contents
#         self.bic = self._make_bic_code(
#             owner_code=owner_code,
#             serial=ShippingContainer._get_next_serial())
#
# class RefrigeatedShippingContainer(ShippingContainer):
#
#     @staticmethod
#     def _make_bic_code(owner_code, serial):
#         return iso6346.create(owner_code=owner_code,
#                               serial=str(serial).zfill(6),
#                               category='R')
# from shipping import *
# c = RefrigeatedShippingContainer('MAE', 'fish')
# c.bic


# ==================================================================================================================
# using property decorator
import iso6346

# class ShippingContainer:
#
#     HEIGHT_FT = 8.5
#     WIDTH_FT = 8.0
#
#     next_serial = 1337
#
#     @staticmethod
#     def _make_bic_code(owner_code, serial):
#         return iso6346.create(owner_code=owner_code,
#                               serial=str(serial).zfill(6))
#
#     @classmethod
#     def _get_next_serial(cls):
#         result = cls.next_serial
#         cls.next_serial += 1
#         return result
#
#     @classmethod
#     def create_empty(cls, owner_code, length_ft, *args, **kwargs):
#         return cls(owner_code, length_ft, contents=None, *args, **kwargs)
#
#     @classmethod
#     def create_with_items(cls, owner_code, length_ft, items, *args, **kwargs):
#         return cls(owner_code, length_ft, contents=list(items), *args, **kwargs)
#
#     def __init__(self, owner_code, length_ft, contents):
#         self.contents = contents
#         self.length_ft = length_ft
#         self.bic = self._make_bic_code(
#             owner_code=owner_code,
#             serial=ShippingContainer._get_next_serial())
#
#     @property
#     def volume_f3(self):
#         return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft
#
#
# class RefrigeatedShippingContainer(ShippingContainer):
#
#     MAX_CELSIUS = 4.0
#
#     FRIDGE_VOLUME_FT3 = 100
#
#     @staticmethod
#     def _make_bic_code(owner_code, serial):
#         return iso6346.create(owner_code=owner_code,
#                               serial=str(serial).zfill(6),
#                               category='R')
#
#     @staticmethod
#     def _c_to_f(celsius):
#         return celsius * 9/5 + 32
#
#     @staticmethod
#     def _f_to_c(fahrenheit):
#         return (fahrenheit - 32) * 5/9
#
#     def __init__(self, owner_code, length_ft, contents, celsius):
#         super().__init__(owner_code, length_ft, contents)
#         self.celsius = celsius
#
#     @property
#     def celsius(self):
#         return self._celsius
#
#     @celsius.setter
#     def celsius(self, value):
#         if value > RefrigeatedShippingContainer.MAX_CELSIUS:
#             raise ValueError("Temperature too hot")
#         self._celsius = value
#
#     @property
#     def fahrenheit(self):
#         return RefrigeatedShippingContainer._c_to_f(self.celsius)
#
#     @fahrenheit.setter
#     def fahrenheit(self, value):
#         self.celsius = RefrigeatedShippingContainer._f_to_c(value)
#
#     @property
#     def volume_ft3(self):
#         return super().volume_f3 - RefrigeatedShippingContainer.FRIDGE_VOLUME_FT3


# from shipping import *
# c2 = ShippingContainer.create_empty('YML', ["fish"], celsius=-18.0)
# c2.celsius
# from shipping import *
# c = ShippingContainer.create_empty('YML', length_ft=20)
# c.volume_f3
# ==================================================================================================================
import iso6346


class ShippingContainer:

    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 1337

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6))

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code, length_ft, *args, **kwargs):
        return cls(owner_code, length_ft, contents=None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, *args, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), *args, **kwargs)

    def __init__(self, owner_code, length_ft, contents):
        self.contents = contents
        self.length_ft = length_ft
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._get_next_serial())

    def _calc_volume(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft

    @property
    def volume_f3(self):
        return self._calc_volume()


class RefrigeatedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    FRIDGE_VOLUME_FT3 = 100

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6),
                              category='R')

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5/9

    def __init__(self, owner_code, length_ft, contents, celsius):
        super().__init__(owner_code, length_ft, contents)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._set_celsius(value)

    def _set_celsius(self, value):
        if value > RefrigeatedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot")
        self._celsius = value

    @property
    def fahrenheit(self):
        return RefrigeatedShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeatedShippingContainer._f_to_c(value)

    def _calc_volume(self):
        return super()._calc_volume() - RefrigeatedShippingContainer.FRIDGE_VOLUME_FT3


class HeatedRefrigeratedShippingCOntainer(RefrigeatedShippingContainer):

    MIN_CELSIUS = -20

    def _set_celsius(self, value):
        if not (HeatedRefrigeratedShippingCOntainer.MIN_CELSIUS
                <= value
                <= RefrigeatedShippingContainer.MAX_CELSIUS):
            raise ValueError("Temperature out of range")
        super()._set_celsius(value)







