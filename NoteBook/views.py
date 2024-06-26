import os
import datetime
from .settings import BASE_DIR
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import mdg
from . import info


def index(request):
    file_name_lst = os.listdir(os.path.join(BASE_DIR, "notebooks/"))
    notebook_lst = []
    for name in file_name_lst:
        notebook_lst.append(os.path.splitext(name)[0])
    con = info.data
    con['notebook_list'] = notebook_lst
    return render(request, "index.html", con)


def notebook(request, name):
    pth = os.path.join(BASE_DIR, f"notebooks/{name}.md")
    con = info.data
    con["title"] = name
    if not os.path.exists(pth):
        con['content'] = '404 Not Found.'
    else:
        with open(pth, "r", encoding='utf-8') as f:
            content = f.read()
        con['content'] = content
    return render(request, "notebook.html", con)


def modify(request, name):
    pth = os.path.join(BASE_DIR, f"notebooks/{name}.md")
    con = info.data
    con["title"] = name
    if not os.path.exists(pth):
        con['content'] = f'Create your new notebook {name}'
    else:
        with open(pth, "r", encoding='utf-8') as f:
            content = f.read()
        con['content'] = content
    return render(request, "modify.html", con)


unavailable_char = '\/:*?"<>|'


def available_filename(name, path):
    name = name.lstrip()
    if name == ".md":
        now_time = datetime.datetime.now()
        now_time_str = now_time.strftime("%Y-%m-%d-%H-%M-%S")
        name = now_time_str + ".md"
    for c in unavailable_char:
        name = name.replace(c, "_")
    if not os.path.exists(os.path.join(path, name)):
        return name
    cnt = 1
    names = os.path.splitext(name)
    while os.path.exists(os.path.join(path, names[0] + '_' + str(cnt) + names[1])):
        cnt += 1
    return names[0] + '_' + str(cnt) + names[1]


@csrf_exempt
def upload_image(request):
    if request.method == "POST":
        try:
            img = request.FILES['editormd-image-file']
            name = available_filename(img.name, os.path.join(BASE_DIR, "image/"))
            with open(os.path.join(BASE_DIR, "image/" + name), "wb") as f:
                for chunk in img.chunks():
                    f.write(chunk)
                    f.flush()
            return JsonResponse({"success": 1, "message": "Successfully", "url": "/image/" + name})
        except:
            return JsonResponse({"success": 0, "message": "Failed"})


@csrf_exempt
def upload_modify(request):
    if request.POST:
        pre = request.POST['pre']
        if os.path.exists(os.path.join(BASE_DIR, f"notebooks/{pre}.md")):
            os.remove(os.path.join(BASE_DIR, f"notebooks/{pre}.md"))
        name = available_filename(request.POST['title'] + ".md", os.path.join(BASE_DIR, "notebooks/"))
        with open(os.path.join(BASE_DIR, f"notebooks/{name}"), "w", encoding='utf-8') as f:
            content = request.POST['content']
            content = str(content).replace('\r', '')
            f.write(content)
        return redirect('/notebook/' + os.path.splitext(name)[0])
    return HttpResponse("404")


def upload_del(request, name):
    if os.path.exists(os.path.join(BASE_DIR, f"notebooks/{name}.md")):
        os.remove(os.path.join(BASE_DIR, f"notebooks/{name}.md"))
    return redirect('/')

