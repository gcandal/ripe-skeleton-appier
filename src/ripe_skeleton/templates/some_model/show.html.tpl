{% extends "partials/layout.html.tpl" %}
{% block content %}
    {{ super() }}
    <div class="some-model">
        <h1>{{ "Some Model"|locale }}</h1>
        <div class="key">{{ "ID"|locale }}</div>
        <div class="value">{{ some_model.id }}</div>
    </div>
{% endblock %}
