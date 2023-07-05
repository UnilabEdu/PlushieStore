from app.admin import SecureModelView

PAGE_SIZE = 10


class UserView(SecureModelView):
    column_list = ["first_name", "last_name", "email", "phone"]
    column_labels = {"first_name": "სახელი", "last_name": "გვარი", "email": "მეილი", "phone": "ტელეფონის ნომერი"}
    column_filters = ["first_name", "last_name", "email", "phone"]
    column_searchable_list = ["first_name", "last_name", "email", "phone"]

    can_export = True
    can_create = False
    can_delete = False
    page_size = PAGE_SIZE
