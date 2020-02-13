from django.db import models

# Create your models here.
from . validators import validate_transaksi

class AccountType(models.Model):
    akun_tipe_id          = models.IntegerField(primary_key=True, default=0)
    akun_tipe_nama        = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.akun_tipe_id)


class Account(models.Model):
    nomor_akun           = models.IntegerField(primary_key=True, default=0)
    nama_akun            = models.CharField(max_length=255)
    deskripsi_akun       = models.TextField()
    akun_tipe_id         = models.ForeignKey(AccountType, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.nomor_akun)


class CounterPart(models.Model):
    counterpart_id      = models.IntegerField(primary_key=True, default=0)
    counterpart_name    = models.CharField(max_length=255)
    counterpart_code    = models.CharField(max_length=255)
    customer_link       = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.counterpart_id)


class LegderMeta(models.Model):
    ledger_id        = models.IntegerField(primary_key=True, default=0)
    ledger_name      = models.CharField(max_length=255)
    ledger_currency  = models.CharField(max_length=255)
    ledger_country   = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.ledger_id)


class TransactionObject(models.Model):
    transaksi_id            = models.IntegerField(primary_key=True, default=0)
    supporting_dokumen_id   = models.CharField(max_length=255)
    total_amount            = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.transaksi_id)

        
class CenterTable(models.Model):
    center_number   = models.IntegerField(primary_key=True, default=0)
    name            = models.CharField(max_length=255)
    description     = models.TextField()
    ledger_id       = models.ForeignKey(LegderMeta, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.center_number)


class LedgerDetail(models.Model):
    tanggal_transaksi         = models.DateTimeField(auto_now_add=True)
    transaksi_id              = models.ForeignKey(TransactionObject, on_delete=models.CASCADE, null=True)
    transaksi_deskripsi       = models.TextField(validators = [validate_transaksi])
    nomor_akun                = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    center_number             = models.ForeignKey(CenterTable, on_delete=models.CASCADE, blank=True, null=True)
    counterpart_id            = models.ForeignKey(CounterPart, on_delete=models.CASCADE, blank=True, null=True)
    reconciliation_reference  = models.CharField(max_length=255)
    accounting_periode        = models.CharField(max_length=255)
    financial_year            = models.CharField(max_length=255)
    amount_ForEX              = models.IntegerField(default=0)
    forEX_CCD                 = models.CharField(max_length=255)
    debet_ledger_currency     = models.IntegerField(default=0)
    credit_ledger_currency    = models.IntegerField(default=0)
    user_id                   = models.CharField(max_length=255)
    timestamp                 = models.DateTimeField(auto_now_add=True)
    ledger_id                 = models.ForeignKey(LegderMeta, on_delete=models.CASCADE, null=True)
    supporting_dokumen        = models.FileField(blank=True)

    def __str__(self):
        return "{}".format(self.tanggal_transaksi)

