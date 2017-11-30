from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from crum import get_current_request

class CreateUpdateModel(models.Model):
    created = models.DateTimeField(auto_now_add=True,editable=False)
    updated = models.DateTimeField(auto_now=True,editable=False)
    create_user = models.ForeignKey(User,null=True,blank=True,related_name="+",editable=False,on_delete=models.CASCADE)
    update_user = models.ForeignKey(User,null=True, blank=True,related_name="+",editable=False,on_delete=models.CASCADE)
    guid = models.CharField(null=True,blank=True,max_length=64,editable=False)
    archived = models.BooleanField(default=False,verbose_name=_("archived"))

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        try:
            req=get_current_request()
            request_user=req.user
            if not self.create_user:
                self.create_user=request_user
            self.update_user=request_user
        except:
            pass
        super(CreateUpdateModel, self).save(*args, **kwargs)