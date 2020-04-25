{
    'name': 'alquimia',
    'summary': 'Gestión Club de Patinaje Alquimia',
    'description': 'Módulo de Gestión del Club de Patinaje Alquimia. Incluye Gestión de Personal, Socios y Website',
    'author': 'Javier Fernández Peón',
    'website': 'http://cpalquimia.com',
    'category': 'Uncategorized',
    'version': '13.0.1',
    'depends': ['base', 'website', 'website_blog', 'hr_attendance'],
    'data': [
        'views/views.xml',
        'views/templates.xml',
	'data/blog_blog.xml',
	'data/user_groups.xml',		
	'security/ir.model.access.csv',
	'security/rules.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
