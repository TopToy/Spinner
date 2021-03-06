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
    path('transactions/cid=<int:cid>&worker=<int:worker>&pid=<int:pid>&'
         'bid=<int:bid>&tx_num=<int:tx_num>&blocking=<int:blocking>',
         views.read_tx, name='read_tx'),
    path('transactions/cid=<int:cid>&worker=<int:worker>&pid=<int:pid>&'
         'bid=<int:bid>&tx_num=<int:tx_num>&blocking=<int:blocking>/data',
         views.read_tx_data, name='read_tx_data'),
    path('transactions/cid=<int:cid>&worker=<int:worker>&pid=<int:pid>&'
         'bid=<int:bid>&tx_num=<int:tx_num>/status',
         views.tx_status, name='tx_status'),
    path('transactions/cid=<int:cid>',
         views.write_tx, name='write_tx'),
    path('blocks/cid=<int:cid>&height=<int:height>&blocking=<int:blocking>',
         views.read_block, name='read_block'),

]