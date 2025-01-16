from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import VPS
from .forms import VPSForm
from .filters import VPSFilter
from .serializers import VPSSerializer
from django_filters.views import FilterView

class VPSListView(FilterView):
    model = VPS
    template_name = 'vps_app/vps_list.html'
    context_object_name = 'vps_list'
    filterset_class = VPSFilter

class VPSCreateView(CreateView):
    model = VPS
    form_class = VPSForm
    template_name = 'vps_app/vps_form.html'
    success_url = reverse_lazy('vps_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create VPS'
        return context

class VPSUpdateView(UpdateView):
    model = VPS
    form_class = VPSForm
    template_name = 'vps_app/vps_form.html'
    success_url = reverse_lazy('vps_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Update VPS'
        return context

class VPSDeleteView(DeleteView):
    model = VPS
    template_name = 'vps_app/vps_confirm_delete.html'
    success_url = reverse_lazy('vps_list')

class VPSViewSet(viewsets.ModelViewSet):
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = VPSFilter