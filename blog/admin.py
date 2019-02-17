from django.contrib import admin

from .models import User
from .models import Topic
from .models import Comment
from .models import File
from .models import Image
from .models import Carma
from .models import MapLabel
from .models import KeyWord
from .models import HashTag
#from .models import NewsWall

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(File)
admin.site.register(Image)
admin.site.register(Carma)
admin.site.register(MapLabel)
admin.site.register(KeyWord)
admin.site.register(HashTag)
#admin.site.register(NewsWall)
