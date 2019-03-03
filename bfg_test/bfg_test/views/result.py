from pyramid.view import view_config





@view_config(route_name='result',
             renderer='pyramid_blogr:templates/result.jinja2')
def results(request):
    return {}


    # def result(self):
    #     try:
    #         page = self.request.params['page']
    #         if page and page.isdigit():
    #             page = int(page)
    #         else:
    #             page = 1
    #     except:
    #         page = 1

    #     print('Search result')

        
    #     query = self.request.params['query']
    #     print(query)
    #     if DBSession.query(AllResults).filter_by(title=str(query)).first():
    #         result = DBSession.query(Search).filter_by(label=str(query)).all()
    #         return dict(result=result)
    #     else:
    #         DBSession.add(AllResults(title=query, name=str(query)+'_vrewrgtrgtrgtrg'))

    #         for p in range(1, 10):
    #             r = requests.get('http://api.stackexchange.com/2.2/search?', 
    #             params = {
    #             'page' : p,
    #             'order' : 'desc', 
    #             'sort' : 'activity', 
    #             'tagged' : prob_to_tchkzpt(query),
    #             'site' : 'stackoverflow',
    #             'pagesize' : 25
    #                     }
    #             )       
    #             for i in range(len(r.json()['items'])):
    #                 title = r.json()['items'][i]['title']
    #                 name = r.json()['items'][i]['owner']['display_name']
    #                 label = str(query)
    #                 DBSession.add(Search(title=title, name=name, label=label))

    #     result = DBSession.query(Search).filter_by(label=str(query)).all()

    #     # print(result)
        
    #     return dict(result=result)