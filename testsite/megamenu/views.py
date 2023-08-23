from django.shortcuts import render

def menu_view(request):
    # Xử lý logic liên quan đến menu ở đây
    context = {
        # Các dữ liệu cần truyền vào template
    }
    return render(request, 'megamenu/menu.html', context)
