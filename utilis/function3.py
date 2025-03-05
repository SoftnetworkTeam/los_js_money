from django.db.models import Q
from querystring_parser import parser
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'pageSize'
    max_page_size = 9999


class BaseListAPIView3(ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = StandardResultsSetPagination
    serializer_class = None
    queryset = None

    def _build_filters(self, filters, django_filters, filter_logic):
        for filter_id in filters:
            filter = filters[filter_id]
            my_filter = dict()
            if ('field' in filter) and ('operator' in filter) and ('value' in filter):
                if filter['operator'] == 'startswith' or filter['operator'] == 'endswith' or \
                        filter['operator'] == 'contains':
                    filter['operator'] = 'i' + filter['operator']
                if filter['field'] == 'status_name':
                    filter['field'] = 'status'
                if "." in filter['field']:
                    filter['field'] = filter['field'].replace('.', '__')
                    # my_filter[filter['field']] = filter['value']
                if (filter['value'] == 'true' or filter['value'] == 'false') and filter_logic == 'AND':
                    if filter['operator'] == 'eq':
                        if filter['value'] == 'true':
                            my_filter[filter['field']] = True
                        else:
                            my_filter[filter['field']] = False
                    else:
                        if filter['value'] == 'true':
                            my_filter[filter['field'] + '__' + filter['operator']] = True
                        else:
                            my_filter[filter['field'] + '__' + filter['operator']] = False
                elif (filter['value'] == 'true' or filter['value'] == 'false') and filter_logic == 'OR':
                    my_filter = dict()
                else:
                    if filter['operator'] == 'eq':
                        my_filter[filter['field']] = filter['value']
                    else:
                        my_filter[filter['field'] + '__' + filter['operator']] = filter['value']
            if my_filter:
                django_filters.append(my_filter)
        return django_filters

    def _build_sorts(self, sorts, django_sorts):
        for sort_id in sorts:
            sort = sorts[sort_id]
            if "." in sort['field']:
                sort['field'] = sort['field'].replace('.', '__')
            if ('field' in sort) and ('dir' in sort):
                if sort['dir'].lower() == 'desc':
                    django_sorts.append('-%s' % sort['field'])
                else:
                    django_sorts.append(sort['field'])
        if (len(django_sorts) == 0):
            django_sorts.append('id')
        return django_sorts

    def get_queryset(self, *args, **kwargs):
        arguments = parser.parse(self.request.GET.urlencode())
        # print(arguments)
        filter_arg = list()
        sort_arg = list()
        filter_logic = 'and'
        items = self.queryset
        first_filter = {}
        for key, value in arguments.items():
            if key not in ['take', 'skip', 'page', 'pageSize', 'sort', 'filter']:
                if isinstance(value, dict):
                    for key2, value2 in value.items():
                        first_filter[key + '__' + key2] = value2
                else:
                    first_filter[key] = value
        if first_filter:
            items = items.filter(**first_filter)
        # if "status" in arguments:
        #     items = items.filter(status=arguments['status'])
        if ("filter" in arguments) and ('filters' in arguments['filter']):
            filter_logic = arguments['filter']['logic'].upper()
            filter_arg = self._build_filters(arguments['filter']['filters'], filter_arg, filter_logic)
        if 'sort' in arguments:
            sort_arg = self._build_sorts(arguments['sort'], sort_arg)
        else:
            sort_arg = ['id']
        # filter and sort
        my_filter_qs = Q()
        for creator_filter in filter_arg:
            filters = Q(**creator_filter)
            my_filter_qs.add(filters, filter_logic)
        # print(my_filter_qs)
        if len(sort_arg) > 0:
            items = items.filter(my_filter_qs).order_by(*sort_arg)
        return items
