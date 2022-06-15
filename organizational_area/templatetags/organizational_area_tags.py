from django import template
from django.db.models import Q

from organizational_area.models import OrganizationalStructureOfficeEmployee


register = template.Library()

@register.simple_tag
def employee_offices(user, structure=None):
    """
    Returns all user offices relationships
    """
    if not user: return None
    query = Q(employee=user)
    query_structure = ()
    if structure:
        query_structure = Q(office__organizational_structure=structure)
    return OrganizationalStructureOfficeEmployee.objects.filter(query,
                                                                query_structure)
