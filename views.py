# VIEWS PROJEK #

from django.shortcuts import render, redirect

# Create your views here.

from .forms import PostForm
from .models import *		


def update(request,update_id):
	data_update = LedgerDetail.objects.get(id=update_id)

	data = {
		'transaksi deskripsi'		: data_update.transaksi_deskripsi,
		'nomor akun'				: data_update.nomor_akun,
		'center number'				: data_update.center_number,
		'counterpart id'			: data_update.counterpart_id,
		'reconciliation reference'	: data_update.reconciliation_reference,
		'accounting periode'		: data_update.accounting_periode,
		'debet ledger currency'		: data_update.debet_ledger_currency,
		'credit ledger currency'	: data_update.credit_ledger_currency,

	}

	post_form = PostForm(request.POST or None, initial=data, instance=data_update)

	if request.method == 'POST':
		if post_form.is_valid():
			post_form.save()

		return redirect('projek:index')

	context = {
		'Judul':'Update Data',
		'logo':'projek/img/logo-baezeni.png',
		'post_form':post_form,
	}

	return render(request,'projek/create.html',context)


def delete(request,delete_id):
	LedgerDetail.objects.filter(id=delete_id).delete()


	return redirect('projek:index')


def create(request):
	post_form = PostForm(request.POST or None)

	if request.method == 'POST':
		if post_form.is_valid():
			post_form.save()

			return redirect('projek:index')

	context = {
		'Judul':'Form Input',
        'Subjudul':'Selamat Datang',
        'logo':'projek/img/logo-baezeni.png', 
		'post_form':post_form

	}
	return render(request,'projek/create.html',context)


def index(request):
	posts	= LedgerDetail.objects.all()

	context = {
		'Judul':'Ini ProjekKu',
		'Subjudul':'Selamat Datang',
		'logo':'projek/img/logo-baezeni.png',
		'posts':posts
	}

	return render(request, 'projek/index.html', context)
