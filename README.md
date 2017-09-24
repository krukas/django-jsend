Django Jsend
============
Django view for sending Jsend responses.

Instalation
===========
To install the Django library:
    
    pip install django_jsend

Usage
=====

.. code:: python

    from django_jsend import JsendView
    
    class CustomJsendView(JsendView):

    	def handle_request(self, request, param_id=None):
    	    if not param_id:
    	        raise Exception('Param id could not be empty')
    	   return {
    	        'some': 'date',
    	        'object': param_id,
    	   }
    
    # urls
    url(r'^custom/(?P<param_id>\w+)/$', CustomJsendView.as_view(), name='custom')
