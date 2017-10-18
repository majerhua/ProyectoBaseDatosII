from django.conf.urls import url
from . import views

from .views import (

    ProyectoList,
    ProyectoCreacion,
  	ProyectoDetail,
  	ProyectoDelete,
  	ProyectoUpdate,

    ProyectoDocsCreacion,
    ProyectoDocsDetail,
    ProyectoDocsUpdate,
    ProyectoDocsDelete,

    ProyectoCostoCreacion,
    ProyectoCostoDetail,
    ProyectoCostoUpdate,
    ProyectoCostoDelete,

)

urlpatterns = [

	url(r'^$', views.index, name='index'),
	url(r'^proyecto$', views.ProyectoListFunc, name='list_p'),
	url(r'^proyecto/nuevo$', ProyectoCreacion.as_view(), name='new_p'),
	url(r'^proyecto/(?P<pk>\d+)$', ProyectoDetail.as_view(), name='det_p'),
	url(r'^proyecto/actualizar/(?P<pk>\d+)$', ProyectoUpdate.as_view(), name='upd_p'),
	url(r'^proyecto/eliminar/(?P<pk>\d+)$', ProyectoDelete.as_view(), name='del_p'),

  url(r'^proyectodocs$', views.ProyectoDocsListFunc, name='list_pd'),
  url(r'^proyectodocs/nuevo$',ProyectoDocsCreacion.as_view(), name='new_pd'),
  url(r'^proyectodocs/(?P<pk>\d+)$', ProyectoDocsDetail.as_view(), name='det_pd'),
  url(r'^proyectodocs/actualizar/(?P<pk>\d+)$', ProyectoDocsUpdate.as_view(), name='upd_pd'),
  url(r'^proyectodocs/eliminar/(?P<pk>\d+)$', ProyectoDocsDelete.as_view(), name='del_pd'),

  url(r'^proyectocosto$', views.ProyectoCostoListFunc, name='list_pc'),
  url(r'^proyectocosto/nuevo$',ProyectoCostoCreacion.as_view(), name='new_pc'),
  url(r'^proyectocosto/(?P<pk>\d+)$', ProyectoCostoDetail.as_view(), name='det_pc'),
  url(r'^proyectocosto/actualizar/(?P<pk>\d+)$', ProyectoCostoUpdate.as_view(), name='upd_pc'),
  url(r'^proyectocosto/eliminar/(?P<pk>\d+)$', ProyectoCostoDelete.as_view(), name='del_pc'),


  url(r'^series/$', views.serie_list),
  url(r'^series/(?P<pk>[0-9]+)/$', views.serie_detail),

]