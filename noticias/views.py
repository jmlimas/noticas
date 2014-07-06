# -*- coding: utf-8 -*-

from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
    FormView,
)
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy

from noticias.models import Noticia as NoticiasModel, Rubrica as RubricaModel
from noticias.forms  import NoticiaForm, ContactenosForm


class Noticias(ListView):
    model = NoticiasModel
    template_name = "noticias/list.html"
    context_object_name = "noticias"
    paginate_by = 10
    


class Noticia(DetailView):
    model = NoticiasModel
    template_name = "noticias/detail.html"
    context_object_name = "noticia"


class UpdateNoticia(UpdateView):
    model = NoticiasModel
    template_name = "noticias/form.html"
    form_class = NoticiaForm
    success_url = reverse_lazy("noticias")


class CreateNoticia(CreateView):
    model = NoticiasModel
    template_name = "noticias/form.html"
    form_class = NoticiaForm
    success_url = reverse_lazy("noticias")


class DeleteNoticia(DeleteView):
    model = NoticiasModel
    success_url = reverse_lazy("noticias")
    template_name = "noticias/delete_confirm.html"



class NoticiasDeCine(ListView):
    model = NoticiasModel
    template_name = "noticias/cine_list.html"
    context_object_name = "noticias"

    def get_queryset(self):
        return super(NoticiasDeCine, self).get_queryset().filter(rubric__slug="cine")

class NoticiasDeDeporte(ListView):
    model = NoticiasModel
    template_name = "noticias/deporte_list.html"
    context_object_name = "deportes"

    def get_queryset(self):
        return super(NoticiasDeDeporte, self).get_queryset().filter(rubric__slug="sport")


class NoticiasPaginated(ListView):
    model = NoticiasModel
    template_name = "noticias/paginated_list.html"
    context_object_name = "noticias"
    paginate_by = 8


class Pubrica(DetailView):
    model = RubricaModel
    template_name = "noticias/rubrica.html"
    slug_field = "slug"


class Contactenos(FormView):
    form_class = ContactenosForm
    template_name = "noticias/contactenos.html"
    success_url = reverse_lazy("gracias")


############################## Mixin #####################################
import json
from django.http import HttpResponse
from django.core import serializers

class JSONResponseMixin(object):

    def render_to_response(self, context, **response_kwargs):
        return self.get_json_response(self.convert_context_to_json(context), **response_kwargs)

    def get_json_response(self, content, **response_kwargs):
        return HttpResponse(
            content, content_type='application/json', **response_kwargs
        )

    def convert_context_to_json(self, context):
        options = {}
        if hasattr(self, "serialize_fields"):
            options.update(fields=self.serialize_fields)
        if hasattr(self, "object"):
            to_json = serializers.serialize('python', [getattr(self, "object")], **options)[0]
            return json.dumps(to_json)
        elif hasattr(self, "object_list"):
            return serializers.serialize('json', getattr(self, "object_list"), **options)


class NoticiasJSON(JSONResponseMixin, ListView):
    model = NoticiasModel
    context_object_name = "noticias"