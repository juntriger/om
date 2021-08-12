from django.urls import path

from . import views

app_name = 'opman'

urlpatterns = [
    path('', views.base_views.index, name='index'),
    path('order/process/', views.base_views.order_process, name='order_process'),


    path('search/', views.search_views.search_order, name='search_order'),
    path('excel_paste.html', views.search_views.excel_paste, name='excel_paste'),
    path('searchbystr/', views.search_views.search_order_by_str, name='search_order_by_str'),

    path('export_order_xlsx/', views.export_order_xlsx, name='export_order_xlsx'),
    path('fileupload/', views.update_views.file_upload, name='file_upload'),

    path('watchlist/', views.watchlist_views.watchlist, name='watchlist'),
    path('watchlist/add/<str:_id_str>', views.watchlist_views.add_watch_user, name='add_watch_user'),
    path('watchlist/del/<str:_id_str>', views.watchlist_views.del_watch_user, name='del_watch_user'),

    path('order/mention/view/<int:order_id>', views.mention_views.mention_view, name='mention_view'),
    path('order/mention/create/<int:mention_id>', views.mention_views.mention_create, name='mention_create'),
    path('order/mention/modify/<int:mention_id>', views.mention_views.mention_modify, name='mention_modify'),
    path('order/mention/delete/<int:mention_id>', views.mention_views.mention_delete, name='mention_delete'),

]