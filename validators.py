from django.core.exceptions import ValidationError

def validate_transaksi(value):
	transaksi_input = value
	if transaksi_input == "anis":
		message = "Maaf, " + transaksi_input + " SUDAH ADA YG PUNYA"
		raise ValidationError(message)