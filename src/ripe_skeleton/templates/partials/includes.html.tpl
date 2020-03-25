<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename = 'css/base.css') }}" />
<link rel="shortcut icon" href="{{ url_for('static', filename = 'images/favicon.png') }}" />
<script type="text/javascript" src="{{ url_for('static', filename = 'dist/bundle.js', compress = 'js') }}"></script>
{% for plugin in owner.plugins %}
    {% for stylesheet in plugin.stylesheets %}
        <link rel="stylesheet" type="text/css" href="{{ stylesheet.url }}" />
    {% endfor %}
    {% for script in plugin.scripts %}
        <script type="text/javascript" src="{{ script.url }}"></script>
    {% endfor %}
{% endfor %}
