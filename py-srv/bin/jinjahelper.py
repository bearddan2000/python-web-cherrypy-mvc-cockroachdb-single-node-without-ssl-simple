from jinja2 import Environment, FileSystemLoader, TemplateNotFound

class JinjaHelper:
    def __init__(self, base_path):
        self.base_path = base_path

    def get_template(self, path):
        try:
            env = Environment(loader=FileSystemLoader(['{0}/templates'.format(self.base_path),
                                                       '{0}/templates/{1}'.format(self.base_path, path)]))
            return env.get_template(path)
        except TemplateNotFound:
            return None

    def render(self, path, template_vars):
        try:
            return self.get_template(path).render(template_vars)
        except Exception as ex:
            Logger.error('Error rendering template', ex)
