from wtforms.validators import DataRequired

from app.admin import SecureModelView
from wtforms.fields import SelectField, TextAreaField


class CityView(SecureModelView):
    column_labels = {"name_geo": "სახელი ქართულად", "name_eng": "სახელი ინგლისურად", "delivery_cost": "ფასი ლარში",
                     "delivery_delay": "მიწოდების დრო"}
    can_delete = True
    can_edit = True


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
    form_args = {"order_status": {"validators": [DataRequired()],
                                  "choices": ["გადახდილი", "გადაუხდელი", "გაგზავნილი", "მიტანილი", "უკან მობრუნებული"]}}

    column_filters = ["order_status", "delivery_date"]


class ToyView(SecureModelView):
    column_list = ["category", "photo", "name_geo", "name_eng", "price", "stock", "is_popular"]
    column_labels = {
        "category": "კატეგორია",
        "photo": "სურათი",
        "name_geo": "სახელწოდება ქართულად",
        "name_eng": "სახელწოდება ინგლისურად",
        "desc_eng": "აღწერა ინგლისურად",
        "desc_geo": "აღწერა ქართულად",
        "price": "ფასი",
        "stock": "რაოდენობა",
        "is_popular": "პოპულარული/არაპოპულარული"
    }
    column_editable_list = ["is_popular"]
    form_overrides = {"desc_eng": TextAreaField, "desc_geo": TextAreaField}


class ToyCategoryView(SecureModelView):
    column_labels = {
        "name_geo": "სახელი ქართულად",
        "name_eng": "სახელი ინგლისურად",
        "description_geo": "აღწერა ქართულად",
        "description_eng": "აღწერა ინგლისურად"
    }
    column_list = ["name_geo", "name_eng"]
    form_overrides = {"description_eng": TextAreaField, "description_geo": TextAreaField}



