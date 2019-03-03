from pyramid.view import view_config
from ..services.main_record import MainRecord


@view_config(route_name='main',
             renderer='bfg_test:templates/main.jinja2')
def main(request):
   
	page = int(request.params.get('page', 1))
	paginator = MainRecord.get_paginator(request, page)
	return {'paginator': paginator}