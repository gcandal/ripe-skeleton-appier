{% block html %}
    {% set htitle = "RIPE Retail" %}
    {% set hauthor = "PLATFORME" %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            {% block head scoped %}
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1, minimum-scale=1, maximum-scale=1" />
                <meta name="theme-color" content="#2d2d2d" />
                {% for meta in metatags %}
                    <meta name="{{ meta.name }}" content="{{ meta.content }}" />
                {% endfor %}
                {% block title scoped %}
                    <meta name="title" content="{{ htitle }}" />
                {% endblock %}
                {% block description scoped %}
                    <meta name="description" content="{{ bdescription }}" />
                {% endblock %}
                {% block keywords scoped %}
                    <meta name="keywords" content="{{ bkeywords }}" />
                {% endblock %}
                {% block author scoped %}
                    <meta name="author" content="{{ hauthor }}" />
                {% endblock %}
                {% block og scoped %}
                    <meta property="og:type" content="website" />
                    <meta property="og:site_name" content="{{ htitle }}" />
                {% endblock %}
                {% block canonical scoped %}
                    <link rel="canonical" href="{{ url_for('location', absolute = True) }}" />
                {% endblock %}
                {% block includes scoped %}
                    {% include "partials/includes.html.tpl" with context %}
                {% endblock %}
                <title>{% block htitle scoped %}{{ htitle }}{% endblock %}</title>
            {% endblock %}
        </head>
        <body class="ripe-skeleton {% if own.is_admin %}is-admin{% endif %} {% block body_cls %}{% endblock %}" ontouchstart="">
            {% block content scoped %}{% endblock %}
        </body>
    </html>
{% endblock %}
