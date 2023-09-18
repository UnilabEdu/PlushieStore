from app.admin import SecureModelView
from wtforms.fields import SelectField, TextAreaField
from flask_admin.form.upload import ImageUploadField
from flask_ckeditor.fields import CKEditorField
from os import path
from flask import Markup

PAGE_SIZE = 10


class CityView(SecureModelView):
    column_labels = {
        "name_geo": "სახელი ქართულად",
        "name_eng": "სახელი ინგლისურად",
        "delivery_cost": "ფასი ლარში",
        "delivery_delay": "მიწოდების დრო"
    }
    can_delete = True
    can_edit = True
    column_filters = ["name_geo", "name_eng", "delivery_cost", "delivery_delay"]
    column_searchable_list = ["name_geo", "name_eng", "delivery_cost", "delivery_delay"]
    page_size = PAGE_SIZE


class OrderView(SecureModelView):
    column_labels = {
        "order_id": "შეკვეთის ნომერი",
        "ordered_toys": "შეკვეთილი სათამაშოები",
        "order_price": "სრული ფასი",
        "customer_info": "შემკვეთის მონაცემები",
        "customer_phone": "შემკვეთის ტელეფონის ნომერი",
        "customer_address": "შემკვეთის მისამართი",
        "customer_note": "მომხმარებლის შენიშვნა",
        "order_status": "შეკვეთის სტატუსი",
        "order_date": "შეკვეთის განთავსების თარიღი",
        "delivery_date": "მიტანის თარიღი",
        "admin_note": "ადმინის კომენტარი"
    }
    can_export = True
    form_overrides = {"order_status": SelectField, "admin_note": TextAreaField, "customer_note": TextAreaField}
    form_args = {"order_status": {"choices": ["გადახდილი", "გადაუხდელი", "გაგზავნილი", "მიტანილი", "უკან მობრუნებული"]}}

    column_editable_list = ["admin_note"]
    column_filters = ["order_status", "delivery_date"]

    column_searchable_list = ["order_id", "ordered_toys", "order_price", "customer_info", "customer_phone",
                              "customer_address", "customer_note", "order_status", "order_date", "delivery_date",
                              "admin_note"]

    page_size = PAGE_SIZE


class ToyView(SecureModelView):
    column_list = ["photo", "name_geo", "name_eng", "price", "stock", "is_popular", "category"]
    column_labels = {
        "category": "კატეგორია",
        "photo": "სურათი",
        "name_geo": "სახელწოდება ქართულად",
        "name_eng": "სახელწოდება ინგლისურად",
        "desc_eng": "აღწერა ინგლისურად",
        "desc_geo": "აღწერა ქართულად",
        "price": "ფასი",
        "stock": "რაოდენობა",
        "meta_geo": "Meta desc geo",
        "meta_eng": "Meta desc eng",
        "is_popular": "ჩანს პოპულარულებში"
    }
    column_editable_list = ["is_popular"]
    column_formatters = dict(
        photo=lambda v, c, m, p: Markup(f'<img src="/static/img/products/{m.photo}" width="50">')
    )
    column_filters = ["category", "photo", "name_geo",
                      "name_eng", "desc_eng", "desc_geo",
                      "price", "stock", "is_popular",
                      "meta_geo", "meta_eng"
                      ]
    column_searchable_list = ["photo", "name_geo", "name_eng",
                              "desc_eng", "desc_geo", "price",
                              "stock", "meta_geo", "meta_eng"
                              ]

    form_overrides = {"desc_eng": CKEditorField, "desc_geo": CKEditorField, "meta_eng": TextAreaField,
                      "meta_geo": TextAreaField, 'photo': ImageUploadField}
    form_args = {"photo": {"base_path": path.dirname("app/static/img/products/"),
                           "url_relative_path": "/img/products/"}}

    create_template = "admin/newcreate.html"
    edit_template = "admin/newedit.html"

    page_size = PAGE_SIZE


class ToyCategoryView(SecureModelView):
    column_labels = {
        "photo": "სურათი",
        "name_geo": "სახელი ქართულად",
        "name_eng": "სახელი ინგლისურად",
        "description_geo": "აღწერა ქართულად",
        "description_eng": "აღწერა ინგლისურად"
    }
    column_list = ["name_geo", "name_eng"]
    form_overrides = {"description_eng": TextAreaField, "description_geo": TextAreaField, 'photo': ImageUploadField}
    form_args = {"photo": {"base_path": path.dirname("app/static/img/covers/"),
                           "url_relative_path": "img/covers/"}}
    column_filters = ["name_geo", "name_eng", "description_geo", "description_eng"]
    page_size = PAGE_SIZE

    column_searchable_list = ["name_geo", "name_eng", "description_geo", "description_eng"]
