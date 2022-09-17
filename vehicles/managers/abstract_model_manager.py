from django.db.models import Manager


class AbstractModelManager(Manager):
    def get_active_vehicles(self):
        return self.filter(is_active=True).select_related('model', 'model__brand')

    def get_active_models(self):
        return self.filter(is_active=True).select_related('brand')

    def get_active_brands(self):
        return self.filter(is_active=True)
