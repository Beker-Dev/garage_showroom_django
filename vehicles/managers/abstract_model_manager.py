from django.db.models import Manager


class AbstractModelManager(Manager):
    def __get_active_base(self):
        return self.filter(is_active=True)

    def __ordering(self, qs):
        return qs.order_by('-id')

    def get_active_vehicles(self):
        return self.__ordering(
            self.__get_active_base().select_related('model', 'model__brand').prefetch_related('image_set')
        )

    def get_active_models(self):
        return self.__ordering(
            self.__get_active_base().select_related('brand')
        )

    def get_active_brands(self):
        return self.__ordering(
            self.__get_active_base()
        )
