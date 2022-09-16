from django.db.models import Manager


class AbstractModelManager(Manager):
    def get_active(self):
        return self.filter(is_active=True)
