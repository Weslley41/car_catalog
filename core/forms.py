from django import forms
from django.core.mail.message import EmailMessage

class contatoForm(forms.Form):
	nome = forms.CharField(label='Nome', max_length=64)
	email = forms.EmailField(label='E-mail', max_length=128)
	assunto = forms.CharField(label='Assunto', max_length=128)
	mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)

	def enviar_mail(self):
		nome = self.cleaned_data['nome']
		email = self.cleaned_data['email']
		assunto = self.cleaned_data['assunto']
		mensagem = self.cleaned_data['mensagem']

		conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'
		email = EmailMessage(
			from_email='contato@cartalog.com',
			to=['contato@cartalog.com'],
			headers={'Reply-To': email},
			subject=assunto,
			body=mensagem,
		)

		email.send()
