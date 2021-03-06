import rules
from accounts.rules import is_admin, is_manager


@rules.predicate
def is_same_section(user, obj):
    return user.section == obj.section


@rules.predicate
def can_view(user, obj):
    return is_same_section(user, obj) or is_admin(user) or is_manager(user)


rules.add_perm('myapp.same_section', is_same_section | is_admin | is_manager)
