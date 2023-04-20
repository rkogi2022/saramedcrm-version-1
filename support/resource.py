from import_export import resources
from .models import support
from .models import courtesy
 
class supportResource(resources.ModelResource):
    class Meta:
        model = support

class courtesyResource(resources.ModelResource):
    class Meta:
        model = courtesy