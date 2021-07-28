from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from devices.forms import FilterForm, SearchForm
from .models import Device


class List(ListView):
    model = Device
    context_object_name = "devices"
    template_name = "inc/result.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter_form = FilterForm
        search_form = SearchForm
        context['filter_form'] = filter_form
        context['search_form'] = search_form
        return context


class For(TemplateView):

    def get(self, request):
        all_device = Device.objects.all()
        context = {
            "all_device": all_device,
        }

        return render(request, template_name="inc/device.html", context=context)

    def post(self, request):
        query = request.POST["search"]
        result_list = Device.objects.filter(Q(title__icontains=query) |
                                            Q(address__icontains=query) |
                                            Q(category__contains=query)
                                            )
        query1 = request.POST["search1"]
        list_type = Device.objects.filter(category__contains=query1)
        if list_type:
            context = {
                "list_type": list_type,
                "query1": query1,
            }

        elif result_list.count() != 0:
            context = {
                "result_list": result_list,
                "query": query,
            }
        else:
            context = {
                "empty": "Ничего не найдено !",
                "query": query,
            }
        return render(request, template_name="inc/result.html", context=context)