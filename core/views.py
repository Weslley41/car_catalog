from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Carro, Vendedor
from .forms import contatoForm

class indexView(FormView):
	template_name = 'index.html'
	form_class = contatoForm
	success_url = reverse_lazy('index')

	def get_context_data(self, **kwargs):
		context = super(indexView, self).get_context_data(**kwargs)
		context['vendedores'] = Vendedor.objects.all()
		context['carros'] = Carro.objects.filter(destaque=True)

		return context


	def form_valid(self, form, *args, **kwargs):
		form.enviar_mail()
		messages.success(self.request, 'Mensagem enviada com sucesso!')

		return super(indexView, self).form_valid(form, *args, **kwargs)


	def form_invalid(self, form, *args, **kwargs):
		messages.error(self.request, 'Não foi possível enviar a mensagem!')

		return super(indexView, self).form_invalid(form, *args, **kwargs)
