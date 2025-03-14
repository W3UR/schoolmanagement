from django.apps import AppConfig


class TemplatesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'templates'

{% if user.is_authenticated %}
    <a href="{% url 'logout' %}">🚪 लॉगआउट</a>
{% else %}
    <a href="{% url 'login' %}">🔑 लॉगिन</a>
{% endif %}
