from io import BytesIO
from django.shortcuts import render, redirect, HttpResponse

from site0219.utils.forms import UserForm
from site0219 import models
from site0219.utils.code import check_code


def main(request):
    if request.method == "GET":
        form = UserForm()
        return render(request, 'login.html', {'form': form})
    else:
        form = UserForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('password'))
            input_imgcode = form.cleaned_data.pop('img_code')
            code = request.session.get('sess_img_code', '')
            if input_imgcode.upper() != code.upper():
                form.add_error('img_code', '验证码错误')
                return render(request, 'login.html', {'form': form})
            admin_obj = models.UserInfo.objects.filter(**form.cleaned_data).first()
            if not admin_obj:
                form.add_error('password', '账号或密码错误')
                return render(request, 'login.html', {'form': form})
            request.session['info'] = {'id': admin_obj.id, 'username': admin_obj.username,
                                       'password': admin_obj.password}
            request.session.set_expiry(60 * 60 * 24)
            return redirect(to='/index/')
        return render(request, 'login.html', {'form': form})


def imgcode(request):
    img, str_img = check_code()
    request.session['sess_img_code'] = str_img
    request.session.set_expiry(60)
    stream = BytesIO()
    img.save(stream, 'png')
    # print(str_img)
    return HttpResponse(stream.getvalue())


def logout(request):
    request.session.clear()
    return redirect('/login/')
