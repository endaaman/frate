from bbs.models import *
from bbs.views import *
c = Comment.objects.all()
df = DeleteForm(dict(edit_key='13'), instance=c[0])
df.is_valid()



from photo.models import *;ps = Photo.objects.all();ps = Photo.objects.all()