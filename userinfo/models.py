from django.db import models


# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField('用户名', max_length=20, null=False)
    upwd = models.CharField('密码', max_length=200, null=False)
    uemail = models.CharField('邮箱', max_length=40, null=False)
    uphone = models.CharField('手机', max_length=20, null=False)
    time = models.DateTimeField('注册时间', auto_now=True)
    isban = models.BooleanField('禁用', default=False)
    isdelete = models.BooleanField('删除', default=False)

    class Meta:
        db_table = 'userinfo'

    def __str__(self):
        return self.uname