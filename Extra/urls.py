from django.urls import path
from . import views

urlpatterns = [
    path("split-evenly/", views.split_evenly, name="split_evenly"),
    path("split-unevenly/", views.split_unevenly, name="split_unevenly"),
    path("split-including-tip-tax/", views.add_tip_tax_and_evenly_split, name="split-including-tip-tax"),
    path("split-with-discount/", views.add_discount_and_evenly_split, name="split-with-discount"),
    path("uneven-split-with-shared-items/", views.shared_items_and_unevenly_split, name="uneven-split-with-shared-items")
]
