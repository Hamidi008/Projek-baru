from django.contrib import admin

# Register your models here.

from . models import *

admin.site.register(AccountType)
admin.site.register(Account)
admin.site.register(CounterPart)
admin.site.register(LegderMeta)
admin.site.register(TransactionObject)
admin.site.register(CenterTable)
admin.site.register(LedgerDetail)