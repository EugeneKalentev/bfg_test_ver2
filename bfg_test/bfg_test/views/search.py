from pyramid.view import view_config


@view_config(route_name='search',
             renderer='pyramid_blogr:templates/search.jinja2')
def search(request):
    return {}

  
    # print('Incoming request')
    # name = 'EugeneKalentev'

    # return dict(name=name)