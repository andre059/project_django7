from rest_framework.permissions import BasePermission


class IsUserOrStaff(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:  # проверка на менеджера
            return True

        # проверка на владельца и оплачен ли у него курс
        return request.user == view.get_object().user  # and request.user.course_paid


class UserIsStaff(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:  # проверка на менеджера
            return True
        else:
            return False
