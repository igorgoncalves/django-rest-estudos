from django.shortcuts import get_object_or_404, get_list_or_404


class MultipleFieldLookupMixin(object):
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(self.serializer_class.Meta.model, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj
     
    def get_queryset(self):
        
        filter = {}
        for field in self.lookup_fields:
            print(field)
            if self.kwargs[field]: # Ignore empty fields.
                filter[field] = self.kwargs[field]        
        
        queryset = get_list_or_404(self.serializer_class.Meta.model, **filter)  # Lookup the object

        queryset = self.filter_queryset(queryset)  # Apply any filter backends

        return queryset