from photo.models import *
ps = Photo.objects.all()
for p in ps:
 p.save()


ALTER TABLE photo_photo ADD COLUMN thumb varchar(100);