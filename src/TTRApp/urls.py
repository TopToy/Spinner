from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('state/height', views.height, name='height'),
    path('state/liveness', views.liveness, name='liveness'),
    path('state/pool_size', views.pool_size, name='pool_size'),
    path('state/pending_size', views.pending_size, name='pending_size'),
    path('state/validators', views.validators, name='validators'),
    path('state/info', views.info, name='info'),
    path('transactions/<int:cid>&<int:worker>&<int:pid>&<int:bid>&<int:tx_num>&<int:blocking>',
         views.read_tx, name='read_tx'),
    path('transactions/status/<int:cid>&<int:worker>&<int:pid>&<int:bid>&<int:tx_num>&<int:blocking>',
         views.tx_status, name='tx_status'),
    path('transactions/write/<int:cid>',
         views.write_tx, name='write_tx'),
    path('blocks/<int:cid>&<int:height>&<int:blocking>',
         views.read_block, name='read_block'),

]