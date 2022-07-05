

from site0219 import models
from django import forms
from site0219.utils.BootStrap import BootStarpModelForm, BootStarpForm

from site0219.utils.encrypt import md5


# class Userinfo_form(BootStarpModelForm):
#     name = forms.CharField(min_length=5)
#
#     class Meta:
#         model = models.User_info
#         fields = ['name', 'password', 'age', 'account', 'create_time', 'department', 'gender']
#
#
# class PretyForm(BootStarpModelForm):
#     # num = forms.CharField(
#     #     label='手机号',
#     #     validators=[RegexValidator(r'^1\d{10}$', '手机号格式错误')]
#     # )
#
#     class Meta:
#         model = models.PretyNum
#         fields = ['num', 'price', 'level', 'status']
#
#     def clean_num(self):
#         num = self.cleaned_data['num']
#         if re.match(r'1[3,4,5,7,8]\d{9}', num):
#             if models.PretyNum.objects.exclude(id=self.instance.pk).filter(num=num).exists():
#                 raise ValidationError('手机号已存在')
#             return num
#         raise ValidationError('手机号格式错误')
#
#
# class AdminForm(BootStarpModelForm):
#     confirm_pwd = forms.CharField(label='确认密码', widget=forms.PasswordInput, max_length=64)
#
#     class Meta:
#         model = models.AdminInfo
#         fields = ['username', 'password', 'confirm_pwd']
#         widgets = {
#             'password': forms.PasswordInput
#         }
#
#     def clean_password(self):
#         password = self.cleaned_data.get('password')
#         return md5(password)
#
#     def clean_confirm_pwd(self):
#         password = self.cleaned_data.get('password')
#         confirm_pwd = self.cleaned_data.get('confirm_pwd')
#         if password == md5(confirm_pwd):
#             return md5(confirm_pwd)
#         else:
#             raise ValidationError('密码不一致')
#
#
# class AdminEditForm(BootStarpModelForm):
#     class Meta:
#         model = models.AdminInfo
#         fields = ['username']
#
#
# class AdminResetForm(AdminForm):
#     class Meta:
#         model = models.AdminInfo
#         fields = ['password', 'confirm_pwd']
#         widgets = {
#             'password': forms.PasswordInput
#         }
#
#
# class AccountForm(BootStarpForm):
#     username = forms.CharField(
#         label='用户名',
#         widget=forms.TextInput
#     )
#     password = forms.CharField(
#         label='密码',
#         widget=forms.PasswordInput
#     )
#     img_code = forms.CharField(
#         label='图片验证码',
#         widget=forms.TextInput
#     )
#
#     def clean_password(self):
#         password = self.cleaned_data.get('password')
#         return md5(password)
#
#
# class AjaxForm(BootStarpModelForm):
#     class Meta:
#         model = models.AjaxTest
#         fields = '__all__'
#         widgets = {
#             "detail": forms.TextInput
#         }
#
#
# class OrderForm(BootStarpModelForm):
#     class Meta:
#         model = models.OrderManage
#         exclude = ['orderNum', 'orderAdmin']


'''
bilibili
'''


class NewAniModelForm(BootStarpModelForm):
    class Meta:
        model = models.NewAni
        fields = '__all__'



class RankingForm(forms.ModelForm):
    exclude_fields=[]
    class Meta:
        model=models.Ranking
        fields='__all__'

class UserForm(BootStarpForm):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput
    )
    img_code = forms.CharField(
        label='图片验证码',
        widget=forms.TextInput
    )

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return md5(password)