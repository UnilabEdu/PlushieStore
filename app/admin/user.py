from app.admin import SecureModelView


class UserView(SecureModelView):
    column_list = ["first_name","last_name","email", "phone"]
    column_labels = {"first_name": "სახელი", "last_name": "გვარი", "email": "მეილი", "phone": "ტელეფონის ნომერი"}
    can_export = True
    can_create = False
    can_delete = False
