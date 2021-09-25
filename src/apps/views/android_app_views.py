from django.shortcuts import render

from apps.models.android_app_model import AndroidApp


class AndroidAppViews:
    def dashboard(request):
        installs = request.GET.get('installs')
        category = request.GET.get('category')
        total_ratings = request.GET.get('total_ratings')
        paid = request.GET.get('paid')

        context = {}
        android_app_objects, total_count = AndroidApp.search(installs=installs, category=category,
                                                             total_ratings=total_ratings, paid=paid)

        context['android_apps'] = android_app_objects
        context['total_count'] = total_count
        return render(request, "android_app/dashboard.html", context)
