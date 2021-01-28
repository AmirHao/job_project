from job.models.history import HistoricalModels
from job.models.company import Company
from job.models.company2user import Company2User
from job.models.jianli import JianLi
from job.models.role import Role
from job.models.user import User


# class ModelRouter:
#     """
#     A router to control all database operations on models in the
#     auth and contenttypes applications.
#     """
#
#     def db_for_read(self, model, **hints):
#         """
#         Attempts to read auth and contenttypes models go to auth_db.
#         """
#         if model and hasattr(model, 'Meta') and model.Meta is HistoricalModels.Meta:
#             return 'historical_records'
#         return None
#
#     def db_for_write(self, model, **hints):
#         """
#         Attempts to write auth and contenttypes models go to auth_db.
#         """
#         if model and hasattr(model, 'Meta') and model.Meta is HistoricalModels.Meta:
#             return 'historical_records'
#         return None
#
#     # def db_for_write(self, model, **hints):
#     #     """
#     #     Attempts to write auth and contenttypes models go to auth_db.
#     #     """
#     #     if model:
#     #         model_class = str(model).split('.')[-1]
#     #         if model_class.startswith('Historical'):
#     #             return 'historical_records'
#     #     return None
#     #
#     # def allow_relation(self, obj1, obj2, **hints):
#     #     """
#     #     Allow relations if a model in the auth or contenttypes apps is
#     #     involved.
#     #     """
#     #     if (
#     #         obj1._meta.app_label in self.route_app_labels or
#     #         obj2._meta.app_label in self.route_app_labels
#     #     ):
#     #        return True
#     #     return None
#
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """ databases 为 historical_records 的，只做 historical_records migrations
#         """
#         if db == 'historical_records':
#             if app_label in ('auth', 'contenttypes'):
#                 return True
#             if model_name and model_name.startswith('historical'):
#                 return True
#             return False
#         if model_name and model_name.startswith('historical'):
#             return False
#         return None
