import rules
from .models import PermissionType


@rules.predicate
def is_admin(user):
    return user.permission_type == PermissionType.ADMIN.value


@rules.predicate
def is_manager(user):
    return user.permission_type == PermissionType.MANAGER.value


@rules.predicate
def is_employee(user):
    return user.permission_type == PermissionType.EMPLOYEE.value


rules.add_perm('accounts.admin', is_admin)
rules.add_perm('accounts.manager', is_admin | is_manager)
rules.add_perm('accounts.employee', is_admin | is_manager | is_employee)
