from django import forms

from .models import LedgerDetail

class PostForm(forms.ModelForm):
	class Meta:
		model = LedgerDetail
		fields = [
			'transaksi_deskripsi',
			'nomor_akun',
			'center_number',
			'counterpart_id',
			'reconciliation_reference',
			'accounting_periode',
			'debet_ledger_currency',
			'credit_ledger_currency',
			'supporting_dokumen',
		]

		widgets = {
			'transaksi_deskripsi': forms.Textarea(
				attrs = {
					'class':'form-control',
					'placeholder':'terserah mau diisi apa ge',}
				),

			'reconciliation_reference': forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'isi dong',}
				),
			'accounting_periode': forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'ayo dong',}
				),
			'nomor_akun': forms.Select(
				attrs = {
					'class':'form-control',
					}
				),
			'center_number': forms.Select(
				attrs = {
					'class':'form-control',
					}
				),
			'counterpart_id': forms.Select(
				attrs = {
					'class':'form-control',
					}
				),
			'debet_ledger_currency': forms.NumberInput(
				attrs = {
					'class':'form-control',
					}
				),
			'credit_ledger_currency': forms.NumberInput(
				attrs = {
					'class':'form-control',
					}
				),
			'supporting_dokumen': forms.FileInput(
				attrs = {
					'class':'form-group',
					}
				),
		}
